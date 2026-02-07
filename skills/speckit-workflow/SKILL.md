---
name: speckit-workflow
description: Speckit 规范化功能开发工作流 - 整合规格生成、技术计划、任务分解、一致性分析、实施执行的完整流程
---

# Speckit 规范化功能开发工作流

## 概述

本技能实现了 Speckit 框架的完整开发工作流，从自然语言功能描述到可执行的任务列表，确保每个环节都有明确的质量保证机制。

**核心原则**:
- **Specification First** - 规格优先，清晰的需求定义
- **Constitution Driven** - 宪法驱动，质量门禁控制
- **Consistency Verified** - 一致性验证，六重分析检测
- **Task Dependency Managed** - 依赖管理，并行执行优化

## 工作流架构

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         Speckit 规范化开发工作流                             │
└─────────────────────────────────────────────────────────────────────────────┘

     ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
     │   Specify   │───▶│    Plan     │───▶│    Tasks    │───▶│   Analyze   │
     │   规格生成    │    │   技术计划    │    │   任务分解    │    │  一致性分析   │
     └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
           │                   │                   │                   │
           ▼                   ▼                   ▼                   ▼
     ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
     │ 智能分支管理  │    │ 宪法检查     │    │ 任务依赖管理  │    │ 六重一致性   │
     │ 自动编号     │    │ 质量门禁     │    │ [P]并行标记  │    │ 严重程度分级  │
     │ 短名称生成   │    │ 复杂度论证   │    │ 用户故事分组  │    │ 覆盖率分析   │
     └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                                                                 │
                                                                 ▼
                                                          ┌─────────────┐
                                                          │  Implement  │
                                                          │   实施执行    │
                                                          └─────────────┘
                                                                │
                                                                ▼
                                                          ┌─────────────┐
                                                          │ TDD 执行    │
                                                          │ 检查清单验证 │
                                                          └─────────────┘
