# Instinct 演化系统完全指南

## 一、系统概述

### 1.1 什么是 Instinct？

**Instinct**（直觉/本能）是 AI 在执行任务时学到的**原子行为模式**。

### 类比理解
| 概念 | 程序员 | AI (Instinct) |
|------|--------|---------------|
| 基本单位 | 函数/类 | Instinct（原子行为） |
| 组织方式 | 库/框架 | Skill/Command/Agent |
| 学习方式 | 阅读代码/文档 | 观察会话/提取模式 |
| 置信度 | 单元测试覆盖 | 置信度评分 (0.3-0.9) |

---

## 二、演化系统架构

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Instinct 演化系统                                │
└─────────────────────────────────────────────────────────────────────┘

                        会话活动
                           ↓
                  ┌────────────────┐
                  │ Observer Agent │  ← 观察者：静默记录
                  └────────────────┘
                           ↓
                  ┌────────────────┐
                  │ observations   │  ← 原始数据
                  │   .jsonl       │
                  └────────────────┘
                           ↓
                  ┌────────────────┐
                  │  分析 & 提取   │  ← 识别模式
                  └────────────────┘
                           ↓
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                  ↓
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│   Instincts   │  │   Instincts   │  │   Instincts   │
│  (confidence  │  │  (confidence  │  │  (confidence  │
│   0.3-0.5)    │  │   0.6-0.7)    │  │   0.8-0.9)    │
│  低置信度     │  │  中置信度     │  │  高置信度     │
└───────────────┘  └───────────────┘  └───────────────┘
        ↓                  ↓                  ↓
    持续观察          成熟为技能         可立即演化
                           ↓
                  ┌────────────────┐
                  │    /evolve     │  ← 演化命令
                  └────────────────┘
                           ↓
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                  ↓
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│   Commands    │  │    Skills     │  │    Agents     │
│ 用户显式调用  │  │ 自动触发行为  │  │ 复杂多步骤    │
│  /commit      │  │ 代码风格检查  │  │ 架构设计流程  │
│  /review-pr   │  │ 错误处理模式  │  │ 端到端交付    │
└───────────────┘  └───────────────┘  └───────────────┘
```

---

## 三、完整工作流程

### 3.1 生命周期图

```
┌──────────────────────────────────────────────────────────────────────────┐
│                         Instinct 生命周期                                │
└──────────────────────────────────────────────────────────────────────────┘

阶段 1: 捕获 (Capture)
─────────────────────────────────────────────────────────────────────────
  日常开发会话 → Observer Agent 记录 → observations.jsonl

阶段 2: 提取 (Extraction)
─────────────────────────────────────────────────────────────────────────
  分析 observations → 识别模式 → 生成 Instincts (带置信度)

阶段 3: 成熟 (Maturation)
─────────────────────────────────────────────────────────────────────────
  低置信度 (0.3-0.5)     → 继续观察
  中置信度 (0.6-0.7)     → 多次验证
  高置信度 (0.8-0.9)     → 可演化

阶段 4: 演化 (Evolution)
─────────────────────────────────────────────────────────────────────────
  /evolve 命令 → 聚类分析 → 生成 Skills/Commands/Agents

阶段 5: 应用 (Application)
─────────────────────────────────────────────────────────────────────────
  新会话 → 自动/手动调用 → 持续优化
```

---

## 四、具体应用场景与实例

### 场景 1：代码提交规范自动化

#### 背景问题
团队每次提交代码时，AI 都要重新学习：
- 如何生成规范的 commit message
- 需要包含哪些信息
- 应该避免什么

#### 演化过程

**Step 1: 捕获阶段**
```bash
# 开发者进行多次提交会话
会话 1: "帮我提交代码，修改了用户登录功能"
  → AI 学到：需要查看 git diff，识别变更类型

会话 2: "提交这次修改"
  → AI 学到：需要遵循 Conventional Commits 格式

会话 3: "commit 这里的改动"
  → AI 学到：需要添加 Co-Authored-By 标记

会话 4-10: 类似请求...
```

**Step 2: Instinct 生成**
Observer 提取出 3 个 Instincts：

```yaml
# instinct-001.yaml
---
id: commit-message-diff-analysis
trigger: when user requests git commit
confidence: 0.85
domain: workflow
source: personal
---
## Context
User asks to commit code changes.

