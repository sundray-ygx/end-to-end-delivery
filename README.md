# 端到端价值交付闭环插件 (End-to-End Delivery)

整合 superpowers、everything-claude-code、feature-dev 三大插件精华，形成的完整端到端价值交付闭环开发流程。

## 最新特性 v3.0

### 🎉 新增核心能力

#### diagnostic-pro（诊断专家）
整合三大插件优势的调试、诊断、修复系统，提供系统化的诊断能力：

- **系统化调试技术**: 科学方法、二分调试、Rubber Duck 调试法
- **构建错误修复**: 增量式修复、最小化改动原则
- **错误处理模式**: 异常层次结构、Result 类型、重试与熔断
- **安全诊断**: SQL 注入、XSS、密钥泄露检测
- **数据库诊断**: 查询性能分析、死锁检测、索引优化

**命令**: `/diagnose`

#### continuous-learning-v2（Instinct 学习）
自动提取和演化可复用知识的学习系统：

- **Observer Agent**: 通过 hooks 捕获会话数据
- **Instincts**: 原子行为，带置信度评分（0.3-0.9）
- **Evolution**: Instincts → Skills/Commands/Agents
- **导入/导出**: 支持 Instincts 的分享和备份

**命令**: `/instinct-export`, `/instinct-import`, `/instinct-status`, `/evolve`

#### 多语言支持（Python/Go/C/C++）
完整的全栈开发模式支持：

- **Python**: python-patterns、python-testing、Django 支持
- **Go**: golang-patterns、golang-testing、table-driven tests
- **C/C++**: c-cpp-patterns（现代 C++）、c-cpp-testing（Google Test/Catch2）

#### eval-harness（评估驱动开发）
在需求阶段定义评估标准：

- **Capability Evals**: 功能评估
- **Regression Evals**: 回归评估
- **pass@k 指标**: 可靠性测量

#### database-reviewer（数据库专家）
PostgreSQL 数据库架构审查：

- 查询性能优化
- 模式设计
- 索引策略
- RLS 设计

#### iterative-retrieval（渐进式检索）
解决子代理上下文问题：

- DISPATCH → EVALUATE → REFINE → LOOP
- 最多 3 次循环
- 渐进式细化代码库理解

## v2.0 特性（保留）

### 🎉 本地模板融合

支持与企业本地模板深度融合，利用模板提供的分析维度和框架，增强AI分析的深度和完整性：

- **智能复杂度评估** - 自动评估需求复杂度，选择瀑布流或敏捷模式
- **模板维度参考** - 本地模板提供分析框架和维度（如 INVEST 原则、架构设计方法）
- **深度分析增强** - AI基于模板维度进行深度分析，而非简单填充模板
- **编码规范检查** - 自动检测编程语言，加载对应的编码 checklist 进行审查

## 概述

本插件提供了一个完整的、可执行的、端到端的开发流程，从需求发现到价值交付，形成完整的闭环。

### 核心特点

- **端到端闭环**: 从需求到交付的完整流程
- **质量优先**: 严格的质量门禁和验证
- **证据优先**: 所有结论基于验证证据
- **持续学习**: 每次交付都提取模式和最佳实践
- **模板融合**: 支持本地开发流程模板融合（v2.0 新增）
- **诊断系统**: 整合的调试、诊断、修复能力（v3.0 新增）
- **多语言支持**: Python/Go/C/C++ 全栈开发（v3.0 新增）

### 核心原则

1. **Evidence Before Claims** - 证据优先于断言
2. **Quality First** - 质量第一
3. **Continuous Learning** - 持续学习

## 工作流架构

```
Discovery → Exploration → Design → Implementation → Verification → Delivery
    ↓           ↓            ↓         ↓            ↓          ↓
 需求发现   代码库探索    架构设计    实施执行     质量验证    价值交付
    ↓           ↓            ↓         ↓            ↓          ↓
 澄清问题    映射架构    多方案对比   TDD执行     全面验证    模式提取
 定义标准    识别模式    权衡分析    两阶段审查   质量门禁    知识沉淀
    ↓                                                       ↓
  eval-harness                                       continuous-learning-v2
  (评估驱动)                                        (Instinct学习)
```

