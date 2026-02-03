# Build Fix 模块

构建错误快速修复，增量式解决问题。

## 核心原则

### 最小化改动
- 只修复错误，不重构
- 不优化性能
- 不改变架构
- 一次修复一个错误

### 增量式修复
1. 运行构建
2. 解析错误输出
3. 逐个修复
4. 验证修复
5. 继续下一个

## 修复流程

### Step 1: 运行构建

```bash
# 检查项目构建
npm run build 2>&1 | tail -20

# 或
pnpm build 2>&1 | tail -20

# 或
yarn build 2>&1 | tail -20
```

### Step 2: 解析错误输出

**错误分组**:
- 按文件分组
- 按严重程度排序

**错误类型**:
- TypeScript 类型错误
- 语法错误
- 依赖问题
- 配置错误

### Step 3: 修复每个错误

对于每个错误：
1. 显示错误上下文（前后5行）
2. 解释问题
3. 提出修复方案
4. 应用修复
5. 重新运行构建
6. 验证错误已解决

### Step 4: 停止条件

如果满足以下条件则停止：
- 修复引入了新错误
- 同一错误持续3次尝试
- 用户请求暂停

### Step 5: 显示摘要

- 已修复错误
- 剩余错误
- 引入的新错误

**安全第一**: 一次修复一个错误！

## 常见错误模式与修复

### 模式 1: 类型推断失败

```typescript
// ❌ 错误: Parameter 'x' implicitly has an 'any' type
function add(x, y) {
  return x + y
}

// ✅ 修复: 添加类型注解
function add(x: number, y: number): number {
  return x + y
}
```

### 模式 2: Null/Undefined 错误

```typescript
// ❌ 错误: Object is possibly 'undefined'
const name = user.name.toUpperCase()

// ✅ 修复: 可选链
const name = user?.name?.toUpperCase()

// ✅ 或: Null 检查
const name = user && user.name ? user.name.toUpperCase() : ''
```

### 模式 3: 缺少属性

```typescript
// ❌ 错误: Property 'age' does not exist on type 'User'
interface User {
  name: string
}
const user: User = { name: 'John', age: 30 }

// ✅ 修复: 添加属性到接口
interface User {
  name: string
  age?: number // 如果不总是存在则可选
}
```

### 模式 4: 导入错误

```typescript
// ❌ 错误: Cannot find module '@/lib/utils'
import { formatDate } from '@/lib/utils'

// ✅ 修复 1: 检查 tsconfig 路径是否正确
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}

// ✅ 修复 2: 使用相对导入
import { formatDate } from '../lib/utils'
```

### 模式 5: 类型不匹配

```typescript
// ❌ 错误: Type 'string' is not assignable to type 'number'
const age: number = "30"

// ✅ 修复: 解析字符串为数字
const age: number = parseInt("30", 10)

// ✅ 或: 改变类型
const age: string = "30"
```

### 模式 6: 泛型约束

```typescript
// ❌ 错误: Type 'T' is not assignable to type 'string'
function getLength<T>(item: T): number {
  return item.length
}

// ✅ 修复: 添加约束
function getLength<T extends { length: number }>(item: T): number {
  return item.length
}
```

## 语言特定修复

### Python 构建/类型检查

```bash
# 类型检查
mypy --strict .

# 格式检查
black --check .
ruff check .

# 修复
mypy source_file.py
black source_file.py
ruff check --fix source_file.py
```

### Go 构建

```bash
# 构建
go build ./...

# 类型检查
go vet ./...

# 格式检查
gofmt -l .

# 修复
go fix ./...
gofmt -w .
```

### JavaScript/TypeScript

```bash
# 构建
npm run build

# 类型检查
npx tsc --noEmit

# Lint
npm run lint

# 修复
npx eslint . --fix
```

### C/C++

```bash
# 构建
make

# 或
cmake --build build

# 常见错误
# - 未声明标识符 → 添加 #include
# - 链接错误 → 添加链接库
# - 类型不匹配 → 添加显式转换
```

## 错误解析工具

### TypeScript 错误解析

```typescript
// 错误格式
// file.ts(line,col): error TScode: message

// 示例
// src/utils.ts(10,5): error TS2322: Type 'string' is not assignable to type 'number'

// 解析步骤
// 1. 文件: src/utils.ts
// 2. 位置: 第10行，第5列
// 3. 错误代码: TS2322
// 4. 消息: Type 'string' is not assignable to type 'number'
```

### Python 错误解析

```python
# 错误格式
# File "file.py", line N, in <scope>
#   Error message

# 示例
# File "src/utils.py", line 42, in <module>
#   NameError: name 'undefined_var' is not defined

# 解析步骤
# 1. 文件: src/utils.py
# 2. 位置: 第42行
# 3. 错误类型: NameError
# 4. 消息: name 'undefined_var' is not defined
```

## 最佳实践

1. **先读错误消息**: 它们通常很有帮助
2. **一次修复一个问题**: 不要同时修复多个
3. **验证修复**: 修复后重新运行构建
4. **理解根本原因**: 不要盲目修复
5. **保持简单**: 最小化改动
6. **记录修复**: 记录常见错误和解决方案
