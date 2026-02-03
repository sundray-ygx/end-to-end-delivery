---
description: 启动端到端价值交付闭环流程 - 从需求发现到价值交付的完整工作流（v3.0 整合诊断、学习、多语言支持）
argument-hint: 功能需求描述
---

# /deliver - 端到端价值交付命令 v3.0

启动完整的端到端价值交付闭环流程，整合需求发现、代码库探索、架构设计、实施执行、质量验证、价值交付的完整链路。

## v3.0 新特性

### 🎯 核心能力增强
- **diagnostic-pro 诊断系统** - 整合三大插件优势的调试、诊断、修复能力
- **continuous-learning-v2 Instinct 学习** - 自动提取和演化可复用知识

### 🌐 多语言支持
- **Python** - python-patterns, python-testing (pytest, factory_boy)
- **Go** - golang-patterns, golang-testing (table-driven tests, testify)
- **C/C++** - c-cpp-patterns, c-cpp-testing (Google Test, RAII, smart pointers)

### 📊 专业能力
- **eval-harness** - 需求阶段评估驱动开发（Capability/Regression Evals）
- **database-reviewer** - PostgreSQL 数据库专家（查询优化、索引设计）
- **iterative-retrieval** - 渐进式检索模式（解决子代理上下文问题）

## 自动化执行

**重要**: 此命令会自动调用 `end-to-end-workflow` 技能，无需手动调用。

### 模板自动回退

当项目没有配置本地模板时，插件会**自动使用内置的默认模板**：

```
模板查找顺序：
1. 项目根目录/.claude/templates/    (用户自定义)
2. 项目根目录/templates/            (项目模板)
3. 插件目录/templates/              (插件默认 - 自动回退) ✅
```

**无需任何配置**，直接使用即可：
```bash
/deliver "实现用户登录功能"
```

插件会自动使用默认的需求分析模板、设计模板、编码规范等。

## 使用方式

```bash
# 启动完整的端到端交付流程
/deliver "实现用户邮箱登录功能"

# 带更多上下文
/deliver """
实现用户登录功能，需求如下：
- 支持邮箱和密码登录
- 登录后返回 JWT token
- 记住登录状态 7 天
- 有登录失败次数限制
"""
```

## 工作流程

```
┌─────────────────────────────────────────────────────────────────┐
│                      端到端交付流程                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Discovery (需求发现)                                        │
│     ├─ 理解需求                                                │
│     ├─ 澄清问题                                                │
│     ├─ 定义验收标准                                            │
│     └─ 识别风险                                                │
│                                                                 │
│  2. Exploration (代码库探索)                                    │
│     ├─ 映射代码库结构                                          │
│     ├─ 识别现有模式                                            │
│     ├─ 分析相关功能                                            │
│     └─ 标注关键文件                                            │
│                                                                 │
│  3. Design (架构设计)                                          │
│     ├─ 生成多个方案                                            │
│     ├─ 权衡分析                                                │
│     ├─ 推荐方案                                                │
│     └─ 实施蓝图                                                │
│                                                                 │
│  4. Implementation (实施执行)                                  │
│     ├─ TDD 红绿重构                                            │
│     ├─ 两阶段审查                                              │
│     ├─ 自审与修复                                              │
│     └─ 频繁提交                                                │
│                                                                 │
│  5. Verification (质量验证)                                    │
│     ├─ 构建验证                                                │
│     ├─ 类型检查                                                │
│     ├─ 代码规范                                                │
│     ├─ 测试验证                                                │
│     └─ 安全扫描                                                │
│                                                                 │
│  6. Delivery (价值交付)                                        │
│     ├─ 交付文档                                                │
│     ├─ 价值验证                                                │
│     ├─ 模式提取                                                │
│     └─ 知识沉淀                                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 执行步骤

### Step 1: 初始化
```markdown
## 端到端交付初始化

正在启动端到端价值交付闭环流程...

**功能需求**: $ARGUMENTS

**工作流程配置**:
- 质量门禁: ✅ 启用
- 持续学习: ✅ 启用
- 自动验证: ✅ 启用

