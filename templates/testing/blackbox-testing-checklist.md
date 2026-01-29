# 黑盒测试 Checklist

> 本文档提供黑盒测试的审查维度框架，包括 E2E 测试、集成测试、性能测试（DFX）

## 审查维度说明

本文档提供**黑盒测试的审查维度和框架**。基于这些维度对黑盒测试进行深度分析，识别问题和改进空间。

**适用场景**：
- 验证阶段的用户场景测试（E2E）
- 功能集成测试（API/DB/外部服务）
- 性能测试（DFX - Design for X）

**与其他模板的关系**：
- 与 `testing-checklist-*.md`（白盒测试）互补
- 白盒测试关注代码结构和单元测试覆盖率
- 黑盒测试关注用户场景和系统集成质量

---

## 维度 1: E2E 测试

### 1.1 用户旅程覆盖

**维度说明**: E2E 测试是否覆盖关键用户旅程，基于 Discovery 阶段的 User Story 验收标准。

**审查要点**:
- [ ] 基于 Discovery Story 验收标准（Given-When-Then）生成测试
- [ ] 覆盖关键用户流程（登录、注册、购买、查询等）
- [ ] 包含快乐路径和错误场景
- [ ] 用户角色覆盖完整（管理员、普通用户、访客等）
- [ ] 业务流程端到端完整

**深度分析方向**:
- 用户旅程是否从入口到出口完整验证
- 是否有遗漏的关键业务流程
- 错误场景是否考虑（异常输入、网络错误、权限不足）
- 跨页面/跨模块的流程是否验证
- 业务规则是否正确实现

**相关模式**: `everything-claude-code:e2e-runner`

---

### 1.2 测试稳定性

**维度说明**: E2E 测试是否稳定可靠，避免间歇性失败（flaky tests）。

**审查要点**:
- [ ] 使用 `data-testid` 定位器（而非脆弱的 CSS 选择器）
- [ ] 正确处理异步加载（等待元素可见/可点击）
- [ ] 避免 hard-coded 等待时间（使用动态等待）
- [ ] 无 flaky 测试（连续运行 3 次全部通过）
- [ ] 测试之间相互独立（无共享状态）
- [ ] 测试数据隔离（每次测试使用独立数据）

**深度分析方向**:
- 测试是否可靠（一致性）
- 是否有间歇性失败（随机性）
- 等待策略是否合理（过度等待 vs 等待不足）
- 选择器是否健壮（class、XPath 可能变化）
- 测试数据是否可重复使用

**最佳实践**:
```typescript
// ✅ Good - 使用 data-testid
await page.click('[data-testid=submit-button]');

// ❌ Bad - 脆弱的 CSS 选择器
await page.click('.btn.btn-primary.btn-lg');
```

---

### 1.3 Artifact 管理

**维度说明**: E2E 测试是否生成足够的调试信息（截图、视频、trace）。

**审查要点**:
- [ ] 失败时自动截图
- [ ] 视频记录整个测试过程
- [ ] Trace 文件生成（网络请求、控制台日志）
- [ ] 日志记录完整（动作、断言、错误）
- [ ] Artifact 存储和访问便捷
- [ ] CI/CD 集成时自动上传

**深度分析方向**:
- 失败时是否有足够的调试信息
- Artifact 是否易于访问和分析
- 是否支持回放测试过程
- Trace 文件是否包含完整上下文
- 存储（磁盘、云）是否合理配置

**Playwright Artifact 配置示例**:
```typescript
// playwright.config.ts
export default defineConfig({
  use: {
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    trace: 'retain-on-failure',
  },
});
```

---

### 1.4 跨平台兼容性

**维度说明**: E2E 测试是否验证跨平台兼容性（浏览器、设备、响应式）。

**审查要点**:
- [ ] 多浏览器测试（Chromium, Firefox, WebKit）
- [ ] 响应式设计测试（桌面、平板、手机）
- [ ] 移动端测试（触摸操作、手势）
- [ ] 设备兼容性（不同分辨率、DPI）
- [ ] 操作系统兼容性（Windows, macOS, Linux）
- [ ] 浏览器版本兼容性（最新版、前版本）