## Action
1. Run `git status` to see changes
2. Run `git diff` to understand modifications
3. Run `git log -3 --format='%an %ae'` to check recent authors
```

```yaml
# instinct-002.yaml
---
id: commit-conventional-format
trigger: when user requests git commit
confidence: 0.92
domain: workflow
source: personal
---
## Action
Format commit message using Conventional Commits:
- type: feat|fix|docs|style|refactor|test|chore
- scope: affected component
- subject: brief description
- body: detailed explanation (if needed)
```

```yaml
# instinct-003.yaml
---
id: commit-co-author-tag
trigger: when user requests git commit
confidence: 0.78
domain: workflow
source: personal
---
## Action
Add Co-Authored-By tag when AI contributed:
Co-Authored-By: Claude <noreply@anthropic.com>
```

**Step 3: 执行演化**
```bash
/evolve --domain workflow
```

**Step 4: 生成 Command**
```markdown
# commands/commit.md

---
description: Create git commit with proper message format
argument-hint: commit message description
---

# /commit - Smart Git Commit

Analyzes changes and creates properly formatted commit messages.

## Usage
/commit "Add user authentication"

## What it does
1. Runs git status and git diff
2. Identifies change type (feat/fix/docs/etc)
3. Generates Conventional Commit message
4. Adds Co-Authored-By when appropriate
5. Creates commit with proper formatting
```

#### 效果对比

| 对比项 | 演化前 | 演化后 |
|--------|--------|--------|
| 用户输入 | "帮我提交代码" | `/commit "添加用户登录"` |
| AI 行为 | 每次重新推理 | 直接执行标准化流程 |
| 一致性 | 不稳定 | 100% 规范 |
| 时间成本 | ~2 分钟 | ~10 秒 |

---

### 场景 2：错误处理模式演化

#### 背景问题
代码中重复出现的错误处理模式：
- API 调用失败重试
- 数据库连接错误处理
- 文件不存在时的降级方案

#### 演化过程

**捕获的 Instincts**

```yaml
# instinct-api-retry.yaml
---
id: api-call-retry-pattern
trigger: when implementing API client calls
confidence: 0.88
domain: error-handling
---
## Action
Wrap API calls with retry logic:
- Max 3 retries
- Exponential backoff (1s, 2s, 4s)
- Log each retry attempt
```

```yaml
# instinct-db-connection-retry.yaml
---
id: db-connection-retry
trigger: when implementing database operations
confidence: 0.82
domain: error-handling
---
## Action
Database connection pattern:
- Connection pool validation
- Retry on connection timeout
- Fail fast on authentication errors
```

```yaml
# instinct-file-graceful-degradation.yaml
---
id: file-not-found-handling
trigger: when reading optional config files
confidence: 0.75
domain: error-handling
---
## Action
Optional file pattern:
- Try to read file
- If not found, use defaults
- Log warning but continue
```

**执行演化**
```bash
/evolve --domain error-handling
```

**生成 Skill**
```markdown
# skills/resilient-operations/SKILL.md

---
name: resilient-operations
description: Automatic error handling and resilience patterns
---

## When to Use

This skill triggers automatically when:
- Implementing API calls
- Working with databases
- Reading optional files

## Patterns Included

### Retry Pattern
- Exponential backoff
- Configurable max retries
- Detailed logging

### Fallback Pattern
- Graceful degradation
- Default values
- Non-blocking failures

### Circuit Breaker Pattern
- Threshold-based tripping
- Automatic recovery
- Health check integration
```

#### 效果

| 代码场景 | 演化前 | 演化后 |
|----------|--------|--------|
| 开发者写 API 调用 | 手动写 retry 逻辑 | AI 自动添加 resilience |
| 错误处理一致性 | 各不相同 | 统一模式 |
| 代码审查要点 | 每次检查 | 自动保证 |

---

### 场景 3：架构设计流程演化

#### 背景问题
每次设计新功能时，AI 需要重新思考：
- 需要考虑哪些架构选项
- 如何进行权衡分析
- 应该输出什么文档

#### 演化过程

**捕获的 Instincts**（高置信度，来自多次架构设计会话）

```yaml
# instinct-arch-options.yaml
---
id: generate-multiple-architecture-options
trigger: when designing new feature architecture
confidence: 0.91
domain: architecture
---
## Action
Always provide 2-3 architecture options:
1. Describe each option
2. List pros and cons
3. Recommend with justification
```

```yaml
# instinct-arch-tradeoffs.yaml
---
id: analyze-architecture-tradeoffs
trigger: when comparing architecture approaches
confidence: 0.89
domain: architecture
---
## Action
Analyze tradeoffs across:
- Performance
- Scalability
- Maintainability
- Development time
- Operational complexity
```

```yaml
# instinct-arch-documentation.yaml
---
id: output-architecture-decision-record
trigger: when finalizing architecture design
confidence: 0.86
domain: architecture
---
## Action
Generate Architecture Decision Record:
- Context and problem
- Considered alternatives
- Decision rationale
- Consequences and implications
```

**执行演化**
```bash
/evolve --domain architecture
```

**生成 Agent**
```markdown
# agents/architecture-designer.md