创建任务追踪...
```

### Step 2: Discovery Phase（v3.0 增强流程）
启动 `discovery-agent` 进行需求发现

**v2.0 新增步骤**:
1. 需求复杂度评估（功能、技术、规模、风险四个维度）
2. 根据复杂度自动选择开发模式（瀑布流/敏捷）
3. 基于模板维度进行深度需求分析

**v3.0 新增步骤**:
1. **eval-harness 评估驱动** - 在需求阶段定义评估标准（Capability Evals、Regression Evals）

**检查点**:
- [ ] 需求清晰明确
- [ ] 验收标准定义
- [ ] 约束条件识别
- [ ] 风险已评估
- [ ] 复杂度评估完成（v2.0）
- [ ] 维度分析完成（v2.0）
- [ ] 评估标准已定义（v3.0）

### Step 3: Exploration Phase（v3.0 增强流程）
启动 `exploration-agent` 进行代码库探索

**v3.0 新增步骤**:
1. **iterative-retrieval 渐进式检索** - DISPATCH → EVALUATE → REFINE → LOOP（最多 3 次循环）
2. 渐进式细化代码库理解，解决子代理上下文问题

**检查点**:
- [ ] 代码库结构已映射
- [ ] 现有模式已识别
- [ ] 关键文件已标注
- [ ] 技术债务已记录
- [ ] 渐进式检索完成（v3.0）

### Step 4: Design Phase（v3.0 增强流程）
启动 `design-agent` 进行架构设计

**v2.0 新增步骤**:
1. 根据需求复杂度选择设计分析框架（总体设计/模块详细设计/模块微型设计）
2. 基于模板维度进行深度架构设计分析

**v3.0 新增步骤**:
1. **database-reviewer 数据库专家** - PostgreSQL 查询优化、模式设计、索引策略、RLS 设计

**检查点**:
- [ ] 3 个方案已生成
- [ ] 权衡分析完成
- [ ] 推荐方案明确
- [ ] 实施蓝图详细
- [ ] 维度分析完成（v2.0）
- [ ] 数据库设计已审查（v3.0）

### Step 5: Implementation Phase（v3.0 增强流程）
启动 `implementation-agent` 进行实施执行

**v2.0 新增步骤**:
1. 自动检测项目编程语言
2. 加载对应的编码 checklist，提取审查维度
3. 基于checklist维度进行深度代码审查

**v3.0 新增步骤**:
1. **多语言支持** - Python/Go/C/C++ 全栈开发模式
2. 对应的编码规范和测试框架支持

**检查点**:
- [ ] TDD 流程遵循
- [ ] 测试覆盖率 ≥ 80%
- [ ] 代码审查通过
- [ ] 自审完成
- [ ] 编码规范检查完成（v2.0）
- [ ] 语言特定规范符合（v3.0）

### Step 6: Verification Phase（v3.0 增强流程）
启动 `verification-agent` 进行质量验证

**v2.0 新增步骤**:
1. 验证需求分析维度覆盖度
2. 验证设计分析维度覆盖度
3. 生成维度覆盖度验证报告

**v3.0 新增步骤**:
1. **diagnostic-pro 诊断触发** - 验证失败时自动调用诊断系统
2. 支持构建/运行时/性能/安全/数据库五类诊断

**检查点**:
- [ ] 构建成功
- [ ] 类型检查通过
- [ ] 代码规范通过
- [ ] 测试全部通过
- [ ] 安全扫描通过
- [ ] 维度覆盖度验证完成（v2.0）
- [ ] 诊断问题已解决（v3.0）

### Step 7: Delivery Phase（v3.0 增强流程）
启动 `delivery-agent` 进行价值交付

**v2.0 新增步骤**:
1. 基于各阶段维度分析成果生成交付总结
2. 生成端到端价值交付总结报告
3. 提取符合企业标准的价值模式

**v3.0 新增步骤**:
1. **continuous-learning-v2 Instinct 学习** - 自动提取可复用知识
2. Instincts → Skills/Commands/Agents 演化路径

**检查点**:
- [ ] 交付文档完整
- [ ] 价值已验证
- [ ] 模式已提取
- [ ] 知识已沉淀
- [ ] 维度覆盖度总结完成（v2.0）
- [ ] Instincts 已提取（v3.0）

## 输出物

完成端到端流程后，将产出:

### 1. 需求文档
- `docs/requirements/feature-name.md`
- 验收标准
- 用户故事

### 2. 设计文档
- `docs/design/feature-name.md`
- 架构设计
- 接口定义

### 3. 实现代码
- 源代码
- 测试代码
- 配置文件

### 4. 交付文档
- 变更日志
- 发布说明
- 技术文档
- PR 描述

### 5. 学习记录
- 新发现的模式
- 最佳实践
- 经验教训

## 质量门禁

每个阶段都有严格的质量门禁，必须通过才能进入下一阶段:

| 阶段 | 门禁标准 | 状态 |
|------|----------|------|
| Discovery | 需求明确, 验收标准清晰 | ⏳ 待验证 |
| Exploration | 代码库理解完整 | ⏳ 待验证 |
| Design | 架构方案明确 | ⏳ 待验证 |
| Implementation | 测试通过, 覆盖率达标 | ⏳ 待验证 |
| Verification | 所有验证通过 | ⏳ 待验证 |
| Delivery | 交付物完整 | ⏳ 待验证 |

## 分阶段执行

如果需要分阶段执行，可以使用阶段命令:

```bash
# 仅执行需求发现
/discovery "用户登录功能"

