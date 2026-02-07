---
name: speckit-tasks
description: Speckit 任务依赖管理 - [P]并行标记、用户故事分组、依赖关系可视化
---

# Speckit 任务依赖管理

## 概述

本技能实现 Speckit 框架的任务依赖管理功能，将设计文档转化为可执行的任务列表，通过用户故事组织和并行执行标记优化开发效率。

**核心功能**:
- **用户故事驱动** - 按用户故事组织任务，支持独立测试
- **依赖管理** - 清晰的依赖关系和并行执行标记 [P]
- **标准化格式** - `- [ ] T001 [P] [US1] Description` 格式
- **质量控制** - 任务完整性验证和 MVP 范围建议

## 使用方式

### 基本用法

```text
/skill speckit-tasks
```

### 基于设计生成任务

```text
/skill speckit-tasks --from-plan
```

### 在工作流中调用

```text
/skill speckit-workflow "实现用户登录"
→ Specify 完成
→ Plan 完成
→ Analyze 完成
→ 调用 speckit-tasks 生成任务列表
```

## 任务格式

### 标准格式

```markdown
- [ ] T001 [P] [US1] Description with file path
```

### 格式组件

| 组件 | 说明 | 示例 |
|------|------|------|
| `- [ ]` | Markdown 复选框 | `- [ ]` 未完成, `- [x]` 已完成 |
| `T001` | 任务 ID，顺序编号 | T001, T002, T003... |
| `[P]` | 并行执行标记（可选） | 表示可与其他 [P] 任务并行 |
| `[US1]` | 用户故事标签 | US1, US2, US3... |
| `Description` | 任务描述（含文件路径） | "Create User model in src/models/user.py" |

### 示例

```markdown
## Phase 1: Setup
- [ ] T001 Create project structure per implementation plan
- [ ] T002 [P] Configure linting and formatting tools
- [ ] T003 Initialize dependencies

## Phase 2: Foundational
- [ ] T004 Setup database schema and migrations framework
- [ ] T005 [P] Implement authentication framework
- [ ] T006 [P] Setup API routing and middleware structure

## Phase 3: User Story 1 - Email Login (P1) 🎯 MVP
- [ ] T007 [P] [US1] Create User model in src/models/user.py
- [ ] T008 [P] [US1] Create Session model in src/models/session.py
- [ ] T009 [US1] Implement AuthService in src/services/auth.py (depends on T007, T008)
- [ ] T010 [US1] Implement login endpoint in src/api/login.py
```

## 任务组织结构

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           任务组织结构                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Phase 1: Setup (项目初始化)                                                │
│  └─ 共享基础设施，可并行执行                                                  │
│                                                                             │
│  Phase 2: Foundational (阻塞性前置条件)                                      │
│  └─ ⚠️ CRITICAL: 所有用户故事的阻塞依赖，必须先完成                           │
│                                                                             │
│  Phase 3+: User Stories (按优先级)                                          │
│  ├─ User Story 1 (P1) 🎯 MVP ← 第一个用户故事，MVP 候选                      │
│  │   ├─ Tests (OPTIONAL)                                                      │
│  │   └─ Implementation                                                       │
│  ├─ User Story 2 (P2)                                                        │
│  │   ├─ Tests (OPTIONAL)                                                      │
│  │   └─ Implementation                                                       │
│  └─ User Story 3 (P3)                                                        │
│      ├─ Tests (OPTIONAL)                                                      │
│      └─ Implementation                                                       │
│                                                                             │
│  Phase N: Polish (跨功能改进)                                                │
│  └─ 文档、重构、优化、安全加固                                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 阶段详解

### Phase 1: Setup (项目初始化)

**目的**: 项目基础结构和配置

**示例任务**:
```markdown
- [ ] T001 Create project structure per implementation plan
- [ ] T002 [P] Configure linting and formatting tools
- [ ] T003 [P] Initialize language-specific dependencies
- [ ] T004 [P] Setup environment configuration
```

**特点**: 所有标记 [P] 的任务可并行执行

### Phase 2: Foundational (阻塞性前置条件)

