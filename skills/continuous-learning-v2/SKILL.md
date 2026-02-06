---
name: continuous-learning-v2
description: 基于 Instinct 的学习系统，通过 hooks 观察会话、创建带置信度评分的原子本能，并将其演化为 skills/commands/agents。
version: 2.0.0
---

# 持续学习 v2 - 基于 Instinct 的架构

一个高级学习系统，通过原子化的"instincts"（小型学习行为）将您的 Claude Code 会话转化为可复用的知识。

## v2 新特性

| 特性 | v1 | v2 |
|---------|----|----|
| 观察 | Stop hook (会话结束) | PreToolUse/PostToolUse (100% 可靠) |
| 分析 | 主上下文 | 后台代理 (Haiku) |
| 粒度 | 完整技能 | 原子化 "instincts" |
| 置信度 | 无 | 0.3-0.9 加权 |
| 演化 | 直接到技能 | Instincts → 聚类 → skill/command/agent |
| 共享 | 无 | 导出/导入 instincts |

## Instinct 模型

一个 instinct 是一个小的学习行为：

```yaml
---
id: prefer-functional-style
trigger: "当编写新函数时"
confidence: 0.7
domain: "code-style"
source: "session-observation"
---

# 优先使用函数式风格

## 行动
适当时使用函数式模式而非类。

## 证据
- 观察到 5 次函数式模式偏好实例
- 用户在 2025-01-15 将基于类的方法纠正为函数式
```

**属性：**
- **原子化** — 一个触发器，一个行动
- **置信度加权** — 0.3 = 尝试性，0.9 = 接近确定
- **域标签** — code-style、testing、git、debugging、workflow 等
- **证据支持** — 跟踪创建它的观察记录

## 工作原理

```
会话活动
      │
      │ Hooks 捕获提示词 + 工具使用 (100% 可靠)
      ▼
┌─────────────────────────────────────────┐
│         observations.jsonl              │
│   (提示词、工具调用、结果)               │
└─────────────────────────────────────────┘
      │
      │ Observer agent 读取 (后台，Haiku)
      ▼
┌─────────────────────────────────────────┐
│          模式检测                       │
│   • 用户纠正 → instinct                 │
│   • 错误解决 → instinct                 │
│   • 重复工作流 → instinct               │
└─────────────────────────────────────────┘
      │
      │ 创建/更新
      ▼
┌─────────────────────────────────────────┐
│         instincts/personal/             │
│   • prefer-functional.md (0.7)          │
│   • always-test-first.md (0.9)          │
│   • use-zod-validation.md (0.6)         │
└─────────────────────────────────────────┘
      │
      │ /evolve 聚类
      ▼
┌─────────────────────────────────────────┐
│              evolved/                   │
│   • commands/new-feature.md             │
│   • skills/testing-workflow.md          │
│   • agents/refactor-specialist.md       │
└─────────────────────────────────────────┘
```

## 快速开始

### 1. 启用观察 Hooks

添加到您的 `~/.claude/settings.json`。

**如果作为插件安装**（推荐）：

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "${CLAUDE_PLUGIN_ROOT}/skills/continuous-learning-v2/hooks/observe.sh pre"
      }]
    }],
    "PostToolUse": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "${CLAUDE_PLUGIN_ROOT}/skills/continuous-learning-v2/hooks/observe.sh post"
      }]
    }]
  }
}
```

**如果手动安装**到 `~/.claude/skills`：

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/skills/continuous-learning-v2/hooks/observe.sh pre"
      }]
    }],
    "PostToolUse": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/skills/continuous-learning-v2/hooks/observe.sh post"
      }]
    }]
  }
}
```

### 2. 初始化目录结构

Python CLI 会自动创建这些，您也可以手动创建：

```bash
mkdir -p ~/.claude/homunculus/{instincts/{personal,inherited},evolved/{agents,skills,commands}}
touch ~/.claude/homunculus/observations.jsonl
```

### 3. 使用 Instinct 命令