```

## 使用方式

### 完整工作流执行

```text
/skill speckit-workflow "实现用户邮箱登录功能"
```

### 带上下文执行

```text
/skill speckit-workflow """
实现用户登录功能，需求如下：
- 支持邮箱和密码登录
- 登录后返回 JWT token
- 记住登录状态 7 天
- 有登录失败次数限制
"""
```

## 阶段详解

### 阶段 1: Specify (规格生成)

**目标**: 将自然语言功能描述转化为结构化规格文档

**输入**: 功能描述文本
**输出**: `specs/{NUMBER}-{SHORT-NAME}/spec.md`

**活动**:
1. **智能分支管理** (调用 speckit-branch)
   - 自动检测现有分支编号（远程 + 本地 + specs 目录）
   - 生成 2-4 词短名称
   - 创建编号分支：`{NUMBER}-{SHORT-NAME}`

2. **需求解析**
   - 识别角色、操作、数据、约束
   - 限制澄清标记最多 3 个
   - 按影响优先级：范围 > 安全/隐私 > 用户体验 > 技术细节

3. **规格生成**
   - 用户场景（优先级 P1, P2, P3...）
   - 功能需求（每个必须可测试）
   - 成功标准（可测量、技术无关）
   - 关键实体（如涉及数据）

**质量检查**:
- [ ] 无 [NEEDS CLARIFICATION] 标记
- [ ] 所有需求可测试
- [ ] 成功标准可测量
- [ ] 用户场景独立可测试

### 阶段 2: Plan (技术计划)

**目标**: 制定详细的技术实施方案

**输入**: `spec.md`
**输出**: `plan.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md`

**活动**:
1. **宪法检查** (调用 speckit-guard)
   - 验证 TDD 合规性
   - 检查价值优先原则
   - 评估规格质量标准
   - 记录复杂度论证

2. **技术上下文**
   - 语言/版本（或 NEEDS CLARIFICATION）
   - 主要依赖
   - 存储方案
   - 测试框架
   - 目标平台
   - 项目类型（single/web/mobile）

3. **Phase 0: 研究阶段**
   - 解决所有 NEEDS CLARIFICATION
   - 技术选型决策
   - 最佳实践研究

4. **Phase 1: 设计阶段**
   - 数据模型 (`data-model.md`)
   - API 契约 (`contracts/`)
   - 快速开始指南 (`quickstart.md`)
   - Agent 上下文更新

**质量门禁**:
- [ ] 宪法检查通过
- [ ] 所有 NEEDS CLARIFICATION 已解决
- [ ] 技术决策已记录
- [ ] 数据模型和契约已定义

### 阶段 3: Tasks (任务分解)

**目标**: 将设计转化为可执行的任务列表

**输入**: `plan.md`, `spec.md`, `data-model.md`, `contracts/`
**输出**: `tasks.md`

**活动**:
1. **任务依赖管理** (调用 speckit-tasks)
   - 用户故事分组（US1, US2, US3...）
   - [P] 并行执行标记
   - 依赖关系定义

2. **任务组织**
   - Phase 1: Setup（共享基础设施）
   - Phase 2: Foundational（阻塞性前置条件）
   - Phase 3+: User Stories（按优先级 P1, P2, P3...）
   - Phase N: Polish（跨功能改进）

3. **任务格式**
   ```
   - [ ] T001 [P] [US1] Description with file path
   ```

   - `[P]`: 可并行执行（不同文件，无依赖）
   - `[US1]`: 所属用户故事
   - 包含精确文件路径

**任务原则**:
- 每个用户故事独立可测试
- MVP 是第一个用户故事（P1）
- 测试任务在实现任务之前
- 清晰的依赖关系

### 阶段 4: Analyze (一致性分析)

**目标**: 执行跨文档的一致性和质量分析

**输入**: `spec.md`, `plan.md`, `tasks.md`
**输出**: 分析报告

**活动**:
1. **六重一致性检测** (调用 speckit-analyze)
   - **重复检测**: 识别相似需求
   - **歧义检测**: 标记模糊形容词（fast, scalable）
   - **欠规格检测**: 缺失的验收标准
   - **宪法对齐**: 检查合规性冲突
   - **覆盖率缺口**: 需求到任务的覆盖
   - **不一致性**: 术语漂移、冲突需求

2. **严重程度分级**
   - **CRITICAL**: 违反宪法 MUST、缺失核心章节
   - **HIGH**: 重复/冲突需求、模糊的安全/性能
   - **MEDIUM**: 术语漂移、缺失边缘情况
   - **LOW**: 措辞改进、轻微冗余

3. **生成报告**
   - 发现汇总表
   - 覆盖率分析
   - 宪法合规状态
   - 修复建议

**质量门禁**:
- [ ] 无 CRITICAL 问题
- [ ] 覆盖率 ≥ 80%
- [ ] 宪法合规
- [ ] 术语一致

### 阶段 5: Implement (实施执行)

**目标**: 按 TDD 原则执行任务列表

**输入**: `tasks.md`, `plan.md`
**输出**: 实现代码、测试

**活动**:
1. **前置检查**
   - 检查清单验证 (调用 speckit-checklist)
   - 项目类型检测
   - 忽略文件自动生成

2. **TDD 执行**
   - 先写测试，验证测试失败
   - 再实现功能
   - Red-Green-Refactor 循环

3. **分阶段执行**
   - **Setup**: 项目初始化
   - **Foundational**: 核心基础设施（阻塞所有用户故事）
   - **User Stories**: 按优先级独立实现
   - **Polish**: 跨功能改进

4. **进度跟踪**
   - 完成任务标记为 [X]
   - 检查点验证
   - 错误处理

**质量门禁**:
- [ ] 所有任务完成
- [ ] 测试通过
- [ ] 用户故事独立可测试
- [ ] 符合技术计划

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
    │   ├── api.yaml
    │   └── schema.graphql
    └── checklists/          # 质量检查清单
        ├── requirements.md
        ├── ux.md
        └── security.md
```

## 独立 Skill 调用

完整工作流内部会调用以下独立技能，用户也可以单独调用：

| Skill | 功能 | 调用时机 |
|-------|------|---------|
| `speckit-branch` | 智能分支管理 | Specify 阶段 |
| `speckit-guard` | 宪法治理检查 | Plan 阶段 |
| `speckit-tasks` | 任务依赖管理 | Tasks 阶段 |
| `speckit-analyze` | 一致性分析 | Analyze 阶段 |
| `speckit-checklist` | 质量检查清单 | Implement 阶段 |

## 与 End-to-End-Delivery 集成

Speckit 工作流可以独立使用，也可以嵌入到 E2D 工作流中作为增强选项：

```text
# E2D 工作流中使用 Speckit 增强
/deliver "实现用户登录功能"
  → Discovery 阶段调用 speckit-branch
  → Design 阶段调用 speckit-guard
  → Implementation 阶段调用 speckit-tasks
  → Verify 阶段调用 speckit-analyze
  → Delivery 阶段调用 speckit-checklist
```

## 质量保证

### 自动质量检查
- 规格完整性验证
- 宪法合规门禁
- 一致性自动分析
- 任务依赖验证

### 证据优先
- 每个阶段有明确输出
- 质量门禁必须通过
- 测试驱动开发
- 可追溯的需求到代码

## 模板系统

工作流使用 `.specify/templates/` 中的模板：

- `spec-template.md` - 功能规格模板
- `plan-template.md` - 实施计划模板
- `tasks-template.md` - 任务列表模板
- `checklist-template.md` - 检查清单模板

**自动回退机制**: 模板不存在时使用内置默认模板
