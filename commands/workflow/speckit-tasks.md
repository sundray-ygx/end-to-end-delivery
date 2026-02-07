---
description: Speckit 任务依赖管理 - [P]并行标记、用户故事分组、依赖关系可视化
argument-hint: (可选) --from-plan
---

# /speckit-tasks - 任务依赖管理

将设计文档转化为可执行的任务列表，通过用户故事组织和并行执行标记优化开发效率。

## 任务格式

```markdown
- [ ] T001 [P] [US1] Description with file path
```

| 组件 | 说明 |
|------|------|
| `- [ ]` | Markdown 复选框 |
| `T001` | 任务 ID，顺序编号 |
| `[P]` | 并行执行标记（可选） |
| `[US1]` | 用户故事标签 |
| `Description` | 任务描述（含文件路径） |

## 使用方式

```bash
# 基本用法
/speckit-tasks

# 基于设计生成
/speckit-tasks --from-plan
```

## 任务组织

```
Phase 1: Setup          → 项目初始化
Phase 2: Foundational   → 阻塞性前置条件 ⚠️
Phase 3+: User Stories  → 按优先级 (P1, P2, P3...)
Phase N: Polish         → 跨功能改进
```

## 并行执行

- **[P] 标记**: 可与其他 [P] 任务并行执行
- **无标记**: 必须串行执行
- **用户故事**: 不同用户故事可并行开发

## MVP 优先

```markdown
User Story 1 (P1) 🎯 MVP ← 第一个用户故事，MVP 候选
User Story 2 (P2)
User Story 3 (P3)
```

## 输出

```markdown
# Tasks: [FEATURE NAME]

## Phase 1: Setup
- [ ] T001 Create project structure
- [ ] T002 [P] Configure linting

## Phase 2: Foundational
- [ ] T003 Setup database schema ⚠️

## Phase 3: User Story 1 (P1) 🎯 MVP
- [ ] T004 [P] [US1] Create User model
- [ ] T005 [US1] Implement AuthService
```

## 相关技能

```text
/skill speckit-tasks
```