# Architecture Designer Agent

Expert agent for designing software architectures with consistent analysis and documentation.

## Capabilities

1. **Multi-Option Generation**: Always provides 2-3 viable alternatives
2. **Tradeoff Analysis**: Systematic evaluation across 5 dimensions
3. **ADR Generation**: Creates Architecture Decision Records
4. **Pattern Matching**: Suggests appropriate design patterns

## Workflow

```
Requirements → Generate Options → Tradeoff Analysis → Recommendation → ADR
```

## When to Use

Invoke when:
- Designing new features
- Refactoring existing systems
- Evaluating technical approaches
- Documenting architecture decisions
```

#### 效果

| 维度 | 演化前 | 演化后 |
|------|--------|--------|
| 架构选项 | 有时提供1个 | 总是提供2-3个 |
| 分析深度 | 随机性强 | 5维度统一 |
| 文档输出 | 不稳定 | 标准ADR格式 |

---

## 五、使用指南

### 5.1 命令速查表

| 命令 | 功能 | 使用时机 |
|------|------|----------|
| `/instinct-status` | 查看所有 instincts 状态 | 定期检查学习进度 |
| `/instinct-import <file>` | 从外部导入 instincts | 获取团队共享知识 |
| `/instinct-export -o file` | 导出 instincts 到文件 | 备份或分享知识 |
| `/evolve` | 演化 instincts | 有 3+ 高置信度 instincts |
| `/evolve --domain <name>` | 按领域演化 | 针对性优化某领域 |
| `/evolve --dry-run` | 预览演化结果 | 不确定演化效果时 |

### 5.2 最佳实践

#### ✅ DO（推荐做法）

```bash
# 1. 定期检查状态
/instinct-status
# 每周查看积累了多少 insights

# 2. 达到阈值后演化
/evolve --threshold 5
# 等待至少 5 个相关 instincts 再演化

# 3. 按领域演化
/evolve --domain testing
/evolve --domain workflow
# 分别优化不同领域

# 4. 导出备份
/instinct-export -o backup-$(date +%Y%m%d).yaml
# 定期备份积累的知识
```

#### ❌ DON'T（不推荐做法）

```bash
# 1. 不要过早演化
/evolve  # 当只有 1-2 个 instincts 时
# 结果：无法形成有效模式

# 2. 不要忽略置信度
# 低置信度 (<0.6) 的 instincts 还不稳定

# 3. 不要一次性演化所有领域
/evolve  # 当有 100+ instincts 跨多个领域
# 建议：按领域分批演化
```

### 5.3 置信度阈值指南

| 置信度范围 | 建议 | 演化类型 |
|------------|------|----------|
| 0.3 - 0.5 | 继续观察 | 不演化 |
| 0.6 - 0.7 | 可以考虑 | 演化为 Skill |
| 0.8 - 0.9 | 立即演化 | 演化为 Command/Agent |
| 0.9+ | 优先演化 | 高价值输出 |

---

## 六、演化类型决策树

```
                    ┌─────────────────┐
                    │   Instincts    │
                    │   已积累足够    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ 用户显式请求？  │
                    └────┬────────┬───┘
                         │ YES    │ NO
                         ▼        ▼
                ┌────────────┐  ┌────────────┐
                │ COMMAND    │  │ 自动触发？ │
                │ /commit    │  └────┬───┬───┘
                │ /review-pr │       │   │
                │ /deploy    │    YES│   │NO
                └────────────┘       ▼   ▼
                          ┌───────────┐ ┌──────────┐
                          │  SKILL    │ │多步骤？  │
                          │ 自动触发  │ └─────┬────┘
                          │ 代码风格  │       │
                          │ 错误处理  │    YES│ NO
                          └───────────┘       ▼
                                      ┌───────────┐
                                      │  AGENT    │
                                      │ 复杂流程  │
                                      │ 多步骤    │
                                      └───────────┘