**深度分析方向**:
- 是否有浏览器特定的问题
- 响应式布局是否正确
- 移动端触摸操作是否正常
- 不同设备下的性能表现
- 浏览器 API 兼容性问题

**跨浏览器测试配置**:
```typescript
// playwright.config.ts
export default defineConfig({
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
    { name: 'webkit', use: { ...devices['Desktop Safari'] } },
    { name: 'Mobile Chrome', use: { ...devices['Pixel 5'] } },
  ],
});
```

---

## 维度 2: 集成测试

### 2.1 API 功能测试

**维度说明**: API 功能是否完整验证，包括请求/响应契约、错误处理。

**审查要点**:
- [ ] RESTful/GraphQL 端点验证
- [ ] 请求/响应契约验证（OpenAPI/Swagger）
- [ ] 错误码验证（4xx, 5xx）
- [ ] 边界条件验证（空输入、极值、特殊字符）
- [ ] 数据格式验证（JSON, XML）
- [ ] 认证/授权验证（JWT, OAuth, API Key）

**深度分析方向**:
- API 是否符合契约定义
- 错误处理是否完善
- 边界条件是否考虑
- 数据验证是否严格
- 认证/授权是否安全

**测试工具**:
- JavaScript/TypeScript: Jest + Supertest
- Python: pytest + requests
- Go: testing + httptest

**示例测试**:
```typescript
// tests/integration/api/users-api.test.ts
import request from 'supertest';
import app from '../../src/app';

describe('Users API Integration Tests', () => {
  test('POST /api/users should create user and return 201', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({
        email: 'test@example.com',
        password: 'SecurePass123'
      });

    expect(response.status).toBe(201);
    expect(response.body).toHaveProperty('id');
    expect(response.body.email).toBe('test@example.com');
  });

  test('POST /api/users with invalid email should return 400', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({ email: 'invalid-email', password: 'pass' });

    expect(response.status).toBe(400);
    expect(response.body).toHaveProperty('error');
  });
});
```

---

### 2.2 数据库集成

**维度说明**: 数据库集成是否正确，包括 CRUD 操作、事务、数据一致性。

**审查要点**:
- [ ] CRUD 操作完整性（Create, Read, Update, Delete）
- [ ] 事务隔离（ACID 属性验证）
- [ ] 数据一致性验证（外键约束、唯一约束）
- [ ] 并发控制（乐观锁、悲观锁）
- [ ] 数据迁移验证（Schema 变更）
- [ ] 查询性能验证（索引、N+1 问题）

**深度分析方向**:
- 数据库操作是否完整
- 事务是否正确隔离
- 数据一致性是否保证
- 并发场景是否处理
- 数据迁移是否安全
- 查询性能是否优化

**测试策略**:
- 使用测试数据库（Docker/内存数据库）
- 每个测试独立事务
- 测试后自动清理（rollback）
- 使用 fixture 加载测试数据

**示例测试**:
```python
# tests/integration/database/test_user_repository.py
import pytest
from src.repositories.user_repository import UserRepository

@pytest.fixture
def db_session():
    """创建测试数据库会话"""
    session = create_test_session()
    yield session
    session.rollback()
    session.close()

def test_create_user(db_session):
    """测试创建用户"""
    repo = UserRepository(db_session)
    user = repo.create({
        'email': 'test@example.com',
        'password_hash': 'hash'
    })

    assert user.id is not None
    assert user.email == 'test@example.com'

def test_delete_user_cascade(db_session):
    """测试删除用户级联"""
    repo = UserRepository(db_session)
    user = repo.create({'email': 'test@example.com', 'password_hash': 'hash'})
    user_id = user.id

    repo.delete(user_id)

    # 验证级联删除（如订单、收藏等）
    assert repo.find_by_id(user_id) is None
```

