# Database Diagnosis 模块

数据库诊断模块，优化查询性能和解决数据库问题。

## 触发条件

- 编写 SQL、创建迁移
- 设计模式
- 性能问题排查
- 数据库性能优化
- 死锁检测

## 查询性能审查

### 1. 索引使用检查

```bash
# 检查慢查询 (需要 pg_stat_statements)
psql -c "SELECT query, mean_exec_time, calls FROM pg_stat_statements ORDER BY mean_exec_time DESC LIMIT 10;"

# 检查表大小
psql -c "SELECT relname, pg_size_pretty(pg_total_relation_size(relid)) FROM pg_stat_user_tables ORDER BY pg_total_relation_size(relid) DESC;"

# 检查索引使用
psql -c "SELECT indexrelname, idx_scan, idx_tup_read FROM pg_stat_user_indexes ORDER BY idx_scan DESC;"

# 查找外键上缺失的索引
psql -c "SELECT conrelid::regclass, a.attname FROM pg_constraint c JOIN pg_attribute a ON a.attrelid = c.conrelid AND a.attnum = ANY(c.conkey) WHERE c.contype = 'f' AND NOT EXISTS (SELECT 1 FROM pg_index i WHERE i.indrelid = c.conrelid AND a.attnum = ANY(i.indkey));"

# 检查表膨胀
psql -c "SELECT relname, n_dead_tup, last_vacuum, last_autovacuum FROM pg_stat_user_tables WHERE n_dead_tup > 1000 ORDER BY n_dead_tup DESC;"
```

### 2. 查询计划分析

```sql
-- 使用 EXPLAIN ANALYZE 分析查询
EXPLAIN ANALYZE
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
WHERE u.created_at > '2024-01-01'
GROUP BY u.id
ORDER BY order_count DESC
LIMIT 10;

-- 检查是否有 Seq Scan（应该避免在大表上）
-- 检查行估计是否与实际匹配
-- 检查是否有 Nested Loop（可能是 N+1 问题）
```

### 3. N+1 查询检测

```python
# ❌ 错误: N+1 查询
def get_users_with_orders():
    users = db.query(User).all()
    for user in users:
        # 每个用户一次查询 = N+1
        user.orders = db.query(Order).filter_by(user_id=user.id).all()
    return users

# ✅ 正确: 使用 JOIN
def get_users_with_orders():
    return db.query(User).options(
        joinedload(User.orders)
    ).all()

# ✅ 或使用 subqueryload
def get_users_with_orders():
    return db.query(User).options(
        subqueryload(User.orders)
    ).all()
```

## 模式设计审查

### 1. 数据类型选择

```sql
-- ❌ 错误: 使用 VARCHAR 存储数字
CREATE TABLE users (
    id VARCHAR(50),  -- 应该使用 UUID 或整数
    balance VARCHAR(50)  -- 应该使用 DECIMAL
);

-- ✅ 正确: 使用合适的数据类型
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    balance DECIMAL(10, 2) NOT NULL DEFAULT 0
);
```

### 2. 索引策略

```sql
-- 为常用查询创建索引
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created_at ON users(created_at DESC);
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- 复合索引（考虑查询模式）
CREATE INDEX idx_orders_user_status ON orders(user_id, status);

-- 部分索引（只为需要的行创建索引）
CREATE INDEX idx_users_active ON users(email) WHERE active = true;
```

### 3. 外键约束

```sql
-- 确保外键上有索引（通常自动创建）
ALTER TABLE orders
ADD CONSTRAINT fk_orders_user_id
FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE;

-- 检查外键是否被正确索引
SELECT conrelid::regclass, a.attname
FROM pg_constraint c
JOIN pg_attribute a ON a.attrelid = c.conrelid AND a.attnum = ANY(c.conkey)
WHERE c.contype = 'f'
  AND NOT EXISTS (
    SELECT 1 FROM pg_index i
    WHERE i.indrelid = c.conrelid
    AND a.attnum = ANY(i.indkey)
  );
```

## 死锁诊断

### 1. 检测死锁

```sql
-- 查看当前锁
SELECT
    l.locktype,
    cl.relname AS table_name,
    l.mode,
    l.granted
FROM pg_locks l
JOIN pg_class cl ON l.relation = cl.oid
WHERE NOT l.granted;

-- 查看阻塞的查询
SELECT
    pid,
    now() - pg_stat_activity.query_start AS duration,
    query,
    state
FROM pg_stat_activity
WHERE (now() - pg_stat_activity.query_start) > interval '5 minutes';
```

