---
name: diagnostic-pro
description: 诊断专家 - 整合三大插件优势的调试、诊断、修复系统。提供系统化调试技术、构建错误修复、错误处理模式、安全诊断、数据库诊断等全面能力。
version: 1.0.0
---

# 诊断专家 (Diagnostic Pro)

整合 superpowers、everything-claude-code、developer-essentials 三大插件的诊断优势能力，形成加强版的独立诊断系统。

## 核心能力

### 1. 系统化调试技术 (来自 developer-essentials)
- 根因分析方法论
- 二分调试、差分调试、回溯调试
- Rubber Duck 调试法
- 证据收集与假设验证

### 2. 构建错误修复 (来自 everything-claude-code)
- 增量式 TypeScript/构建错误修复
- 最小化改动原则
- 类型错误快速定位

### 3. 错误处理模式 (来自 developer-essentials)
- 异常层次结构设计
- Result 类型模式
- 重试与熔断模式
- 优雅降级策略

### 4. 安全诊断 (来自 everything-claude-code)
- 安全漏洞扫描
- OWASP Top 10 检查
- 密钥泄露检测

### 5. 数据库诊断 (来自 everything-claude-code)
- 查询性能分析
- 死锁检测
- 索引优化建议

## 诊断流程

```
┌─────────────────────────────────────────────────────────────────┐
│                        诊断专家工作流                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  │
│  │ 问题分类  │───▶│ 根因分析  │───▶│ 解决方案  │───▶│ 预防措施  │  │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘  │
│       │              │              │              │            │
│       ▼              ▼              ▼              ▼            │
│  构建错误        系统化方法        增量修复        回归测试      │
│  运行时错误        证据收集        最小改动        模式提取      │
│  性能问题        假设验证        验证有效        知识沉淀      │
│  安全问题                                                  │
│  数据库问题                                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 使用场景

### 构建失败
```bash
/diagnose --type build "TypeScript 类型错误"
```

### 运行时异常
```bash
/diagnose --type runtime "空指针异常"
```

### 性能问题
```bash
/diagnose --type performance "查询响应慢"
```

### 安全问题
```bash
/diagnose --type security "潜在 SQL 注入"
```

### 数据库问题
```bash
/diagnose --type database "死锁检测"
```

### 交互式诊断
```bash
/diagnose
# 引导式诊断流程
```

## 模块说明

### debugging-strategies
系统化调试技术框架，提供科学的诊断方法论。

### build-fix
构建错误快速修复，增量式解决问题。

### error-handling
错误处理模式库，提供健壮的错误处理策略。

### security-diagnosis
安全诊断模块，识别和修复安全漏洞。

### database-diagnosis
数据库诊断模块，优化查询性能和解决数据库问题。

## 相关命令

- `/diagnose` - 启动诊断流程
- `/build-fix` - 构建错误快速修复

## 相关代理

- `diagnostic-agent` - 诊断专家代理