---

### 2.3 外部服务集成

**维度说明**: 外部服务集成是否稳定，包括第三方 API、错误处理、重试逻辑。

**审查要点**:
- [ ] 第三方 API 调用正确性
- [ ] 错误和重试逻辑（指数退避、熔断）
- [ ] 超时处理（连接超时、读取超时）
- [ ] 认证/授权验证（API Key, OAuth）
- [ ] 限流处理（Rate Limit）
- [ ] 降级策略（Fallback）

**深度分析方向**:
- 外部服务调用是否正确
- 错误处理是否完善
- 重试机制是否合理
- 超时设置是否恰当
- 认证是否安全
- 降级策略是否有效

**Mock vs 真实集成**:
- **高优先级**: 使用真实测试环境（如 Stripe Test Mode）
- **中优先级**: 使用 Mock Server（如 MSW）
- **低优先级**: 单元测试级别的 mock

**示例测试**:
```typescript
// tests/integration/external/payment-service.test.ts
import { PaymentService } from '../../src/services/payment';

describe('Payment Service Integration', () => {
  test('should charge payment successfully', async () => {
    const service = new PaymentService(process.env.STRIPE_TEST_KEY);
    const result = await service.charge({
      amount: 1000,
      currency: 'usd',
      source: 'tok_visa', // Stripe test token
    });

    expect(result.status).toBe('succeeded');
    expect(result.amount).toBe(1000);
  });

  test('should handle network timeout', async () => {
    const service = new PaymentService(process.env.STRIPE_TEST_KEY, {
      timeout: 1, // 1ms timeout
    });

    await expect(
      service.charge({ amount: 1000, currency: 'usd', source: 'tok_visa' })
    ).rejects.toThrow('timeout');
  });
});
```

---

### 2.4 测试数据管理

**维度说明**: 测试数据是否合理管理，包括 fixture、数据隔离、清理机制。

**审查要点**:
- [ ] Fixture 设计合理（可复用、易维护）
- [ ] 测试数据隔离（每个测试独立数据）
- [ ] 清理机制完整（自动清理、回滚）
- [ ] 真实数据场景覆盖（边界值、异常值）
- [ ] 敏感数据脱敏（密码、token）
- [ ] 数据工厂模式（Factory Boy、Faker）

**深度分析方向**:
- 测试数据是否易于管理
- 数据隔离是否有效
- 清理是否完整
- 真实场景是否覆盖
- 敏感数据是否保护
- 数据生成是否高效

**示例 Fixture**:
```python
# tests/fixtures/user_fixtures.py
import pytest
from factory import Factory
from faker import Faker

fake = Faker()

class UserFactory(Factory):
    class Meta:
        model = User

    email = lambda: fake.email()
    password_hash = lambda: fake.sha256()
    name = lambda: fake.name()

@pytest.fixture
def user_factory(db_session):
    """创建用户工厂"""
    def create(**kwargs):
        user = UserFactory.create(**kwargs)
        db_session.add(user)
        db_session.commit()
        return user
    return create

# 使用
def test_update_user(user_factory):
    user = user_factory(name='Alice')
    # 测试逻辑...
```

---

## 维度 3: 性能测试（DFX）

### 3.1 响应时间

**维度说明**: 响应时间是否达标，包括 P50/P95/P99 百分位数。

**审查要点**:
- [ ] P50/P95/P99 基线设定（符合业务需求）
- [ ] API 响应时间验证（REST, GraphQL）
- [ ] 页面加载时间验证（FCP, LCP, TTI）
- [ ] 数据库查询时间验证（慢查询检测）
- [ ] 基线符合业务需求（用户体验）
- [ ] 性能回归检测（对比历史数据）

**深度分析方向**:
- 响应时间是否合理
- 百分位数是否设定正确
- 瓶颈在哪里（数据库、网络、计算）
- 性能回归是否及时发现
- 性能预算是否设置
- 性能监控是否完善

