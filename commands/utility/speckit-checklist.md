---
description: Speckit 质量检查清单 - "需求质量单元测试"、可追溯性验证、质量维度检查
argument-hint: (可选) --type [ux|api|security|performance]
---

# /speckit-checklist - 质量检查清单

被称为**"需求的单元测试"** - 验证需求本身的质量、清晰度和完整性。

## 核心原则

- **测试需求质量**，而非实现行为
- **可追溯性要求** ≥80% 项目必须包含引用
- **质量维度验证** - 完整性、清晰度、一致性等

## 是什么（Unit Tests for Requirements）

✅ "是否为所有卡片类型定义了视觉层次需求？"
✅ "'突出显示'是否量化为具体尺寸/位置？"
✅ "所有交互元素的悬停状态需求是否一致？"

## 不是什么（NOT Implementation Testing）

❌ "验证按钮点击正确"
❌ "测试桌面版悬停效果正常"
❌ "确认 API 返回 200"

## 使用方式

```bash
# 基本用法
/speckit-checklist

# 指定检查清单类型
/speckit-checklist --type ux
/speckit-checklist --type api
/speckit-checklist --type security
/speckit-checklist --type performance
```

## 质量维度

| 维度 | 检查项 |
|------|--------|
| **完整性** | 所有必要需求是否已文档化 |
| **清晰度** | 需求是否具体且无歧义 |
| **一致性** | 需求是否对齐且无冲突 |
| **验收标准** | 成功标准是否可测量 |
| **覆盖度** | 所有场景是否已解决 |
| **边缘情况** | 边界条件是否定义 |
| **非功能** | 性能、安全、可访问性 |
| **依赖假设** | 外部因素是否文档化 |

## 可追溯性

≥80% 的检查清单项目必须包含引用：

```markdown
- [ ] CHK001 视觉层次需求是否定义了可测量标准？[Clarity, Spec §FR-1]
- [ ] CHK002 是否为所有交互 UI 定义了键盘导航需求？[Coverage, Gap]
- [ ] CHK003 相关剧集的选择标准是否已文档化？[Gap, Spec §FR-5]
```

## 输出

```markdown
# 检查清单: [TYPE]

## 需求完整性
- [ ] CHK001 是否为所有场景定义了需求？[Completeness]
- [ ] CHK002 是否为边缘情况定义了需求？[Gap]

## 需求清晰度
- [ ] CHK001 "快速加载"是否量化了具体时间？[Clarity, Spec §NFR-2]

## 可追溯性: 85% (17/20)
```

## 相关技能

```text
/skill speckit-checklist --type ux
```
