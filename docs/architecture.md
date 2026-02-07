# 架构文档

## 目录结构

```
end-to-end-delivery/
├── .claude-plugin/           # 插件配置
│   ├── plugin.json          # 插件元数据
│   └── marketplace.json     # 市场配置
├── agents/                  # 代理定义
│   ├── discovery-agent.md   # 需求发现代理
│   ├── exploration-agent.md # 代码库探索代理
│   ├── design-agent.md      # 架构设计代理
│   ├── implementation-agent.md # 实施执行代理
│   ├── verification-agent.md # 质量验证代理
│   ├── delivery-agent.md    # 交付管理代理
│   ├── diagnostic-agent.md  # 诊断专家代理
│   ├── observer-agent.md    # 持续学习观察者
│   └── database-reviewer.md # 数据库专家代理
├── skills/                  # 技能定义
│   ├── ui-design/           # UI/UX设计能力闭环
│   ├── speckit-workflow/    # Speckit 规范化开发工作流
│   ├── speckit-branch/      # 智能分支管理
│   ├── speckit-guard/       # 宪法治理检查
│   ├── speckit-tasks/       # 任务依赖管理
│   ├── speckit-analyze/     # 一致性分析
│   ├── speckit-checklist/   # 质量检查清单
│   ├── end-to-end-workflow/ # 端到端工作流主技能
│   ├── template-adapter/    # 模板适配器技能
│   ├── diagnostic-pro/      # 诊断专家技能
│   ├── continuous-learning-v2/ # Instinct 学习
│   ├── eval-harness/        # 评估驱动开发
│   ├── python-patterns/     # Python 模式
│   ├── python-testing/      # Python 测试
│   ├── golang-patterns/     # Go 模式
│   ├── golang-testing/      # Go 测试
│   ├── c-cpp-patterns/      # C/C++ 模式
│   └── c-cpp-testing/       # C/C++ 测试
├── commands/                # 命令定义
│   ├── core/                # 核心命令 (3个)
│   │   ├── deliver.md
│   │   ├── discovery.md
│   │   └── design.md
│   ├── workflow/            # 工作流命令 (3个)
│   │   ├── speckit-workflow.md
│   │   ├── speckit-analyze.md
│   │   └── speckit-tasks.md
│   └── utility/             # 工具命令 (13个)
│       ├── exploration.md
│       ├── implement.md
│       ├── verify.md
│       ├── delivery.md
│       ├── speckit-branch.md
│       ├── speckit-guard.md
│       ├── speckit-checklist.md
│       ├── ui-design.md
│       ├── diagnose.md
│       ├── instinct-export.md
│       ├── instinct-import.md
│       ├── instinct-status.md
│       └── evolve.md
├── utils/                   # 工具模块
│   ├── complexity-evaluator.md
│   ├── template-loader.md
│   ├── language-detector.md
│   └── template-adapter.md
├── templates/               # 模板文件
│   ├── requirements/        # 需求模板
│   ├── design/              # 设计模板
│   ├── coding/              # 编码 checklist
│   ├── testing/             # 测试 checklist
│   └── documentation/       # 文档模板
├── docs/                    # 文档目录
│   ├── design/              # 设计文档
│   ├── prompt/              # Agent Prompts
│   ├── commands/            # 命令参考
│   └── guides/              # 使用指南
├── CHANGELOG.md             # 变更日志
└── README.md               # 主文档
```

## 架构层次

```
┌─────────────────────────────────────────────┐
│           Claude Code Interface             │
├─────────────────────────────────────────────┤
│              Commands Layer                 │
│  (Core/Workflow/Utility - 19 commands)      │
├─────────────────────────────────────────────┤
│              Agents Layer                   │
│  (9 Agents: Discovery/Delivery/etc.)        │
├─────────────────────────────────────────────┤
│              Skills Layer                   │
│  (17 Skills: UI-Design/Speckit/etc.)        │
├─────────────────────────────────────────────┤
│          Utils & Templates Layer            │
│  (Language Detector, Template Adapter)      │
├─────────────────────────────────────────────┤
│              Rules Layer                    │
│  (TDD, Quality Gates, Evidence First)       │
└─────────────────────────────────────────────┘
```

## 工作流架构

```
Discovery → Exploration → Design → Implementation → Verification → Delivery
    ↓           ↓            ↓         ↓            ↓          ↓
 需求发现   代码库探索    架构设计    实施执行     质量验证    价值交付
    ↓           ↓            ↓         ↓            ↓          ↓
 澄清问题    映射架构    多方案对比   TDD执行     全面验证    模式提取
 定义标准    识别模式    权衡分析    两阶段审查   质量门禁    知识沉淀
    ↓           ↓            ↓         ↓            ↓          ↓
  eval-harness                                       continuous-learning-v2
  (评估驱动)                                        (Instinct学习)
```

## Speckit 工作流

```
Specify → Plan → Tasks → Analyze → Implement
   ↓        ↓       ↓        ↓         ↓
智能分支  宪法检查  任务分解   一致性    TDD执行
```

## 数据流

```
用户输入
  ↓
Command (路由)
  ↓
Agent (执行)
  ↓
Skills (辅助)
  ↓
Utils/Templates (支持)
  ↓
输出结果
```

## 扩展性设计

### 添加新命令

1. 在 `commands/` 对应分类目录创建 `.md` 文件
2. Claude Code 自动发现并注册命令

### 添加新技能

1. 在 `skills/` 创建新目录
2. 创建 `SKILL.md` 定义技能
3. 在 `plugin.json` 添加权限配置

### 添加新代理

1. 在 `agents/` 创建 `.md` 文件
2. 在 `plugin.json` 的 `agents` 数组添加引用

## 配置管理

### plugin.json

```json
{
  "name": "end-to-end-delivery",
  "version": "3.1.0",
  "commands": "./commands",
  "skills": "./skills",
  "agents": ["./agents/*.md"]
}
```

### settings.local.json

```json
{
  "permissions": {
    "allow": [
      "Skill(end-to-end-delivery:*)"
    ]
  }
}
```

## 性能考虑

- 命令加载: 递归搜索 `commands/` 目录
- 技能加载: 按需加载，仅在需要时加载
- 模板加载: 缓存机制，避免重复加载

## 安全考虑

- 权限控制: 通过 `settings.local.json` 管理
- 敏感数据: Instincts 本地存储
- 代码执行: TDD 保护，先测试后执行

## 可维护性

- 清晰的目录结构
- 模块化设计
- 完整的文档
- 版本控制友好
