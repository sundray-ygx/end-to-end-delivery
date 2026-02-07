---
name: speckit-branch
description: Speckit 智能分支管理 - 自动编号、短名称生成、三源检测
---

# Speckit 智能分支管理

## 概述

本技能实现 Speckit 框架的智能分支管理功能，自动化功能分支的创建过程，确保分支命名的一致性和可追溯性。

**核心功能**:
- **自动编号** - 检测现有分支并分配下一个可用编号
- **短名称生成** - 从功能描述提取 2-4 词短名称
- **三源检测** - 同时检查远程分支、本地分支、specs 目录

## 使用方式

### 基本用法

```text
/skill speckit-branch "实现用户邮箱登录功能"
```

### 带自定义短名称

```text
/skill speckit-branch "实现用户邮箱登录功能" --short-name "email-login"
```

### 在工作流中调用

```text
# 在 Discovery 阶段自动调用
1. 调用 speckit-branch 创建分支
2. 继续需求发现...
```

## 工作流程

```
┌─────────────────────────────────────────────────────────────┐
│                    智能分支管理流程                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. 短名称生成                                              │
│     ├─ 分析功能描述                                        │
│     ├─ 提取关键词                                          │
│     └─ 生成 2-4 词短名称                                   │
│                                                             │
│  2. 三源编号检测                                            │
│     ├─ 远程分支: git ls-remote --heads origin              │
│     ├─ 本地分支: git branch                                 │
│     └─ Specs 目录: ls specs/                               │
│                                                             │
│  3. 编号分配                                                │
│     ├─ 提取所有现有编号                                    │
│     ├─ 找到最高编号 N                                      │
│     └─ 分配新编号 N+1                                      │
│                                                             │
│  4. 分支创建                                                │
│     ├─ 调用 create-new-feature.sh 脚本                     │
│     ├─ 创建编号分支: {N}-{SHORT-NAME}                      │
│     └─ 创建 specs 目录结构                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 输入输出

### 输入

- **功能描述** (必需): 自然语言功能描述
- **短名称** (可选): 2-4 词短名称，未提供时自动生成

### 输出

- **分支名称**: `{NUMBER}-{SHORT-NAME}` (如 `001-email-login`)
- **Spec 文件路径**: `specs/{NUMBER}-{SHORT-NAME}/spec.md`
- **分支状态**: 已创建并切换到新分支

## 短名称生成规则

### 自动生成

1. **分析功能描述**，提取关键概念
2. **使用动作-名词格式**（如适用）
   - "add user authentication" → `user-auth`
   - "fix payment timeout" → `fix-payment-timeout`

3. **保留技术术语和缩写**
   - OAuth2, API, JWT, HTTP, JSON

4. **保持简洁但描述性**
   - 2-4 个单词
   - 一目了然理解功能

### 示例

| 功能描述 | 短名称 |
|---------|--------|
| "I want to add user authentication" | `user-auth` |
| "Implement OAuth2 integration for the API" | `oauth2-api-integration` |
| "Create a dashboard for analytics" | `analytics-dashboard` |
| "Fix payment processing timeout bug" | `fix-payment-timeout` |

## 编号检测机制

### 三源检测

```bash
# 1. 获取所有远程分支
git fetch --all --prune
git ls-remote --heads origin | grep -E 'refs/heads/[0-9]+-{SHORT-NAME}$'

# 2. 检查本地分支
git branch | grep -E '^[* ]*[0-9]+-{SHORT-NAME}$'

# 3. 检查 Specs 目录
ls -d specs/[0-9]+-{SHORT-NAME} 2>/dev/null
```

### 编号分配

1. 从所有来源提取编号
2. 找到最高编号 N
3. 使用 N+1 作为新编号
4. 如无现有分支，从 001 开始

## 分支命名规范

### 格式

```
{NUMBER}-{SHORT-NAME}
```

### 规则

- **编号**: 3 位数字，从 001 开始
- **短名称**: 2-4 个单词，小写，连字符分隔
- **总长度**: 不超过 244 字节（GitHub 限制）

### 停用词过滤

以下词不作为短名称的首词：
- i, a, an, the, to, for, of, in, on, at, by, with...

### 示例

```
✅ 001-user-auth
✅ 002-oauth2-api-integration
✅ 003-analytics-dashboard
✅ 004-fix-payment-timeout

❌ 001-the-user-login     (停用词)
❌ 002-add                (无意义)
❌ 003-very-long-branch-name-that-exceeds-github-limit (太长)
```

## 目录结构

执行后创建：

```
specs/
└── {NUMBER}-{SHORT-NAME}/
    └── spec.md          # 功能规格（待填充）
```

## 脚本调用

内部调用 `.specify/scripts/bash/create-new-feature.sh`：

```bash
# Bash 语法
.specify/scripts/bash/create-new-feature.sh \
  --json \
  --number $N \
  --short-name "$SHORT_NAME" \
  "$ARGUMENTS"

# PowerShell 语法
.specify/scripts/bash/create-new-feature.sh `
  -Json `
  -Number $N `
  -ShortName "$SHORT_NAME" `
  "$ARGUMENTS"
```

### JSON 输出

脚本返回 JSON 包含：
```json
{
  "BRANCH_NAME": "001-email-login",
  "SPEC_FILE": "/path/to/specs/001-email-login/spec.md",
  "SPECS_DIR": "/path/to/specs/001-email-login"
}
```

## 使用场景

### 场景 1: 独立使用

```text
/skill speckit-branch "实现用户登录功能"
```

输出：
```
✓ 分支已创建: 001-user-login
✓ 已切换到新分支
✓ Spec 文件: specs/001-user-login/spec.md
```

### 场景 2: 在 Discovery 阶段调用

```text
# E2D Discovery 阶段
/discovery "实现用户登录功能"

# 内部自动调用
→ 调用 speckit-branch 创建分支
→ 继续需求发现...
```

### 场景 3: 在 Speckit 工作流中调用

```text
/skill speckit-workflow "实现用户登录功能"

# Specify 阶段自动调用
→ 调用 speckit-branch 创建分支
→ 继续规格生成...
```

## 错误处理

### 常见错误

| 错误 | 原因 | 解决方案 |
|------|------|---------|
| 脚本不存在 | `.specify/scripts/` 目录缺失 | 检查插件安装 |
| Git 仓库无效 | 非 Git 仓库或无权限 | 初始化 Git 仓库 |
| 分支已存在 | 分支命名冲突 | 手动删除冲突分支 |

### 参数转义

对于包含单引号的参数：
```bash
# 错误
--description "I'm Groot"

# 正确
--description 'I'\''m Groot'
# 或
--description "I'm Groot"
```

## 配置

### 环境变量

- `GIT_BRANCH`: 手动指定分支名（跳过自动检测）

### 配置文件

无额外配置文件，使用 Git 默认配置。

## 限制

1. **编号顺序**: 依赖正确的编号格式 `[0-9]+-{SHORT-NAME}`
2. **短名称冲突**: 相同短名称会递增编号
3. **GitHub 限制**: 分支名不超过 244 字节

## 相关技能

- `speckit-workflow` - 完整工作流（内部调用）
- `speckit-guard` - 宪法检查（后续阶段）

## 模板依赖

使用 `.specify/templates/spec-template.md` 生成初始 spec 文件。