# 然后继续执行下一阶段
/exploration
/design
/implement
/verify
/delivery
```

## 中断与恢复

流程支持中断和恢复:

```bash
# 中断流程后，可以从任意阶段恢复
/design --resume

# 查看当前状态
/deliver --status
```

## 自定义配置

可以通过项目配置自定义流程:

```json
// .claude/end-to-end-delivery.json
{
  "qualityGates": {
    "testCoverage": 80,
    "maxFunctionLength": 50,
    "maxFileLength": 800
  },
  "phases": {
    "autoVerify": true,
    "parallelReview": true
  },
  "templates": {
    "path": "templates/custom-workflow"
  }
}
```

## 注意事项

1. **完整执行**: 建议首次使用时完整执行整个流程
2. **分阶段执行**: 熟练后可以分阶段执行，保持灵活性
3. **质量优先**: 任何时候质量都是第一优先级
4. **证据优先**: 所有结论都要有验证证据支持
5. **持续学习**: 每次交付都要提取模式和最佳实践

## 相关命令

### 主流程命令
- `/discovery` - 仅执行需求发现阶段
- `/exploration` - 仅执行代码库探索阶段
- `/design` - 仅执行架构设计阶段
- `/implement` - 仅执行实施执行阶段
- `/verify` - 仅执行质量验证阶段
- `/delivery` - 仅执行价值交付阶段

### v3.0 新增命令
- `/diagnose` - 诊断命令（支持 build/runtime/performance/security/database）
- `/instinct-export` - 导出 Instincts
- `/instinct-import` - 导入 Instincts
- `/instinct-status` - 查看 Instincts 状态
- `/evolve` - 演化 Instincts 为 Skills/Commands/Agents

## 相关代理

- `discovery-agent` - 需求发现代理
- `exploration-agent` - 代码库探索代理
- `design-agent` - 架构设计代理
- `implementation-agent` - 实施执行代理
- `verification-agent` - 质量验证代理
- `delivery-agent` - 交付管理代理

## 相关技能

- `end-to-end-workflow` - 端到端工作流主技能
- `requirement-analysis` - 需求分析技能
- `codebase-exploration` - 代码库探索技能
- `architecture-design` - 架构设计技能
- `implementation-execution` - 实施执行技能
- `quality-gates` - 质量门禁技能
- `verification-loop` - 验证循环技能
- `continuous-learning` - 持续学习技能

---

**核心原则**: Evidence Before Claims, Quality First, Continuous Learning
