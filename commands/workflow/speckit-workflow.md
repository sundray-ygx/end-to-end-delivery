---
description: Speckit 规范化功能开发工作流 - 整合规格生成、技术计划、任务分解、一致性分析、实施执行的完整流程
argument-hint: 功能需求描述
---

# /speckit-workflow - Speckit 规范化开发工作流

执行完整的 Speckit 规范化功能开发工作流：**specify → plan → tasks → analyze → implement**

## 核心原则

- **Specification First** - 规格优先，清晰的需求定义
- **Constitution Driven** - 宪法驱动，质量门禁控制
- **Consistency Verified** - 一致性验证，六重分析检测
- **Task Dependency Managed** - 依赖管理，并行执行优化

## 使用方式

```bash
# 完整工作流执行
/speckit-workflow "实现用户邮箱登录功能"

# 带上下文执行
/speckit-workflow """
实现用户登录功能，需求如下：
- 支持邮箱和密码登录
- 登录后返回 JWT token
- 记住登录状态 7 天
- 有登录失败次数限制
"""
```

## 工作流阶段

```
1. Specify   (规格生成)  → 智能分支管理、需求规格化
2. Plan      (技术计划)  → 宪法检查、技术决策
3. Tasks     (任务分解)  → 依赖管理、用户故事分组
4. Analyze   (一致性分析) → 六重检测、严重程度分级
5. Implement (实施执行)  → TDD 执行、检查清单验证
```

## 输出目录结构

```
specs/
└── {NUMBER}-{SHORT-NAME}/
    ├── spec.md              # 功能规格
    ├── plan.md              # 实施计划
    ├── tasks.md             # 任务列表
    ├── research.md          # 技术研究
    ├── data-model.md        # 数据模型
    ├── quickstart.md        # 快速开始
    ├── contracts/           # API 契约
    └── checklists/          # 质量检查清单
```

## 独立命令

工作流内部调用以下独立命令，也可单独使用：

| 命令 | 功能 |
|------|------|
| `/speckit-branch` | 智能分支管理 |
| `/speckit-guard` | 宪法治理检查 |
| `/speckit-tasks` | 任务依赖管理 |
| `/speckit-analyze` | 一致性分析 |
| `/speckit-checklist` | 质量检查清单 |

## 相关技能

```text
/skill speckit-workflow "功能描述"
```

通过技能调用可以获得更详细的交互和配置选项。