## 新增命令（v3.0）

```bash
# 诊断命令
/diagnose "错误描述"
/diagnose --type build "构建失败"
/diagnose --type runtime "运行时异常"
/diagnose --type performance "性能问题"
/diagnose --type security "安全问题"
/diagnose --type database "数据库问题"

# Instinct 管理命令
/instinct-export
/instinct-import <file>
/instinct-status
/evolve                    # 演化 Instincts 为 Skills/Commands/Agents
```

## 原有命令（保留）

```bash
# 启动完整的端到端交付流程
/deliver "实现用户登录功能"

# 或分阶段执行
/discovery "实现用户登录功能"
/exploration
/design
/implement
/verify
/delivery
```

## 目录结构（v3.0 更新）

```
end-to-end-delivery/
├── .claude-plugin/           # 插件配置
│   ├── plugin.json          # 插件元数据（v3.0 更新）
│   └── marketplace.json     # 市场配置
├── agents/                  # 代理定义
│   ├── discovery-agent.md   # 需求发现代理（+eval-harness）
│   ├── exploration-agent.md # 代码库探索代理（+iterative-retrieval）
│   ├── design-agent.md      # 架构设计代理（+database-reviewer）
│   ├── implementation-agent.md # 实施执行代理（多语言支持）
│   ├── verification-agent.md # 质量验证代理（+诊断触发）
│   ├── delivery-agent.md    # 交付管理代理（+continuous-learning-v2）
│   ├── diagnostic-agent.md  # [新增] 诊断专家代理
│   ├── observer-agent.md    # [新增] 持续学习观察者
│   └── database-reviewer.md # [新增] 数据库专家代理
├── skills/                  # 技能定义
│   ├── end-to-end-workflow/ # 端到端工作流主技能（v3.0 更新）
│   ├── template-adapter/    # 模板适配器技能
│   ├── diagnostic-pro/      # [新增] 诊断专家技能
│   │   └── modules/
│   │       ├── debugging-strategies.md
│   │       ├── build-fix.md
│   │       ├── error-handling.md
│   │       ├── security-diagnosis.md
│   │       └── database-diagnosis.md
│   ├── continuous-learning-v2/ # [新增] Instinct 学习
│   │   ├── agents/observer.md
│   │   ├── config.json
│   │   ├── scripts/instinct-cli.py
│   │   └── hooks/observe.sh
│   ├── eval-harness/        # [新增] 评估驱动开发
│   ├── python-patterns/     # [新增] Python 模式
│   ├── python-testing/      # [新增] Python 测试
│   ├── golang-patterns/     # [新增] Go 模式
│   ├── golang-testing/      # [新增] Go 测试
│   ├── c-cpp-patterns/      # [新增] C/C++ 模式
│   └── c-cpp-testing/       # [新增] C/C++ 测试
├── commands/                # 命令定义
│   ├── deliver.md           # /deliver 命令（完整流程）
│   ├── discovery.md         # /discovery 命令（需求发现阶段）
│   ├── exploration.md       # /exploration 命令（代码库探索阶段）
│   ├── design.md            # /design 命令（架构设计阶段）
│   ├── implement.md         # /implement 命令（实施执行阶段）
│   ├── verify.md            # /verify 命令（质量验证阶段）
│   ├── delivery.md          # /delivery 命令（价值交付阶段）
│   ├── diagnose/            # [新增] /diagnose 命令
│   ├── instinct-export/     # [新增] /instinct-export 命令
│   ├── instinct-import/     # [新增] /instinct-import 命令
│   ├── instinct-status/     # [新增] /instinct-status 命令
│   └── evolve/              # [新增] /evolve 命令
├── utils/                   # 工具模块
│   ├── complexity-evaluator.md # 复杂度评估工具
│   ├── template-loader.md      # 模板加载工具
│   ├── language-detector.md    # 语言检测工具
│   └── template-adapter.md      # 模板适配器
├── templates/               # 模板文件
│   ├── requirements/        # 需求模板（瀑布流/敏捷）
│   ├── design/              # 设计模板
│   ├── coding/              # 编码 checklist（多语言）
│   ├── testing/             # 测试 checklist（多语言）
│   └── documentation/       # 文档模板
├── CHANGELOG.md             # [新增] 变更日志
└── README.md               # 本文件
```

