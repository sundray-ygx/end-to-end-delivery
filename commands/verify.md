---
description: 执行质量验证阶段 - 全面验证、生成报告、确保质量门禁通过（v3.0 集成 diagnostic-pro）
argument-hint: (可选) 验证范围
---

# /verify - 质量验证阶段 v3.0

执行端到端交付流程的第五阶段：质量验证。

**前置条件**: 必须先完成 Implementation 阶段

## v3.0 新特性

### diagnostic-pro 诊断触发
当验证失败时，自动触发诊断系统进行问题分析：

**支持诊断类型**:
- `--type build` - 构建错误诊断（增量式修复、最小化改动）
- `--type runtime` - 运行时异常诊断（异常层次、错误处理）
- `--type performance` - 性能问题诊断（Profiling、优化建议）
- `--type security` - 安全问题诊断（SQL 注入、XSS、密钥泄露）
- `--type database` - 数据库问题诊断（查询优化、死锁检测）

**自动触发**:
```bash
# 验证失败时自动调用
/verify
# 检测到问题 → 自动触发 /diagnose --type [自动检测]
```

## 使用方式

```bash
# 启动质量验证阶段
/verify

# 验证特定范围
/verify "build and tests only"

# 重新验证
/verify --re-run
```

## 阶段目标

执行全面验证，确保质量门禁通过。

## 验证流程

### 1. 构建验证
```bash
npm run build
# 检查: 退出码为 0, 无构建错误
```

### 2. 类型检查
```bash
npx tsc --noEmit
# 检查: 无类型错误
```

### 3. 代码规范检查
```bash
npm run lint
# 检查: 无规范错误
```

### 4. 测试验证
```bash
npm test -- --coverage
# 检查: 所有测试通过, 覆盖率 ≥ 80%
```

### 5. 安全扫描
```bash
# 检查硬编码密钥
grep -rn "sk-" --include="*.ts" . | head -10

# 检查 console.log
grep -rn "console.log" --include="*.ts" src/ | head -10
```

### 6. 变更审查
```bash
git diff --stat
git diff HEAD~1 --name-only
```

## 证据优先原则

**核心规则**: NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE

```markdown
❌ 错误: "应该能通过测试"
✅ 正确: "测试全部通过 (34/34), 覆盖率 95%"

❌ 错误: "看起来构建成功了"
✅ 正确: "构建成功 (exit 0), 输出: dist/"
```

## 验证报告

```markdown
# 验证报告

## 执行摘要

| 验证项 | 状态 | 详情 |
|--------|------|------|
| 构建 | ✅/❌ | [详情] |
| 类型检查 | ✅/❌ | [详情] |
| 代码规范 | ✅/❌ | [详情] |
| 测试 | ✅/❌ | [详情] |
| 安全 | ✅/❌ | [详情] |

## 总体评估

**状态**: ✅ READY / ❌ NOT READY

## 详细结果

### 1. 构建验证
**状态**: ✅ PASS / ❌ FAIL
**输出**: [构建输出]

### 2. 类型检查
**状态**: ✅ PASS / ❌ FAIL
**类型错误**: X 个

### 3. 代码规范
**状态**: ✅ PASS / ❌ FAIL
**警告**: X 个
**错误**: X 个

### 4. 测试验证
**状态**: ✅ PASS / ❌ FAIL
**测试结果**: X/X 通过
**覆盖率**: XX%

### 5. 安全扫描
**状态**: ✅ PASS / ❌ FAIL
**安全问题**: [列表]

### 6. 变更审查
**变更文件**: X 个
**文件列表**: [列表]

## 问题汇总

### 阻塞性问题 (必须修复)
1. [问题描述]
   - 位置: file.ts:123
   - 修复建议: [建议]

### 非阻塞性问题 (建议修复)
1. [问题描述]
   - 位置: file.ts:456
   - 修复建议: [建议]

## 下一步

**如果 READY**: 可以继续交付流程
**如果 NOT READY**: 修复问题后重新验证
```

## 质量门禁

完成质量验证前，确认:
- [ ] 构建成功
- [ ] 类型检查通过
- [ ] 代码规范通过
- [ ] 测试全部通过
- [ ] 测试覆盖率 ≥ 80%
- [ ] 安全扫描通过
- [ ] 无阻塞性问题

## 下一阶段

质量验证完成后，进入价值交付阶段:
```bash
/delivery
```