**性能基线示例**:
```javascript
// k6/config/benchmarks.yaml
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500', 'p(99)<1000'],
    http_req_waiting: ['p(95)<400'],
    http_req_connecting: ['p(95)<100'],
  },
};
```

**响应时间标准**:
| 类型 | P50 | P95 | P99 |
|-----|-----|-----|-----|
| 静态页面 | < 200ms | < 500ms | < 1000ms |
| API 查询 | < 100ms | < 300ms | < 500ms |
| API 写入 | < 200ms | < 500ms | < 1000ms |
| 复杂查询 | < 500ms | < 1500ms | < 3000ms |

---

### 3.2 并发能力

**维度说明**: 系统并发能力是否达标，包括并发用户、错误率、稳定性。

**审查要点**:
- [ ] 并发用户测试（逐步增加负载）
- [ ] 错误率验证（< 1% 为合格）
- [ ] 稳定性验证（长时间运行）
- [ ] 资源竞争处理（数据库连接池、锁）
- [ ] 死锁检测（数据库、应用层）
- [ ] 内存泄漏检测（长时间运行）

**深度分析方向**:
- 并发能力是否达标
- 错误率是否在可接受范围
- 系统是否稳定（无崩溃）
- 资源竞争是否正确处理
- 死锁是否发生
- 内存是否泄漏

**并发测试场景**:
```javascript
// k6/tests/concurrent-users.js
export const options = {
  stages: [
    { duration: '2m', target: 100 },  // 2分钟爬升到100用户
    { duration: '5m', target: 100 },  // 维持100用户5分钟
    { duration: '2m', target: 200 },  // 爬升到200用户
    { duration: '5m', target: 200 },  // 维持200用户5分钟
    { duration: '2m', target: 0 },    // 降到0
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],     // 错误率 < 1%
    http_req_duration: ['p(95)<2000'],  // 95%请求 < 2s
  },
};
```

**验收标准**:
- 错误率 < 1%
- P95 响应时间 < 2s
- 无内存泄漏
- 数据库连接池正常
- 无死锁

---

### 3.3 负载测试

**维度说明**: 负载测试是否识别性能瓶颈和崩溃点。

**审查要点**:
- [ ] 瓶颈识别（数据库、CPU、网络、I/O）
- [ ] 崩溃点测试（最大并发用户数）
- [ ] 恢复能力测试（负载下降后恢复）
- [ ] 容量规划（预估最大负载）
- [ ] 水平扩展验证（增加实例）
- [ ] 垂直扩展验证（增加资源）

**深度分析方向**:
- 系统瓶颈在哪里
- 最大并发用户数是多少
- 崩溃点是什么
- 恢复能力如何
- 容量规划是否合理
- 扩展策略是否有效

**负载测试场景**:
```javascript
// k6/tests/load-test.js
export const options = {
  stages: [
    { duration: '5m', target: 50 },
    { duration: '5m', target: 100 },
    { duration: '5m', target: 200 },
    { duration: '5m', target: 400 },
    { duration: '5m', target: 800 },
    { duration: '10m', target: 0 },  // 恢复阶段
  ],
};
```

**输出分析**:
- 最大并发用户数
- 崩溃点识别
- 瓶颈分析（数据库/CPU/网络）
- 容量规划建议

---

### 3.4 资源监控

**维度说明**: 资源使用是否合理，包括 CPU、内存、磁盘 I/O、网络。

**审查要点**:
- [ ] CPU 使用率监控（用户态、内核态）
- [ ] 内存使用监控（堆、栈、泄漏）
- [ ] 磁盘 I/O 监控（读写、IOPS）
- [ ] 网络监控（带宽、延迟、丢包）
- [ ] 数据库连接池监控（活跃连接、空闲连接）
- [ ] 缓存命中率监控（Redis、Memcached）

**深度分析方向**:
- CPU 使用是否合理
- 内存是否泄漏
- I/O 是否瓶颈
- 网络是否瓶颈
- 连接池是否合理配置
- 缓存是否有效