```bash
/instinct-status     # 显示学习的 instincts 及置信度评分
/evolve              # 将相关 instincts 聚类为 skills/commands
/instinct-export     # 导出 instincts 以供分享
/instinct-import     # 从他人导入 instincts
```

## 命令

| 命令 | 描述 |
|---------|-------------|
| `/instinct-status` | 显示所有学习的 instincts 及置信度 |
| `/evolve` | 将相关 instincts 聚类为 skills/commands |
| `/instinct-export` | 导出 instincts 以供分享 |
| `/instinct-import <file>` | 从他人导入 instincts |

## 配置

编辑 `config.json`：

```json
{
  "version": "2.0",
  "observation": {
    "enabled": true,
    "store_path": "~/.claude/homunculus/observations.jsonl",
    "max_file_size_mb": 10,
    "archive_after_days": 7
  },
  "instincts": {
    "personal_path": "~/.claude/homunculus/instincts/personal/",
    "inherited_path": "~/.claude/homunculus/instincts/inherited/",
    "min_confidence": 0.3,
    "auto_approve_threshold": 0.7,
    "confidence_decay_rate": 0.05
  },
  "observer": {
    "enabled": true,
    "model": "haiku",
    "run_interval_minutes": 5,
    "patterns_to_detect": [
      "user_corrections",
      "error_resolutions",
      "repeated_workflows",
      "tool_preferences"
    ]
  },
  "evolution": {
    "cluster_threshold": 3,
    "evolved_path": "~/.claude/homunculus/evolved/"
  }
}
```

## 文件结构

```
~/.claude/homunculus/
├── identity.json           # 您的档案、技术水平
├── observations.jsonl      # 当前会话观察
├── observations.archive/   # 已处理的观察
├── instincts/
│   ├── personal/           # 自动学习的 instincts
│   └── inherited/          # 从他人导入
└── evolved/
    ├── agents/             # 生成的专家代理
    ├── skills/             # 生成的技能
    └── commands/           # 生成的命令
```

## 与 Skill Creator 集成

当您使用 [Skill Creator GitHub App](https://skill-creator.app) 时，它现在会生成**两者**：
- 传统的 SKILL.md 文件（向后兼容）
- Instinct 集合（用于 v2 学习系统）

从仓库分析生成的 instincts 带有 `source: "repo-analysis"` 标签，并包含源仓库 URL。

## 置信度评分

置信度随时间演变：

| 分数 | 含义 | 行为 |
|-------|---------|----------|
| 0.3 | 尝试性 | 建议但不强制 |
| 0.5 | 中等 | 相关时应用 |
| 0.7 | 强 | 自动批准应用 |
| 0.9 | 接近确定 | 核心行为 |

**置信度增加**当：
- 模式被反复观察
- 用户不纠正建议的行为
- 来自其他来源的类似 instincts 一致

**置信度减少**当：
- 用户明确纠正该行为
- 长时间未观察到该模式
- 出现矛盾的证据

## 为什么使用 Hooks 而非 Skills 进行观察？

> "v1 依赖 skills 来观察。Skills 是概率性的——它们根据 Claude 的判断触发约 50-80% 的时间。"

Hooks **100% 时间**确定性地触发。这意味着：
- 每次工具调用都被观察
- 不会遗漏模式
- 学习是全面的

## 向后兼容性

v2 完全兼容 v1：
- 现有的 `~/.claude/skills/learned/` skills 仍然有效
- Stop hook 仍然运行（但现在也输入到 v2）
- 渐进迁移路径：并行运行两者

## 隐私

- 观察保留在您的机器上**本地**
- 只有 **instincts**（模式）可以导出
- 不分享实际代码或对话内容
- 您控制导出的内容

## 相关资源

- [Skill Creator](https://skill-creator.app) - 从仓库历史生成 instincts
- [Homunculus](https://github.com/humanplane/homunculus) - v2 架构的灵感来源
- [长格式指南](https://x.com/affaanmustafa/status/2014040193557471352) - 持续学习部分

---

*基于本能的学习：一次一个观察，教 Claude 您的模式。*
