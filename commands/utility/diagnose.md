---
description: 诊断专家 - 整合三大插件优势的调试、诊断、修复系统（v3.0 支持 build/runtime/performance/security/database 五类诊断）
argument-hint: 问题描述
---

# /diagnose - 诊断命令 v3.0

诊断命令 - 整合三大插件优势的调试、诊断、修复系统。

## 使用方法

```bash
# 基础用法
/diagnose "构建失败，提示类型错误"

# 指定诊断类型
/diagnose --type build "TypeScript 错误"
/diagnose --type runtime "运行时异常"
/diagnose --type performance "查询慢"
/diagnose --type security "潜在漏洞"
/diagnose --type database "死锁检测"

# 交互式诊断
/diagnose
```

## 诊断类型

### build - 构建错误
- TypeScript 类型错误
- 语法错误
- 依赖问题
- 配置错误

### runtime - 运行时错误
- 异常处理
- 空指针异常
- 竞态条件
- 资源泄漏

### performance - 性能问题
- N+1 查询
- 慢查询
- 内存泄漏
- CPU 密集操作

### security - 安全问题
- SQL 注入
- XSS 漏洞
- 密钥泄露
- 认证问题

### database - 数据库问题
- 死锁
- 连接池耗尽
- 索引缺失
- 查询优化

## 诊断流程

1. **问题分类**：根据错误信息自动分类
2. **根因分析**：使用系统化方法分析
3. **解决方案**：提供最小化修复方案
4. **预防措施**：生成回归测试

## 使用 diagnostic-pro skill

```bash
# 自动调用 diagnostic-pro skill
/diagnose "TypeError: Cannot read property 'x' of undefined"

# 将使用以下模块:
# - debugging-strategies: 系统化调试
# - error-handling: 错误处理模式
# - build-fix: 构建修复（如适用）
# - security-diagnosis: 安全诊断（如适用）
# - database-diagnosis: 数据库诊断（如适用）
```

## 输出格式

```markdown
# 诊断报告

## 问题分类
- 类型: runtime
- 严重程度: 高
- 影响: 用户无法登录

## 根因分析
1. 用户对象未正确初始化
2. 缺少空值检查
3. 数据库查询返回 null

## 解决方案
\`\`\`typescript
// 添加可选链操作符
const name = user?.name || 'Anonymous'
\`\`\`

## 预防措施
- [ ] 添加输入验证
- [ ] 添加单元测试
- [ ] 更新文档
```
