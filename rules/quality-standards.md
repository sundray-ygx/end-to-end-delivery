# 质量标准 (Quality Standards)

端到端交付流程的质量标准规范。

## 代码质量标准

### 函数设计
```typescript
// 好的函数
function calculateLiquidityScore(
  volume: number,
  spread: number
): number {
  // 单一职责
  // 参数明确
  // 返回值明确
  // 纯函数
}
```

**标准**:
- 函数长度 ≤ 50 行
- 单一职责
- 参数 ≤ 5 个
- 纯函数优先
- 清晰的命名

### 文件组织
**标准**:
- 文件长度 ≤ 800 行
- 相关功能内聚
- 清晰的导出
- 合理的目录结构

### 命名规范
```typescript
// 文件: kebab-case
user-service.ts

// 变量/函数: camelCase
const userName = 'John';
function getUserById() {}

// 类/接口/类型: PascalCase
class UserService {}
interface UserProfile {}

// 常量: UPPER_SNAKE_CASE
const MAX_RETRIES = 3;
```

### 错误处理
```typescript
// 明确的错误处理
async function getUser(id: string): Promise<User> {
  const user = await db.findUser(id);

  if (!user) {
    throw new NotFoundError(`User not found: ${id}`);
  }

  return user;
}
```

**标准**:
- 所有错误路径已处理
- 错误类型明确
- 错误信息清晰
- 不泄露敏感信息

---

## 测试质量标准

### 覆盖率要求
```markdown
## 全局要求
- 语句覆盖率: ≥ 80%
- 分支覆盖率: ≥ 80%
- 函数覆盖率: ≥ 80%
- 行覆盖率: ≥ 80%

## 关键代码要求 (100%)
- 安全相关代码
- 财务计算代码
- 核心业务逻辑
- 认证授权代码
```

### 测试类型
```typescript
// 单元测试
describe('calculateLiquidityScore', () => {
  it('should return high score for liquid market', () => {
    // 测试
  });

  it('should handle edge case: zero volume', () => {
    // 边界条件
  });

  it('should throw error for invalid input', () => {
    // 错误场景
  });
});
```

**标准**:
- 快乐路径覆盖
- 边界条件覆盖
- 错误场景覆盖
- 测试独立无依赖

---

## 安全质量标准

### 输入验证
```typescript
// 所有输入已验证
function processInput(input: unknown): Result {
  if (!isValidInput(input)) {
    throw new ValidationError('Invalid input');
  }
  // 处理
}
```

### 敏感数据
```markdown
## 禁止
- 硬编码密钥
- 硬编码密码
- API Key 在代码中
- Token 泄露

## 要求
- 环境变量
- 密钥管理服务
- 加密存储
- 安全传输
```

### 错误处理
```markdown
## 安全的错误处理
- 不泄露系统信息
- 不泄露路径信息
- 不泄露内部结构
- 统一错误消息
```

---

## 文档质量标准

### 代码文档
```typescript
/**
 * 计算流动性评分
 *
 * @param market - 市场数据
 * @returns 评分 (0-100)
 * @throws {ValidationError} 数据无效时抛出
 *
 * @example
 * ```typescript
 * const score = calculateLiquidityScore(market);
 * ```
 */
function calculateLiquidityScore(market: MarketData): number {
  // 实现
}
```

**标准**:
- 所有公共 API 有文档
- 复杂逻辑有注释
- 参数和返回值清晰
- 有使用示例

### 项目文档
```markdown
## 必需文档
- README.md
- ARCHITECTURE.md
- API.md (如适用)
- CONTRIBUTING.md
- CHANGELOG.md
```

---

## 性能质量标准

### 响应时间
```markdown
## API 端点
- 简单查询: < 100ms
- 复杂查询: < 500ms
- 写操作: < 200ms

## 前端
- 首屏加载: < 2s
- 交互响应: < 100ms
- 路由切换: < 500ms
```

### 资源使用
```markdown
## 内存
- 常驻内存: < 100MB
- 峰值内存: < 500MB

## CPU
- 空闲: < 5%
- 正常: < 50%
- 峰值: < 80%
```

---

## 可维护性标准

### 代码复杂度
```markdown
## 圈复杂度
- 函数: ≤ 10
- 文件: ≤ 100

## 嵌套深度
- 最大: ≤ 4 层

## 重复代码
- 相似代码: < 5 行
- 重复次数: < 3 次
```

### 设计原则
```markdown
## SOLID
- Single Responsibility
- Open/Closed
- Liskov Substitution
- Interface Segregation
- Dependency Inversion

## DRY
- Don't Repeat Yourself
- 提取可复用代码
- 创建共享组件

## YAGNI
- You Aren't Gonna Need It
- 只实现需要的功能
- 避免过度设计
```

---

## 交付质量标准

### 交付物清单
```markdown
## 代码
- [ ] 源代码
- [ ] 测试代码
- [ ] 配置文件

## 文档
- [ ] 变更日志
- [ ] 发布说明
- [ ] 技术文档
- [ ] API 文档 (如适用)

## 测试
- [ ] 单元测试通过
- [ ] 集成测试通过
- [ ] E2E 测试通过
- [ ] 测试覆盖率达标

## 质量
- [ ] 代码规范通过
- [ ] 安全扫描通过
- [ ] 性能测试通过
```

### PR 质量
```markdown
## PR 描述
- [ ] 清晰的标题
- [ ] 详细的描述
- [ ] 变更类型标识
- [ ] 相关 Issue 链接
- [ ] 测试说明
- [ ] 截图/演示 (如适用)

## 检查清单
- [ ] 代码符合规范
- [ ] 自审完成
- [ ] 测试通过
- [ ] 文档更新
```

---

## 持续改进标准

### 每次交付后
```markdown
## 模式提取
- [ ] 新发现的代码模式
- [ ] 新发现的架构模式
- [ ] 新发现的测试模式

## 最佳实践
- [ ] 做得好的地方
- [ ] 经验教训
- [ ] 改进建议

## 知识沉淀
- [ ] 更新技能库
- [ ] 更新文档
- [ ] 更新模板
```

---

## 质量检查清单

### 代码提交前
- [ ] 代码符合规范
- [ ] 测试全部通过
- [ ] 覆盖率达标
- [ ] 自审完成

### PR 创建前
- [ ] 描述完整
- [ ] 文档更新
- [ ] 没有遗留问题

### 交付前
- [ ] 所有验证通过
- [ ] 交付物完整
- [ ] 价值已验证

---

**记住**: 质量是交付的生命线。遵守质量标准就是遵守对用户的承诺。