```

---

## 七、实际案例：完整演化周期

### 案例：从零到创建 `/commit` 命令

#### 第一周：捕获期
```
会话 1-3: 用户请求提交代码
  → Observer 记录行为模式
  → 提取 3 个低置信度 instincts (0.4-0.5)

/instinct-status
  Total: 3 instincts
  High confidence: 0
```

#### 第二周：验证期
```
会话 4-8: 更多提交请求
  → 现有 instincts 被验证
  → 置信度提升到 0.6-0.7
  → 新增 2 个相关 instincts

/instinct-status
  Total: 5 instincts
  High confidence: 0
  Medium confidence: 5
```

#### 第三周：成熟期
```
会话 9-15: 模式稳定
  → 所有 instincts 置信度 > 0.8
  → 发现一致的模式

/instinct-status
  Total: 8 instincts
  High confidence: 8  ← 可演化！
  Domain: workflow
```

#### 第四周：演化期
```bash
/evolve --domain workflow

输出：
  === EVOLVE ANALYSIS - 8 instincts ===

  High confidence instincts (>=80%): 8
  Potential skill clusters found: 2

  ## SKILL CANDIDATES

  1. Cluster: "git commit operations"
     Instincts: 5
     Avg confidence: 87%
     Domains: workflow
     Instincts:
       - commit-message-diff-analysis
       - commit-conventional-format
       - commit-co-author-tag
       - commit-changelog-update
       - commit-branch-validation

  ## COMMAND CANDIDATES (5)

    /commit
      From: git-commit-operations
      Confidence: 87%

  ===生成建议===
  建议演化类型: COMMAND
  理由: 用户显式请求操作，模式稳定
```

#### 执行演化
```bash
/evolve --domain workflow --generate

✅ 生成完成！
  Command: /commit
  位置: commands/commit.md
  Instincts 聚合: 5
```

#### 第五周：应用期
```
用户: /commit "fix user authentication bug"

AI: [直接执行 learned 模式]
  1. 运行 git status ✓
  2. 分析 git diff ✓
  3. 识别类型: fix ✓
  4. 生成 message: fix(auth): resolve login timeout ✓
  5. 添加 Co-Authored-By ✓
  6. 创建提交 ✓

完成时间: 8 秒
```

---

## 八、常见问题

### Q1: 多久演化一次？
**A:** 取决于使用频率：
- 高频团队（每天使用）：每周检查，每2-3周演化
- 中频团队：每两周检查，每月演化
- 低频使用：每月检查，季度演化

### Q2: 演化后会丢失原始 instincts 吗？
**A:** 不会。instincts 保留在 `~/.claude/homunculus/instincts/`，演化结果保存在 `~/.claude/homunculus/evolved/`，两者共存。

### Q3: 可以手动编辑生成的 commands/skills/agents 吗？
**A:** 可以且推荐！演化生成的是起点，你应该根据实际需求调整：
- 优化描述
- 调整参数
- 添加边界情况处理

### Q4: 如何判断演化质量？
**A:** 检查以下几点：
- 生成的 command/skill 是否符合直觉？
- 覆盖的场景是否全面？
- 是否有遗漏的重要边界情况？
- 置信度是否 >= 0.8？

### Q5: 可以撤销演化吗？
**A:** 可以。删除 `~/.claude/homunculus/evolved/` 下对应文件即可，instincts 保持不变。

---

## 九、总结

### 核心价值

1. **知识积累**: 从零散经验 → 系统化知识
2. **效率提升**: 从每次推理 → 直接执行
3. **一致性保证**: 从随机变化 → 稳定输出
4. **团队协作**: 从个人经验 → 共享资产

### 使用原则

1. **耐心积累**: 等待足够 instincts（3+ 高置信度）
2. **按需演化**: 有明确需求时才演化
3. **持续优化**: 演化后根据反馈调整
4. **定期备份**: 导出 instincts 作为知识库

### 快速开始

```bash
# 1. 检查当前状态
/instinct-status

# 2. 如果有 3+ 高置信度 instincts
/evolve

# 3. 查看演化结果
ls ~/.claude/homunculus/evolved/

# 4. 应用到新会话
# （自动或手动调用生成的 commands/skills/agents）
```

---

这个系统让 AI 随着使用越来越"聪明"——不是通过重新训练，而是通过观察和学习！
