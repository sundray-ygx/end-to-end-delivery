---
name: speckit-checklist
description: Speckit 质量检查清单 - "需求质量单元测试"、可追溯性验证、质量维度检查
---

# Speckit 质量检查清单

## 概述

本技能实现 Speckit 框架的质量检查清单系统，被称为**"需求的单元测试"** - 验证需求本身的质量、清晰度和完整性，而非测试实现。

**核心原则**:
- **测试需求质量**，而非实现行为
- **可追溯性要求** ≥80% 项目必须包含引用
- **质量维度验证** - 完整性、清晰度、一致性等

## 检查清单目的

### 是什么（Unit Tests for Requirements）

检查清单验证需求文档本身的质量：

- ✅ "是否为所有卡片类型定义了视觉层次需求？" [完整性]
- ✅ "'突出显示'是否量化为具体尺寸/位置？" [清晰度]
- ✅ "所有交互元素的悬停状态需求是否一致？" [一致性]

### 不是什么（NOT Implementation Testing）

检查清单不验证系统实现：

- ❌ "验证按钮点击正确"
- ❌ "测试桌面版悬停效果正常"
- ❌ "确认 API 返回 200"

## 使用方式

### 基本用法

```text
/skill speckit-checklist
```

### 指定检查清单类型

```text
/skill speckit-checklist --type ux
/skill speckit-checklist --type api
/skill speckit-checklist --type security
```

### 在工作流中调用

```text
# Verify 阶段
/verify
→ 调用 speckit-checklist 验证需求质量
→ 根据结果决定是否交付
```

## 质量维度

### 1. 需求完整性 (Completeness)

检查所有必要需求是否已文档化：

- 是否为所有场景定义了需求？
- 是否为边缘情况定义了需求？
- 是否为所有交互元素定义了需求？
- 错误处理需求是否已定义？

**示例项目**:
```markdown
- [ ] CHK001 是否为所有 API 失败模式定义了错误处理需求？[Gap]
- [ ] CHK002 是否为所有交互元素定义了可访问性需求？[Completeness]
- [ ] CHK003 是否为响应式布局定义了移动断点需求？[Gap]
```

### 2. 需求清晰度 (Clarity)

检查需求是否具体且无歧义：

- 模糊术语是否已量化？
- 选择标准是否明确定义？
- 术语是否一致使用？

**示例项目**:
```markdown
- [ ] CHK001 "快速加载"是否量化了具体时间阈值？[Clarity, Spec §NFR-2]
- [ ] CHK002 "相关剧集"的选择标准是否明确定义？[Clarity, Spec §FR-5]
- [ ] CHK003 "突出显示"是否定义为可测量的视觉属性？[Ambiguity, Spec §FR-4]
```

### 3. 需求一致性 (Consistency)

检查需求是否对齐且无冲突：

- 导航需求在所有页面是否一致？
- 不同页面间的卡片组件需求是否一致？

**示例项目**:
```markdown
- [ ] CHK001 导航需求在所有页面间是否一致？[Consistency, Spec §FR-10]
- [ ] CHK002 登陆和详情页的卡片组件需求是否一致？[Consistency]
```

### 4. 验收标准质量 (Acceptance Criteria Quality)

检查成功标准是否可测量：

- 视觉层次需求是否可测量/可测试？
- "平衡视觉权重"能否客观验证？

**示例项目**:
```markdown
- [ ] CHK001 视觉层次需求是否可测量/可测试？[Acceptance Criteria, Spec §FR-1]
- [ ] CHK002 "平衡视觉权重"能否客观验证？[Measurability, Spec §FR-2]
```

### 5. 场景覆盖 (Coverage)

检查所有场景是否已解决：

- 是否存在零状态场景（无剧集）的需求？
- 是否处理了并发用户交互场景？
- 是否为部分数据加载失败定义了需求？

**示例项目**:
```markdown
- [ ] CHK001 是否为零状态场景（无剧集）定义了需求？[Coverage, Edge Case]
- [ ] CHK002 是否处理了并发用户交互场景？[Coverage, Gap]
- [ ] CHK003 是否为部分数据加载失败定义了需求？[Coverage, Exception Flow]
```

