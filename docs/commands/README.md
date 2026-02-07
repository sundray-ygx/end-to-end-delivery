# 命令参考

本文档提供 end-to-end-delivery 插件所有命令的详细参考。

## 目录

- [Core Commands](#core-commands)
- [Workflow Commands](#workflow-commands)
- [Utility Commands](#utility-commands)

---

## Core Commands

核心命令是端到端开发流程的主要入口点。

### /deliver

启动完整的端到端价值交付闭环流程。

```bash
/deliver "实现用户登录功能"
```

**功能**：
- 自动执行：Discovery → Exploration → Design → Implementation → Verification → Delivery
- 全流程自动化管理
- 适用于完整功能开发

**相关命令**: `/discovery`, `/design`, `/implement`, `/verify`, `/delivery`

---

### /discovery

需求发现阶段。澄清问题、定义标准、识别约束。

```bash
/discovery "实现用户登录功能"
```

**功能**：
- 澄清需求和问题
- 定义验收标准
- 识别技术约束
- 评估需求复杂度

**输出**：
- 需求规格文档
- 验收标准列表
- 复杂度评估报告

**相关命令**: `/exploration`, `/design`

---

### /design

架构设计阶段。提供多个架构方案、权衡分析、实施蓝图。

```bash
/design
```

**功能**：
- 提供 3 个架构方案
- 权衡分析
- 输出实施蓝图

**输出**：
- 架构设计方案
- 权衡分析报告
- 实施蓝图文档

**相关命令**: `/discovery`, `/implement`

---

## Workflow Commands

工作流命令提供规范化的开发流程。

### /speckit-workflow

Speckit 规范化开发工作流的完整流程。

```bash
/speckit-workflow "实现用户登录功能"
```

**功能**：
- 整合所有 Speckit 步骤
- Specify → Plan → Tasks → Analyze → Implement
- 端到端规范化流程

**相关命令**:
- `/speckit-branch` - 智能分支管理
- `/speckit-guard` - 宪法治理检查
- `/speckit-tasks` - 任务依赖管理
- `/speckit-analyze` - 一致性分析
- `/speckit-checklist` - 质量检查清单

---

### /speckit-analyze

一致性分析。六重检测：重复、歧义、欠规格、宪法、覆盖、一致。

```bash
/speckit-analyze
```

**功能**：
- 检测需求重复
- 识别歧义表述
- 发现欠规格内容
- 验证宪法合规
- 评估覆盖完整性
- 检查一致性

**输出**：
- 一致性分析报告
- 问题列表和建议

---

### /speckit-tasks

任务依赖管理。用户故事分组、依赖关系可视化。

```bash
/speckit-tasks
```

**功能**：
- 分解用户故事
- 标记任务依赖
- 并行任务标记 [P]
- 可视化依赖关系

**输出**：
- 任务分解列表
- 依赖关系图
- 执行顺序建议

---

## Utility Commands

工具命令提供辅助和诊断功能。

### /exploration

代码库探索阶段。映射架构、识别模式、分析依赖。

```bash
/exploration
```

**功能**：
- 分析代码库结构
- 识别设计模式
- 映射依赖关系
- 发现技术债务

**输出**：
- 代码库地图
- 模式识别报告
- 依赖关系图

**相关命令**: `/discovery`, `/design`

---

### /implement

实施执行阶段。TDD 开发、代码质量保证。

```bash
/implement
```

**功能**：
- TDD 红-绿-重构循环
- 代码质量检查
- 自动化测试
- 覆盖率验证（≥80%）

**相关命令**: `/design`, `/verify`

---

### /verify

质量验证阶段。全面验证、质量门禁。

```bash
/verify
```

**功能**：
- 功能验证
- 测试覆盖率检查
- 代码质量审查
- 安全检查

**输出**：
- 验证报告
- 质量评分
- 改进建议

**相关命令**: `/implement`, `/delivery`

---

### /delivery

价值交付阶段。模式提取、知识沉淀。

```bash
/delivery
```

**功能**：
- 提取可复用模式
- 生成 Instincts
- 更新最佳实践
- 交付总结报告

**输出**：
- 模式库更新
- Instincts 导出
- 交付报告

**相关命令**: `/verify`

---

### /speckit-branch

智能分支管理。自动编号、短名称生成、三源检测。

```bash
/speckit-branch "实现用户登录功能"
```

**功能**：
- 自动生成分支编号
- 智能短名称
- 三源检测（Issue/Git/Branch）
- 分支命名规范

**输出**：
- 分支名称
- 创建命令

---

### /speckit-guard

宪法治理检查。质量门禁、复杂度论证、合规性验证。

```bash
/speckit-guard
```

**功能**：
- 质量门禁检查
- 复杂度论证
- 宪法合规性验证
- 风险评估

**输出**：
- 治理检查报告
- 风险列表
- 改进建议

---

### /speckit-checklist

质量检查清单。"需求质量单元测试"、可追溯性验证。

```bash
/speckit-checklist
```

**功能**：
- 需求质量检查
- 可追溯性验证
- 检查清单管理
- 覆盖率验证

**输出**：
- 检查清单报告
- 可追溯性矩阵
- 质量评分

---

### /diagnose

诊断专家。系统化调试、错误处理、安全诊断。

```bash
/diagnose "错误描述"
/diagnose --type build "构建失败"
/diagnose --type runtime "运行时异常"
/diagnose --type performance "性能问题"
/diagnose --type security "安全问题"
/diagnose --type database "数据库问题"
```

**功能**：
- 系统化调试
- 构建错误修复
- 错误处理模式
- 安全诊断
- 数据库诊断

---

### /ui-design

UI/UX 设计能力闭环。

```bash
/ui-design "SaaS analytics dashboard" --project-name "DataViz Pro"
/ui-design review src/components/Header.tsx
/ui-design check --web-guidelines src/
/ui-design search "glassmorphism dark" --domain style
```

**功能**：
- 设计系统生成（67种样式、96种调色板、57种字体）
- 高质量实现（独特美学方向）
- 规范验证（Vercel Web Interface Guidelines）
- 13种技术栈支持

---

### /instinct-export

导出 Instincts 学习数据。

```bash
/instinct-export
```

**功能**：
- 导出所有 Instincts
- 生成 JSON 文件
- 支持备份和分享

---

### /instinct-import

导入 Instincts 学习数据。

```bash
/instinct-import <file>
```

**功能**：
- 从文件导入 Instincts
- 恢复学习数据
- 合并现有数据

---

### /instinct-status

查看 Instincts 状态。

```bash
/instinct-status
```

**功能**：
- 显示 Instincts 数量
- 置信度分布
- 最近更新时间

---

### /evolve

演化 Instincts 为 Skills/Commands/Agents。

```bash
/evolve
```

**功能**：
- 自动识别高价值 Instincts
- 演化为可复用组件
- 生成代码模板
- 更新插件配置

---

## 命令流程图

```
完整 E2D 流程:
/deliver
  → /discovery
    → /exploration
      → /design
        → /implement
          → /verify
            → /delivery

Speckit 工作流:
/speckit-workflow
  → /speckit-branch (分支创建)
  → /speckit-guard (质量检查)
  → /speckit-tasks (任务分解)
  → /speckit-analyze (一致性分析)
  → /speckit-checklist (质量清单)
```

---

## 相关文档

- [快速开始](../README.md#快速开始)
- [配置指南](configuration.md)
- [最佳实践](best-practices.md)
- [架构设计](architecture.md)