**目的**: 核心基础设施，任何用户故事开始前必须完成

**示例任务**:
```markdown
- [ ] T005 Setup database schema and migrations framework
- [ ] T006 [P] Implement authentication/authorization framework
- [ ] T007 [P] Setup API routing and middleware structure
- [ ] T008 Create base models that all stories depend on
- [ ] T009 Configure error handling and logging infrastructure
- [ ] T010 Setup environment configuration management
```

**⚠️ CRITICAL**: 无用户故事工作可在此阶段完成前开始

**检查点**: 基础就绪 - 用户故事实现现在可以并行开始

### Phase 3+: User Stories (按优先级)

**目的**: 按用户故事组织，每个故事独立可测试

#### 用户故事模板

```markdown
## Phase X: User Story N - [Title] (Priority: P1) 🎯 MVP

**目的**: [简要描述此故事交付的内容]

**独立测试**: [如何单独验证此故事]

### User Story N 的测试 (OPTIONAL - 仅当请求测试时) ⚠️

> **注意**: 先写这些测试，确保在实现前失败

- [ ] TXXX [P] [USn] [端点] 的契约测试 in tests/contract/test_[name].py
- [ ] TXXX [P] [USn] [用户旅程] 的集成测试 in tests/integration/test_[name].py

### User Story N 的实现

- [ ] TXXX [P] [USn] 在 src/models/[entity].py 中创建 [实体] 模型
- [ ] TXXX [P] [USn] 在 src/models/[entity].py 中创建 [实体] 模型
- [ ] TXXX [USn] 在 src/services/[service].py 中实现 [服务] (依赖于 TXXX, TXXX)
- [ ] TXXX [USn] 在 src/[location]/[file].py 中实现 [端点/功能]
- [ ] TXXX [USn] 添加验证和错误处理
- [ ] TXXX [USn] 为用户故事 N 的操作添加日志

**检查点**: 此时，用户故事 N 应完全功能且可独立测试
```

#### 并行执行示例

**同一用户故事内的并行任务**:
```bash
# 一起启动用户故事 1 的所有测试:
Task: "在 tests/contract/test_login.py 中编写登录端点的契约测试"
Task: "在 tests/integration/test_user_flow.py 中编写用户旅程的集成测试"

# 一起启动用户故事 1 的所有模型:
Task: "在 src/models/user.py 中创建 User 模型"
Task: "在 src/models/session.py 中创建 Session 模型"
```

**不同用户故事可并行**:
- 用户故事 1 (P1) ← Developer A
- 用户故事 2 (P2) ← Developer B
- 用户故事 3 (P3) ← Developer C

### Phase N: Polish (跨功能改进)

**目的**: 影响多个用户故事的改进

**示例任务**:
```markdown
- [ ] T090 [P] 在 docs/ 中更新文档
- [ ] T091 代码清理和重构
- [ ] T092 跨所有故事的性能优化
- [ ] T093 [P] 额外的单元测试 (如果请求) in tests/unit/
- [ ] T094 安全加固
- [ ] T095 运行 quickstart.md 验证
```

## 并行执行规则

### [P] 标记规则

**可并行** - 标记 [P] 当:
- 不同文件（无文件冲突）
- 无依赖关系
- 可独立完成

**必须串行** - 不标记 [P] 当:
- 同一文件
- 有明确依赖关系
- 需要前置任务输出

### 依赖关系

```
Phase Dependencies:
├─ Setup (Phase 1): 无依赖 - 可立即开始
├─ Foundational (Phase 2): 依赖于 Setup 完成 - 阻塞所有用户故事
├─ User Stories (Phase 3+): 全部依赖于 Foundational 完成
│  ├─ 然后可并行进行 (如有人员)
│  └─ 或按优先级顺序 (P1 → P2 → P3)
└─ Polish (最终阶段): 依赖于所有期望的用户故事完成

User Story Dependencies:
├─ User Story 1 (P1): Foundational 后可开始 - 无其他故事依赖
├─ User Story 2 (P2): Foundational 后可开始 - 可与 US1 集成但应独立测试
└─ User Story 3 (P3): Foundational 后可开始 - 可与 US1/US2 集成但应独立测试

Within Each Story:
├─ 测试 (如包含) 必须先写并在实现前失败
├─ 模型在服务前
├─ 服务在端点前
├─ 核心实现在集成前
└─ 故事在移动到下一优先级前完成
```