**监控命令**:
```bash
# CPU 使用率
top -b -n 1 | grep "Cpu(s)"

# 内存使用
free -m

# 磁盘 I/O
iostat -x 1

# 数据库连接池
# PostgreSQL
SELECT count(*) FROM pg_stat_activity;

# Redis 连接数
redis-cli INFO clients
```

**资源使用标准**:
| 资源 | 警告阈值 | 危险阈值 |
|-----|---------|---------|
| CPU 使用率 | 70% | 90% |
| 内存使用率 | 70% | 85% |
| 磁盘 I/O | 60% | 80% |
| 网络带宽 | 70% | 90% |

---

### 3.5 DFX 维度覆盖

**维度说明**: DFX（Design for X）维度是否覆盖完整。

**审查要点**:

#### 3.5.1 性能 (Performance)
- [ ] 响应时间达标（P50/P95/P99）
- [ ] 吞吐量达标（QPS, TPS）
- [ ] 资源使用合理（CPU、内存、I/O）
- [ ] 性能预算设置
- [ ] 性能监控完善

#### 3.5.2 可靠性 (Reliability)
- [ ] 错误率 < 0.1%
- [ ] 故障恢复时间（MTTR）
- [ ] 数据一致性保证
- [ ] 故障转移测试
- [ ] 备份恢复测试

#### 3.5.3 可扩展性 (Scalability)
- [ ] 水平扩展能力（增加实例）
- [ ] 垂直扩展能力（增加资源）
- [ ] 缓存策略有效性
- [ ] 负载均衡测试
- [ ] 分库分表能力

#### 3.5.4 可维护性 (Maintainability)
- [ ] 监控点完整（指标、日志、追踪）
- [ ] 日志记录完整（结构化、分级）
- [ ] 告警机制有效（阈值、通知）
- [ ] 文档完善（API、架构、运维）
- [ ] 故障排查流程

#### 3.5.5 安全性 (Security)
- [ ] 认证性能（JWT 验证时间）
- [ ] 加密性能（TLS、AES）
- [ ] DDoS 防护测试
- [ ] SQL 注入防护测试
- [ ] XSS 防护测试

**深度分析方向**:
- DFX 各维度是否覆盖
- 性能指标是否达标
- 可靠性是否保证
- 可扩展性是否支持
- 可维护性是否完善
- 安全性是否考虑

---

## 质量评估矩阵

### 评分标准

| 维度 | 权重 | 评分标准说明 | 评分 (1-5) |
|-----|------|------------|-----------|
| **E2E 测试** | **30%** | | **___** |
| - 用户旅程覆盖 | 10% | 覆盖关键流程、包含错误场景 | |
| - 测试稳定性 | 8% | 无 flaky 测试、选择器健壮 | |
| - Artifact 管理 | 6% | 截图、视频、trace 完整 | |
| - 跨平台兼容性 | 6% | 多浏览器、响应式、移动端 | |
| **集成测试** | **30%** | | **___** |
| - API 功能测试 | 10% | 端点完整、契约验证、错误处理 | |
| - 数据库集成 | 10% | CRUD 完整、事务隔离、数据一致性 | |
| - 外部服务集成 | 5% | 调用正确、错误处理、重试逻辑 | |
| - 测试数据管理 | 5% | Fixture 合理、数据隔离、清理完整 | |
| **性能测试** | **40%** | | **___** |
| - 响应时间 | 12% | P50/P95/P99 达标、基线合理 | |
| - 并发能力 | 10% | 错误率 <1%、稳定性验证 | |
| - 负载测试 | 8% | 瓶颈识别、崩溃点测试 | |
| - 资源监控 | 5% | CPU/内存/I/O 监控 | |
| - DFX 维度覆盖 | 5% | 性能/可靠性/可扩展性/可维护性/安全性 | |

### 评分说明

