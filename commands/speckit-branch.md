---
description: Speckit 智能分支管理 - 自动编号、短名称生成、三源检测
argument-hint: 功能描述
---

# /speckit-branch - 智能分支管理

自动创建功能分支，包含智能编号、短名称生成和三源检测。

## 使用方式

```bash
# 基本用法
/speckit-branch "实现用户邮箱登录功能"

# 带自定义短名称
/speckit-branch "实现用户邮箱登录功能" --short-name "email-login"
```

## 功能

- **自动编号** - 检测现有分支并分配下一个可用编号
- **短名称生成** - 从功能描述提取 2-4 词短名称
- **三源检测** - 同时检查远程分支、本地分支、specs 目录

## 输出

```
✓ 分支已创建: 001-email-login
✓ 已切换到新分支
✓ Spec 文件: specs/001-email-login/spec.md
```

## 分支命名格式

```
{NUMBER}-{SHORT-NAME}

示例:
✓ 001-user-auth
✓ 002-oauth2-api-integration
✓ 003-analytics-dashboard
```

## 相关技能

```text
/skill speckit-branch "功能描述"
```