## 实施策略

### MVP 优先（仅用户故事 1）

1. 完成 Phase 1: Setup
2. 完成 Phase 2: Foundational (关键 - 阻塞所有故事)
3. 完成 Phase 3: User Story 1
4. **停止并验证**: 独立测试用户故事 1
5. 如准备就绪则部署/演示

### 增量交付

1. 完成 Setup + Foundational → 基础就绪
2. 添加用户故事 1 → 独立测试 → 部署/演示 (MVP!)
3. 添加用户故事 2 → 独立测试 → 部署/演示
4. 添加用户故事 3 → 独立测试 → 部署/演示
5. 每个故事在不破坏前述故事的情况下增加价值

### 团队并行策略

有多名开发人员时:

1. 团队一起完成 Setup + Foundational
2. Foundational 完成后:
   - 开发人员 A: 用户故事 1
   - 开发人员 B: 用户故事 2
   - 开发人员 C: 用户故事 3
3. 故事独立完成并集成

## 输入输出

### 输入

自动检测并加载：
- `plan.md` - 技术计划
- `spec.md` - 功能规格（用户故事）
- `data-model.md` - 数据模型（如存在）
- `contracts/` - API 契约（如存在）

### 输出

`tasks.md` 文件，包含：
- 按阶段组织的任务列表
- 依赖关系图
- 并行执行机会
- 实施策略建议

## 质量控制

### 任务完整性检查

- [ ] 每个用户故事有独立测试验证
- [ ] MVP 识别为第一个用户故事（P1）
- [ ] 任务包含精确文件路径
- [ ] 依赖关系清晰标注
- [ ] [P] 标记正确使用

### MVP 范围建议

分析用户故事，提供 MVP 建议：

```markdown
## MVP 范围建议

**最小可行产品**: User Story 1 (P1)

**理由**:
- 第一个用户故事交付核心价值
- 独立可测试和可部署
- 包含必要的基础设施

**增量计划**:
1. MVP (Story 1) → 交付
2. + Story 2 → 增强交付
3. + Story 3 → 完整功能
```

## 使用场景

### 场景 1: Plan 完成后生成任务

```text
/skill speckit-workflow "实现功能"
→ Specify 完成
→ Plan 完成
→ Analyze 完成
→ 调用 speckit-tasks 生成任务列表
→ 输出 tasks.md
```

### 场景 2: 独立生成任务

```text
/skill speckit-tasks --from-plan

# 基于当前 plan.md 和 spec.md 生成任务
```

### 场景 3: 重新组织任务

```text
/skill speckit-tasks --reorganize

# 基于现有 tasks.md 重新组织依赖和并行标记
```

## 相关技能

- `speckit-workflow` - 完整工作流（Tasks 阶段调用）
- `speckit-analyze` - 一致性分析（前置检查）

## 配置

### 自定义任务模板

在项目根目录创建 `.speckit-tasks-config.json`:

```json
{
  "phases": {
    "setup": {
      "enabled": true,
      "tasks": [
        "Create project structure",
        "Configure linting"
      ]
    }
  },
  "userStoryFormat": "## Phase {N}: {Title} (Priority: {P})",
  "enableTestsByDefault": false
}
```

## 限制

1. **TDD 要求**: 测试任务优先（如果启用）
2. **文件冲突**: 同文件任务必须串行
3. **依赖明确**: 必须标注依赖关系

## 最佳实践

1. **用户故事独立**: 每个故事应独立可测试
2. **MVP 优先**: 第一个用户故事作为 MVP
3. **清晰依赖**: 明确标注任务依赖
4. **合理并行**: 只在真正无依赖时使用 [P]
5. **文件路径**: 包含精确文件路径便于执行