### 6. 边缘情况覆盖 (Edge Case Coverage)

检查边界条件是否定义：

- 是否定义了恢复/回滚需求（状态变更时）？
- 是否处理了零状态场景？

**示例项目**:
```markdown
- [ ] CHK001 是否为迁移失败定义了回滚需求？[Gap]
- [ ] CHK002 是否为零输入场景定义了需求？[Edge Case, Gap]
```

### 7. 非功能需求 (Non-Functional Requirements)

检查性能、安全、可访问性等：

- 性能需求是否量化？
- 安全需求是否已定义？
- 可访问性需求是否完整？

**示例项目**:
```markdown
- [ ] CHK001 性能需求是否量化了具体指标？[Clarity]
- [ ] CHK002 是否为所有关键用户旅程定义了性能目标？[Coverage]
- [ ] CHK003 性能需求是否在不同负载条件下指定？[Completeness]
```

### 8. 依赖与假设 (Dependencies & Assumptions)

检查外部因素是否文档化：

- 外部 API 需求是否已文档化？
- 假设是否已验证？

**示例项目**:
```markdown
- [ ] CHK001 外部 API 需求是否已文档化？[Dependency, Gap]
- [ ] CHK002 "podcast API 始终可用"的假设是否已验证？[Assumption]
```

### 9. 歧义与冲突 (Ambiguities & Conflicts)

检查需求中的问题：

- 模糊术语是否已量化？
- 需求间是否存在冲突？

**示例项目**:
```markdown
- [ ] CHK001 术语"快速"是否量化了具体指标？[Ambiguity, Spec §NFR-1]
- [ ] CHK002 §FR-10 和 §FR-10a 间的导航需求是否冲突？[Conflict]
```

## 可追溯性要求

### 最低要求

≥80% 的检查清单项目必须包含至少一个可追溯性引用

### 引用格式

| 引用类型 | 格式 | 示例 |
|---------|------|------|
| Spec 章节 | `[Spec §X.Y]` | `[Spec §FR-1]` |
| 缺口标记 | `[Gap]` | `[Gap]` |
| 歧义标记 | `[Ambiguity]` | `[Ambiguity]` |
| 冲突标记 | `[Conflict]` | `[Conflict]` |
| 假设标记 | `[Assumption]` | `[Assumption]` |

### 示例

```markdown
- [ ] CHK001 播放节目的数量和布局是否明确指定？[Completeness, Spec §FR-001]
- [ ] CHK002 悬停状态需求是否为所有交互元素一致定义？[Consistency, Spec §FR-003]
- [ ] CHK003 导航需求是否为所有可点击品牌元素清晰定义？[Clarity, Spec §FR-010]
- [ ] CHK004 相关剧集的选择标准是否已文档化？[Gap, Spec §FR-005]
- [ ] CHK005 是否为异步剧集数据定义了加载状态需求？[Gap]
```

## 检查清单类型

### UX Requirements Quality (`ux.md`)

**测试需求质量（非实现）**:

```markdown
- [ ] CHK001 视觉层次需求是否定义了可测量标准？[Clarity, Spec §FR-1]
- [ ] CHK002 UI 元素的数量和位置是否明确指定？[Completeness, Spec §FR-1]
- [ ] CHK003 交互状态需求（悬停、焦点、活动）是否一致定义？[Consistency]
- [ ] CHK004 是否为所有交互 UI 定义了键盘导航需求？[Coverage, Gap]
- [ ] CHK005 图片加载失败时的回退行为是否已定义？[Edge Case, Gap]
- [ ] CHK006 "视觉层次"需求能否客观测量？[Measurability, Spec §FR-1]
```

### API Requirements Quality (`api.md`)

```markdown
- [ ] CHK001 是否为所有失败场景指定了错误响应格式？[Completeness]
- [ ] CHK002 速率限制需求是否量化了具体阈值？[Clarity]
- [ ] CHK003 所有端点的认证需求是否一致？[Consistency]
- [ ] CHK004 是否为外部依赖定义了重试/超时需求？[Coverage, Gap]
- [ ] CHK005 版本控制策略是否在需求中已文档化？[Gap]
```