| 分数 | 说明 |
|-----|------|
| **5.0** | 优秀 - 该维度表现卓越，超出预期 |
| **4.0** | 良好 - 该维度表现优秀，符合预期 |
| **3.0** | 合格 - 该维度表现达标，基本符合预期 |
| **2.0** | 需改进 - 该维度存在较多问题 |
| **1.0** | 不合格 - 该维度严重不足 |

### 总分计算

```
总分 = (E2E 测试得分 × 0.30) +
       (集成测试得分 × 0.30) +
       (性能测试得分 × 0.40)
```

**满分**: 5.0

---

## 质量等级

| 总分范围 | 质量等级 | 说明 |
|---------|---------|------|
| **4.5 - 5.0** | 优秀 | 黑盒测试质量卓越，覆盖完整 |
| **4.0 - 4.4** | 良好 | 黑盒测试质量优秀，有小幅改进空间 |
| **3.5 - 3.9** | 合格 | 黑盒测试质量达标，有明显改进空间 |
| **3.0 - 3.4** | 需改进 | 黑盒测试存在较多问题 |
| **< 3.0** | 不合格 | 黑盒测试质量严重不足 |

---

## 审查结果汇总模板

```markdown
# 黑盒测试质量审查报告

## 审查概述
- **审查时间**: YYYY-MM-DD HH:MM
- **审查类型**: E2E 测试 / 集成测试 / 性能测试 / 全部
- **测试框架**: Playwright / k6 / JMeter / Supertest / pytest / 其他
- **审查人**: [姓名/角色]

## 审查框架
基于 `templates/testing/blackbox-testing-checklist.md` 提供的审查维度：

### 1. E2E 测试（权重 30%）
- 用户旅程覆盖（10%）
- 测试稳定性（8%）
- Artifact 管理（6%）
- 跨平台兼容性（6%）

### 2. 集成测试（权重 30%）
- API 功能测试（10%）
- 数据库集成（10%）
- 外部服务集成（5%）
- 测试数据管理（5%）

### 3. 性能测试（权重 40%）
- 响应时间（12%）
- 并发能力（10%）
- 负载测试（8%）
- 资源监控（5%）
- DFX 维度覆盖（5%）

## 各维度深度审查

### 1. E2E 测试维度

#### 1.1 用户旅程覆盖（权重 10%）
**评分**: ___ / 5.0

**分析结果**:
- [ ] 基于 Discovery Story 验收标准生成测试
- [ ] 覆盖关键用户流程
- [ ] 包含快乐路径和错误场景
- [ ] 用户角色覆盖完整

**问题列表**:
- [问题 1] - [严重性: 高/中/低]
- [问题 2]

**改进建议**:
- [具体建议]

---

#### 1.2 测试稳定性（权重 8%）
**评分**: ___ / 5.0

**分析结果**:
- [ ] 使用 data-testid 定位器
- [ ] 正确处理异步加载
- [ ] 避免 hard-coded 等待时间
- [ ] 无 flaky 测试

**问题列表**:
- [问题]

**改进建议**:
- [具体建议]

---

#### 1.3 Artifact 管理（权重 6%）
**评分**: ___ / 5.0

**分析结果**:
- [ ] 失败时自动截图
- [ ] 视频记录
- [ ] Trace 文件生成
- [ ] 日志记录完整

**问题列表**:
- [问题]

**改进建议**:
- [具体建议]

---

#### 1.4 跨平台兼容性（权重 6%）
**评分**: ___ / 5.0

**分析结果**:
- [ ] 多浏览器测试
- [ ] 响应式设计测试
- [ ] 移动端测试
- [ ] 设备兼容性

**问题列表**:
- [问题]

**改进建议**:
- [具体建议]

---

### 2. 集成测试维度

#### 2.1 API 功能测试（权重 10%）
**评分**: ___ / 5.0

**分析结果**:
- [ ] RESTful/GraphQL 端点验证
- [ ] 请求/响应契约验证
- [ ] 错误码验证
- [ ] 边界条件验证

**问题列表**:
- [问题]

**改进建议**:
- [具体建议]

---

#### 2.2 数据库集成（权重 10%）
**评分**: ___ / 5.0

**分析结果**:
- [ ] CRUD 操作完整性
- [ ] 事务隔离
- [ ] 数据一致性
- [ ] 外键约束验证

**问题列表**:
- [问题]

**改进建议**:
- [具体建议]

---

#### 2.3 外部服务集成（权重 5%）
**评分**: ___ / 5.0

**分析结果**:
- [ ] 第三方 API 调用
- [ ] 错误和重试逻辑
- [ ] 超时处理
- [ ] 认证/授权验证

**问题列表**:
- [问题]

**改进建议**:
- [具体建议]

---

#### 2.4 测试数据管理（权重 5%）
**评分**: ___ / 5.0

**分析结果**:
- [ ] Fixture 设计合理
- [ ] 测试数据隔离
- [ ] 清理机制完整
- [ ] 真实数据场景覆盖

**问题列表**:
- [问题]

**改进建议**:
- [具体建议]

---

### 3. 性能测试维度

#### 3.1 响应时间（权重 12%）
**评分**: ___ / 5.0

**分析结果**:
- [ ] P50/P95/P99 基线设定
- [ ] API 响应时间验证
- [ ] 页面加载时间验证
- [ ] 基线符合业务需求

**性能基线**:
| 指标 | 基线 | 实际 | 状态 |
|-----|------|------|------|
| P50 | < 100ms | XX ms | ✅ / ❌ |
| P95 | < 500ms | XX ms | ✅ / ❌ |
| P99 | < 1000ms | XX ms | ✅ / ❌ |

**问题列表**:
- [问题]

**改进建议**:
- [具体建议]

---

#### 3.2 并发能力（权重 10%）
**评分**: ___ / 5.0

**分析结果**:
- [ ] 并发用户测试
- [ ] 错误率验证（<1%）
- [ ] 稳定性验证
- [ ] 资源竞争处理

**并发测试结果**:
| 并发数 | 错误率 | P95 响应时间 | 状态 |
|-------|--------|-------------|------|
| 100 | XX% | XX ms | ✅ / ❌ |
| 200 | XX% | XX ms | ✅ / ❌ |
| 400 | XX% | XX ms | ✅ / ❌ |

**问题列表**:
- [问题]

**改进建议**:
- [具体建议]

---

#### 3.3 负载测试（权重 8%）
**评分**: ___ / 5.0

**分析结果**:
- [ ] 瓶颈识别
- [ ] 崩溃点测试
- [ ] 恢复能力测试
- [ ] 容量规划

**负载测试结果**:
- **最大并发用户数**: XXX
- **崩溃点**: XXX 并发用户
- **瓶颈**: [数据库/CPU/网络/I/O]
- **恢复时间**: XX 秒

**问题列表**:
- [问题]

**改进建议**:
- [具体建议]

---

#### 3.4 资源监控（权重 5%）
**评分**: ___ / 5.0

**分析结果**:
- [ ] CPU 使用率监控
- [ ] 内存使用监控
- [ ] I/O 性能监控
- [ ] 连接池管理

**资源使用情况**:
| 资源 | 使用率 | 状态 |
|-----|--------|------|
| CPU | XX% | ✅ / ⚠️ / ❌ |
| 内存 | XX% | ✅ / ⚠️ / ❌ |
| 磁盘 I/O | XX% | ✅ / ⚠️ / ❌ |
| 网络 | XX% | ✅ / ⚠️ / ❌ |

**问题列表**:
- [问题]

**改进建议**:
- [具体建议]

---

#### 3.5 DFX 维度覆盖（权重 5%）
**评分**: ___ / 5.0

**分析结果**:
- [ ] 性能 - 响应时间、吞吐量达标
- [ ] 可靠性 - 错误率 < 0.1%、故障恢复
- [ ] 可扩展性 - 水平/垂直扩展能力
- [ ] 可维护性 - 监控、日志、告警完善
- [ ] 安全性 - 认证、加密、DDoS 防护

**DFX 覆盖情况**:
| DFX 维度 | 状态 | 说明 |
|---------|------|------|
| 性能 | ✅ / ⚠️ / ❌ | [说明] |
| 可靠性 | ✅ / ⚠️ / ❌ | [说明] |
| 可扩展性 | ✅ / ⚠️ / ❌ | [说明] |
| 可维护性 | ✅ / ⚠️ / ❌ | [说明] |
| 安全性 | ✅ / ⚠️ / ❌ | [说明] |

**问题列表**:
- [问题]

**改进建议**:
- [具体建议]

---

## 总体评估

### 质量等级
- **总分**: ___ / 5.0
- **质量等级**: 优秀 / 良好 / 合格 / 需改进 / 不合格

### 评分明细
| 维度 | 得分 | 权重 | 加权得分 |
|-----|------|------|---------|
| E2E 测试 | ___ / 5.0 | 30% | ___ |
| 集成测试 | ___ / 5.0 | 30% | ___ |
| 性能测试 | ___ / 5.0 | 40% | ___ |
| **总分** | | | **___ / 5.0** |

### 关键发现
**亮点**:
- [亮点 1]
- [亮点 2]

**主要问题**:
- [问题 1] - [影响: 高/中/低]
- [问题 2]

---

## 优先级问题清单

### 高优先级（必须修复）
1. **[问题标题]**
   - **位置**: [文件/行号]
   - **严重性**: CRITICAL
   - **影响**: [描述影响]
   - **修复建议**: [具体建议]

### 中优先级（建议修复）
1. **[问题标题]**
   - **位置**: [文件/行号]
   - **严重性**: MEDIUM
   - **影响**: [描述影响]
   - **修复建议**: [具体建议]

### 低优先级（可选优化）
1. **[问题标题]**
   - **位置**: [文件/行号]
   - **严重性**: LOW
   - **影响**: [描述影响]
   - **修复建议**: [具体建议]

---

## 改进计划

### 短期改进（1-2 周）
- [ ] [具体行动项 1]
- [ ] [具体行动项 2]
- [ ] [具体行动项 3]

### 中期改进（1-2 个月）
- [ ] [具体行动项 1]
- [ ] [具体行动项 2]

### 长期改进（3+ 个月）
- [ ] [具体行动项 1]
- [ ] [具体行动项 2]

---

## 附录

### 测试环境
- **操作系统**: [OS 版本]
- **浏览器**: [浏览器版本]
- **Node.js 版本**: [版本]
- **数据库**: [数据库版本]

### 测试工具
- **E2E 框架**: Playwright / Cypress / 其他
- **性能工具**: k6 / JMeter / 其他
- **API 测试**: Supertest / pytest / 其他

### 参考资料
- [Playwright 文档](https://playwright.dev/)
- [k6 文档](https://k6.io/docs/)
- [Testing Library](https://testing-library.com/)
```

---

## 与模板适配器的集成

### 使用方式

验证代理在执行黑盒测试时，会自动加载本 checklist：

```javascript
// 在 verification-agent 中使用
const blackboxChecklist = await templateAdapter.getBlackboxTestingChecklist();
const dimensions = blackboxChecklist.dimensions;

// 基于维度进行深度审查
const reviewResults = await reviewBlackboxTests(projectPath, dimensions);
```

### 相关 API

- `templateAdapter.getBlackboxTestingChecklist()` - 获取黑盒测试 checklist
- `templateAdapter.getE2ETestingFramework(projectPath)` - 检测 E2E 框架
- `templateAdapter.getPerformanceTestingTools()` - 获取性能测试工具配置

---

**记住**: 黑盒测试验证系统从用户视角的功能性和非功能性质量。与白盒测试（单元测试）互补，共同构成完整的质量保障体系。证据优于断言，永远如此。