### 2. 死锁预防

```python
# ❌ 错误: 以不同顺序访问表
def transfer_money(from_user, to_user, amount):
    db.execute(f"UPDATE users SET balance = balance - {amount} WHERE id = {from_user}")
    db.execute(f"UPDATE users SET balance = balance + {amount} WHERE id = {to_user}")

# ✅ 正确: 以相同顺序访问表
def transfer_money(from_user, to_user, amount):
    # 确保 from_id < to_id 以避免死锁
    if from_user > to_user:
        from_user, to_user = to_user, from_user
        amount = -amount

    db.execute(f"UPDATE users SET balance = balance + {amount} WHERE id = {from_user}")
    db.execute(f"UPDATE users SET balance = balance - {amount} WHERE id = {to_user}")
```

## Row Level Security (RLS)

### 1. 启用 RLS

```sql
-- 在所有表上启用 RLS
ALTER TABLE users ENABLE ROW LEVEL SECURITY;

-- 用户只能查看自己的数据
CREATE POLICY "Users view own data"
ON users FOR SELECT
USING (auth.uid() = id);

-- 用户只能更新自己的数据
CREATE POLICY "Users update own data"
ON users FOR UPDATE
USING (auth.uid() = id);
```

### 2. RLS 策略示例

```sql
-- 管理员可以查看所有数据
CREATE POLICY "Admins view all data"
ON users FOR SELECT
USING (
    EXISTS (
        SELECT 1 FROM user_roles
        WHERE user_id = auth.uid()
        AND role = 'admin'
    )
);

-- 用户可以查看公开数据
CREATE POLICY "Users view public data"
ON posts FOR SELECT
USING (is_public = true OR author_id = auth.uid());
```

## 连接管理

### 1. 连接池配置

```python
# PostgreSQL 连接池配置
from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,  # 根据应用需要调整
    host='localhost',
    database='mydb',
    user='user',
    password='password'
)

# 使用连接
conn = connection_pool.getconn()
try:
    # 执行查询
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
finally:
    connection_pool.putconn(conn)
```

### 2. 超时配置

```sql
-- 设置语句超时
SET statement_timeout = '30s';

-- 设置锁超时
SET lock_timeout = '5s';

-- 在应用中设置
-- Python
import psycopg2
conn = psycopg2.connect(
    dbname="mydb",
    options="-c statement_timeout=30000"
)
```

## 数据库性能优化

### 1. 批量操作

```python
# ❌ 错误: 逐个插入
for user in users:
    db.execute("INSERT INTO users (name) VALUES (?)", (user.name,))

# ✅ 正确: 批量插入
db.executemany(
    "INSERT INTO users (name) VALUES (?)",
    [(user.name,) for user in users]
)

# ✅ 或使用 COPY
import io
import csv

output = io.StringIO()
writer = csv.writer(output)
writer.writerows([(user.name,) for user in users])

cursor.copy_expert(
    "COPY users (name) FROM STDIN WITH CSV",
    output
)
```

### 2. 分页查询

```sql
-- ❌ 错误: OFFSET 分页（大 OFFSET 性能差）
SELECT * FROM orders ORDER BY created_at DESC LIMIT 10 OFFSET 1000;

-- ✅ 正确: 使用游标分页
SELECT * FROM orders
WHERE created_at < :last_created_at
ORDER BY created_at DESC
LIMIT 10;
```

## 监控与分析

### 1. 查询统计

```bash
# 启用 pg_stat_statements
shared_preload_libraries = 'pg_stat_statements'

# 查看最耗时的查询
SELECT
    query,
    calls,
    total_exec_time,
    mean_exec_time,
    stddev_exec_time
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;
```

### 2. 索引使用统计

```sql
-- 查看未使用的索引
SELECT
    schemaname,
    tablename,
    indexname,
    idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0
  AND indexname NOT LIKE '%_pkey';
```

## 常见问题诊断

### 问题 1: 查询慢

**诊断步骤**:
1. 运行 EXPLAIN ANALYZE
2. 检查是否有 Seq Scan
3. 检查行估计是否准确
4. 添加缺失的索引
5. 重写查询

### 问题 2: 连接耗尽

**诊断步骤**:
1. 检查活跃连接数
2. 检查空闲连接数
3. 检查连接池配置
4. 增加连接池大小或减少超时时间

### 问题 3: 数据库膨胀

**诊断步骤**:
1. 检查表大小
2. 检查死元组数量
3. 运行 VACUUM ANALYZE
4. 考虑定期自动清理
