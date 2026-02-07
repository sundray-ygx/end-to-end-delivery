# 最佳实践

## 核心原则

1. **Evidence Before Claims** - 证据优先于断言
2. **Quality First** - 质量第一
3. **Continuous Learning** - 持续学习

## 从小开始

### 1. 简单功能优先

```bash
# 好的做法 - 从简单功能开始
/discovery "添加用户头像显示"

# 避免 - 一开始就追求复杂功能
/discovery "实现完整的用户管理系统"
```

### 2. 逐步增加复杂度

```
第 1 次: 简单 CRUD 功能
第 2 次: 添加认证
第 3 次: 添加权限控制
第 4 次: 添加审计日志
```

## 频繁验证

### 1. 每个小步骤后验证

```bash
# 实施一小步
/implement

# 立即验证
/verify

# 通过后继续
/implement
```

### 2. 不要等到最后

```
❌ 错误做法:
实现所有功能 → 验证 → 发现很多问题

✅ 正确做法:
实现功能1 → 验证 → 实现功能2 → 验证
```

## 及时沟通

### 1. 遇到问题及时沟通

```bash
# 使用诊断命令
/diagnose "构建失败，提示类型错误"
```

### 2. 不要假设

```
❌ 错误: "应该能通过测试"
✅ 正确: "测试全部通过 (34/34), 覆盖率 95%"
```

## 记录决策

### 1. 记录重要的架构决策

使用 `/design` 时，决策会自动记录在实施蓝图中。

### 2. 记录权衡的考虑

```markdown
## 方案选择

选择了方案 A 而非方案 B，因为：
- 性能要求更高
- 团队更熟悉技术栈
- 维护成本更低
```

## 持续改进

### 1. 每次交付后总结

```bash
# 交付后运行
/delivery

# 自动提取模式
# 生成 Instincts
```

### 2. 使用 Instincts 自动提取知识

```bash
# 查看学习状态
/instinct-status

# 演化为可复用技能
/evolve
```

## TDD 最佳实践

### 1. 严格遵循红-绿-重构

```bash
# RED: 先写失败的测试
# GREEN: 实现最小代码
# REFACTOR: 重构改进
```

### 2. 测试覆盖要求

| 测试类型 | 覆盖要求 |
|---------|---------|
| 快乐路径 | 100% |
| 边界条件 | ≥ 80% |
| 错误场景 | ≥ 80% |
| 语句覆盖率 | ≥ 80% |
| 分支覆盖率 | ≥ 80% |

## 代码质量标准

### 1. 函数设计

```typescript
// 好的函数设计
function calculateLiquidityScore(
  volume: number,
  spread: number,
  traders: number
): number {
  // 单一职责
  // 参数明确
  // 返回值明确
  // 纯函数
}
```

### 2. 命名规范

```typescript
// 文件命名: kebab-case
user-service.ts

// 变量/函数: camelCase
const userName = 'John';

// 类/接口: PascalCase
class UserService {}

// 常量: UPPER_SNAKE_CASE
const MAX_RETRIES = 3;
```

## Speckit 工作流最佳实践

### 1. 使用智能分支

```bash
# 创建规范命名的分支
/speckit-branch "实现用户登录功能"
# 输出: feature/001-login

# 三源检测: Issue/Git/Branch 自动关联
```

### 2. 质量门禁

```bash
# 提交前运行
/speckit-guard

# 确保通过所有质量检查
```

### 3. 一致性分析

```bash
# 定期运行
/speckit-analyze

# 检测需求重复、歧义、欠规格
```

## 错误处理最佳实践

### 1. 明确的错误处理

```typescript
// 好的错误处理
async function getUser(id: string): Promise<User> {
  const user = await db.findUser(id);

  if (!user) {
    throw new NotFoundError(`User not found: ${id}`);
  }

  return user;
}
```

### 2. 统一的错误类型

```typescript
class NotFoundError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'NotFoundError';
  }
}
```

## 安全最佳实践

### 1. 输入验证

```typescript
function validateInput(input: unknown): asserts input is ValidInput {
  if (!isValid(input)) {
    throw new ValidationError('Invalid input');
  }
}
```

### 2. 敏感数据处理

```typescript
// 好的做法
const apiKey = process.env.API_KEY;

// 避免
const apiKey = "hardcoded-key-123"; // ❌
```

## 性能最佳实践

### 1. 避免过度优化

```
先让代码工作，再优化性能
使用测量数据，不要猜测
```

### 2. 使用诊断工具

```bash
# 性能问题诊断
/diagnose --type performance "API 响应慢"
```

## 团队协作

### 1. 统一工作流

团队使用相同的命令和工作流：

```bash
# 统一使用 E2D 流程
/deliver "功能描述"

# 或 Speckit 工作流
/speckit-workflow "功能描述"
```

### 2. 代码审查

```bash
# 验证阶段包含代码审查
/verify

# 确保质量门禁通过
```

## 文档最佳实践

### 1. 保持文档更新

- 代码变更时同步更新文档
- 使用自动生成的文档（从命令定义）

### 2. 清晰的提交消息

```bash
git commit -m "feat: add user authentication

- Implement login functionality
- Add JWT token validation
- Handle error cases

Tests: 5/5 passing
Coverage: 95%"
```

## 学习路径

### 新手

1. 从简单功能开始
2. 使用 `/deliver` 完整流程
3. 学习 TDD 基础

### 中级

1. 分阶段使用命令
2. 学习 Speckit 工作流
3. 深入代码质量标准

### 高级

1. 自定义工作流
2. 扩展插件（添加技能）
3. 贡献最佳实践

## 常见陷阱

### 1. 跳过验证

```
❌ 实现 → 直接交付
✅ 实现 → 验证 → 交付
```

### 2. 忽略测试覆盖率

```
❌ 覆盖率 50% 就继续
✅ 覆盖率 ≥ 80% 才继续
```

### 3. 过度设计

```
❌ 实现当前不需要的功能
✅ YAGNI - You Aren't Gonna Need It
```

## 总结

- **质量比速度更重要**
- **慢下来，做对，一次完成**
- **TDD 是你的朋友**
- **持续学习，持续改进**