### Performance Requirements Quality (`performance.md`)

```markdown
- [ ] CHK001 性能需求是否量化了具体指标？[Clarity]
- [ ] CHK002 是否为所有关键用户旅程定义了性能目标？[Coverage]
- [ ] CHK003 是否为不同负载条件指定了性能需求？[Completeness]
- [ ] CHK004 性能需求能否客观测量？[Measurability]
- [ ] CHK005 是否为高负载场景定义了降级需求？[Edge Case, Gap]
```

### Security Requirements Quality (`security.md`)

```markdown
- [ ] CHK001 是否为所有受保护资源指定了认证需求？[Coverage]
- [ ] CHK002 是否为敏感信息定义了数据保护需求？[Completeness]
- [ ] CHK003 威胁模型是否已文档化且需求对齐？[Traceability]
- [ ] CHK004 安全需求是否与合规义务一致？[Consistency]
- [ ] CHK005 是否定义了安全失败/违规响应需求？[Gap, Exception Flow]
```

## 项目结构

```
specs/
└── {NUMBER}-{SHORT-NAME}/
    └── checklists/
        ├── requirements.md    # 规格质量检查
        ├── ux.md              # UX 需求质量
        ├── api.md             # API 需求质量
        ├── performance.md     # 性能需求质量
        ├── security.md        # 安全需求质量
        └── [domain].md        # 领域特定检查
```

## 检查清单验证

### 状态检查

扫描所有检查清单文件并创建状态表：

```markdown
## 检查清单验证状态

| 检查清单 | 总计 | 已完成 | 未完成 | 状态 |
|----------|------|--------|--------|------|
| requirements.md | 15 | 15 | 0 | ✓ 通过 |
| ux.md | 12 | 10 | 2 | ⚠️ 警告 |
| security.md | 8 | 8 | 0 | ✓ 通过 |

**整体**: [通过/失败/警告]
```

### 质量验证

- 确保项目测试需求质量（非实现）
- 验证可追溯性引用（spec 章节、[Gap]、[Ambiguity]）
- 确认 ≥80% 的项目包含可追溯性

## 使用场景

### 场景 1: Implement 阶段前验证

```text
/skill speckit-workflow "实现功能"
→ Tasks 完成
→ 调用 speckit-checklist 验证需求质量
→ CRITICAL 项目必须完成
→ 继续 Implement
```

### 场景 2: Verify 阶段检查

```text
/verify
→ 调用 speckit-checklist
→ 检查需求质量
→ 根据结果决定是否交付
```

### 场景 3: 独立质量检查

```text
/skill speckit-checklist --type ux

# 生成 UX 需求质量检查清单
```

## 质量门禁

| 检查清单状态 | CRITICAL | HIGH | MEDIUM | 决策 |
|-------------|----------|------|--------|------|
| 通过 | 0 未完成 | 0-1 未完成 | ≤3 未完成 | ✅ 继续 |
| 警告 | 0 未完成 | 2-3 未完成 | 4-6 未完成 | ⚠️ 用户决定 |
| 失败 | ≥1 未完成 | ≥4 未完成 | ≥7 未完成 | ❌ 修复后继续 |

## 相关技能

- `speckit-workflow` - 完整工作流（Implement 前调用）
- `speckit-analyze` - 一致性分析（相关但不同）

## 配置

### 自定义检查清单模板

在项目根目录创建 `.speckit-checklist-config.json`:

```json
{
  "types": {
    "ux": {
      "enabled": true,
      "categories": ["Completeness", "Clarity", "Consistency"]
    }
  },
  "traceability": {
    "minimumThreshold": 0.80
  }
}
```

## 限制

1. **需求聚焦**: 测试需求质量，而非实现
2. **可追溯性**: ≥80% 项目必须包含引用
3. **只读分析**: 不修改任何文件

## 最佳实践

1. **早期创建**: 在 Specify 阶段后创建检查清单
2. **迭代完善**: 随着需求细化更新检查清单
3. **独立于实现**: 关注需求质量，而非代码
4. **可追溯性**: 确保大部分项目有引用
5. **领域特定**: 为不同领域创建专门检查清单