## 快速开始

### 1. 安装插件

插件通过本地插件方式安装，实际运行位置：
- **安装位置**: `~/.claude/plugins/cache/local-plugins/end-to-end-delivery/`
- **源位置**: `~/.claude/plugins/marketplaces/end-to-end-delivery/`

```bash
# 从市场复制到本地（如需要）
cp -r ~/.claude/plugins/marketplaces/end-to-end-delivery ~/.claude/plugins/
```

### 2. 使用主要命令

```bash
# 启动完整的端到端交付流程
/deliver "实现用户登录功能"

# 使用诊断命令（v3.0 新增）
/diagnose "构建失败，提示类型错误"

# 管理 Instincts（v3.0 新增）
/instinct-status
/evolve

# 或分阶段执行
/discovery "实现用户登录功能"
/exploration
/design
/implement
/verify
/delivery
```

## 质量标准

### 代码质量
- 函数长度 ≤ 50 行
- 文件长度 ≤ 800 行
- 嵌套深度 ≤ 4 层
- 命名清晰有意义

### 测试质量
- **测试覆盖率 ≥ 80%**（语句、分支、函数）
- 快乐路径覆盖完整
- 边界条件覆盖充分
- 错误场景覆盖全面

### 安全质量
- 无硬编码密钥
- 输入验证完整
- 错误处理安全

## 证据优先原则

**铁律**: NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE

```markdown
❌ 错误: "应该能通过测试"
✅ 正确: "测试全部通过 (34/34), 覆盖率 95%"

❌ 错误: "看起来构建成功了"
✅ 正确: "构建成功 (exit 0), 输出: dist/"
```

## 配置

### 权限配置（v3.0 更新）

在 `.claude/settings.local.json` 中添加新技能的权限：

```json
{
  "permissions": {
    "allow": [
      "Skill(end-to-end-delivery:diagnostic-pro)",
      "Skill(end-to-end-delivery:continuous-learning-v2)",
      "Skill(end-to-end-delivery:eval-harness)",
      "Skill(end-to-end-delivery:python-patterns)",
      "Skill(end-to-end-delivery:python-testing)",
      "Skill(end-to-end-delivery:golang-patterns)",
      "Skill(end-to-end-delivery:golang-testing)",
      "Skill(end-to-end-delivery:c-cpp-patterns)",
      "Skill(end-to-end-delivery:c-cpp-testing)"
    ]
  }
}
```

## 最佳实践

### 1. 从小开始
- 先在简单功能上实践
- 逐步增加复杂度

### 2. 频繁验证
- 每个小步骤后验证
- 不要等到最后

### 3. 及时沟通
- 遇到问题及时沟通
- 不要假设

### 4. 记录决策
- 记录重要的架构决策
- 记录权衡的考虑

### 5. 持续改进（v3.0 增强）
- 每次交付后总结
- 使用 Instincts 自动提取知识
- 使用 evolve 演化为可复用技能

## 与其他插件的关系

本插件整合了以下插件的精华:

### Superpowers
- Subagent-Driven Development
- Writing Plans
- Verification Before Completion

### Everything Claude Code
- Verification Loop
- TDD Workflow
- Continuous Learning v2
- Python/Go/C/C++ Skills
- Database Reviewer
- Iterative Retrieval

### Feature Dev
- Codebase Exploration
- Architecture Design
- Quality Review

### Developer Essentials
- Debugging Strategies
- Error Handling Patterns

## 变更日志

查看 [CHANGELOG.md](CHANGELOG.md) 了解详细版本更新记录。

## 贡献

欢迎贡献改进!

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

MIT License

## 致谢

感谢以下项目的启发:
- [superpowers](https://github.com/obra/superpowers)
- [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
- [claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

---

**核心原则**: Evidence Before Claims, Quality First, Continuous Learning

**记住**: 端到端价值交付闭环不是一次性的活动，而是一个持续改进的循环。每一次交付都是学习的机会，每一次学习都让下一次交付更好。
