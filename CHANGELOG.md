# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.1.0] - 2026-02-07

### Added - Speckit 规范化开发工作流

#### 核心工作流
- speckit-workflow skill: 完整的规范化功能开发流程
- 整合规格生成、技术计划、任务分解、一致性分析、实施执行

#### 智能分支管理 (speckit-branch)
- 自动检测现有分支并分配下一个可用编号
- 从功能描述提取 2-4 词短名称
- 三源检测（远程分支、本地分支、specs 目录）
- 分支命名格式: {NUMBER}-{SHORT-NAME}

#### 宪法治理检查 (speckit-guard)
- TDD 合规性验证
- 价值优先原则检查
- 规格质量标准验证
- 复杂度论证记录
- 质量门禁控制

#### 一致性分析 (speckit-analyze)
- 六重一致性检测:
  - 重复检测: 识别相似需求
  - 歧义检测: 标记模糊形容词
  - 欠规格检测: 缺失的验收标准
  - 宪法对齐: 检查合规性冲突
  - 覆盖率缺口: 需求到任务的覆盖
  - 不一致性: 术语漂移、冲突需求
- 严重程度分级 (CRITICAL/HIGH/MEDIUM/LOW)

#### 任务依赖管理 (speckit-tasks)
- 用户故事分组 (US1, US2, US3...)
- [P] 并行执行标记
- 依赖关系定义和可视化
- 分阶段任务组织 (Setup → Foundational → User Stories → Polish)

#### 质量检查清单 (speckit-checklist)
- "需求质量单元测试"概念
- 可追溯性验证
- 质量维度检查
- 自动生成忽略文件

### Changed - 工作流增强

#### end-to-end-workflow skill
- 各阶段新增 Speckit 增强选项
- Discovery 阶段: 可选调用 speckit-branch
- Design 阶段: 可选调用 speckit-guard、speckit-analyze
- Implementation 阶段: 可选调用 speckit-tasks、speckit-checklist
- Verification 阶段: 可选调用 speckit-analyze、speckit-guard
- Delivery 阶段: 可选调用 speckit-checklist

### Changed - 配置更新

- plugin.json: 版本更新至 3.1.0，新增 speckit 相关关键词

### Added - 新增命令

- `/speckit-workflow` - Speckit 规范化开发工作流
- `/speckit-branch` - 智能分支管理
- `/speckit-analyze` - 一致性分析
- `/speckit-guard` - 宪法治理检查
- `/speckit-tasks` - 任务依赖管理
- `/speckit-checklist` - 质量检查清单

### Added - 新增技能

- speckit-workflow skill: 完整工作流
- speckit-branch skill: 智能分支管理
- speckit-analyze skill: 一致性分析
- speckit-guard skill: 宪法治理检查
- speckit-tasks skill: 任务依赖管理
- speckit-checklist skill: 质量检查清单

## [3.0.0] - 2026-02-03

### Added - 核心能力

#### diagnostic-pro（诊断专家）
- 整合三大插件优势的调试、诊断、修复系统
- 系统化调试技术（科学方法、二分调试、Rubber Duck）
- 构建错误快速修复（增量式修复、最小化改动）
- 错误处理模式（异常层次、Result 类型、重试熔断）
- 安全诊断（SQL 注入、XSS、密钥泄露）
- 数据库诊断（查询优化、死锁检测、索引分析）
- 新增 `/diagnose` 命令

#### continuous-learning-v2（Instinct 学习）
- Instinct-based 学习系统，自动提取和演化知识
- Observer Agent 通过 hooks 捕获会话数据
- Instincts: 原子行为，带置信度评分（0.3-0.9）
- Evolution: Instincts → Skills/Commands/Agents
- 新增命令: `/instinct-export`, `/instinct-import`, `/instinct-status`, `/evolve`

### Added - 多语言支持

#### Python 全栈
- python-patterns skill: Python 最佳实践
- python-testing skill: pytest、factory_boy、TDD
- Django 支持（如适用）

#### Go 全栈
- golang-patterns skill: Go 最佳实践
- golang-testing skill: table-driven tests、testify
- Go 构建错误处理

#### C/C++ 全栈
- c-cpp-patterns skill: 现代 C++ (C++11/14/17/20)
- c-cpp-testing skill: Google Test/Catch2、内存泄漏检测
- RAII 模式、智能指针、并发编程

### Added - 专业能力

#### eval-harness（评估驱动开发）
- 在需求阶段定义评估标准
- Capability Evals: 功能评估
- Regression Evals: 回归评估
- pass@k 指标: 可靠性测量

#### database-reviewer（数据库专家）
- PostgreSQL 数据库架构审查
- 查询性能优化
- 模式设计、索引策略
- RLS 设计

#### iterative-retrieval（渐进式检索）
- 解决子代理上下文问题
- DISPATCH → EVALUATE → REFINE → LOOP
- 最多 3 次循环，渐进式细化代码库理解

### Changed - 代理增强

#### discovery-agent
- 集成 eval-harness 评估驱动能力

#### exploration-agent
- 集成 iterative-retrieval 渐进式检索模式

#### design-agent
- 集成 database-reviewer 数据库专家

#### implementation-agent
- 扩展多语言支持（Python/Go/C/C++）
- 更新 skill 映射表

#### verification-agent
- 集成诊断触发逻辑
- 验证失败时自动调用 diagnostic-pro

#### delivery-agent
- 集成 continuous-learning-v2 Instinct 学习
- 自动提取和演化可复用知识

### Changed - 配置更新

- plugin.json: 版本更新至 3.0.0，新增关键词
- settings.local.json: 新增所有 skills 的权限配置

## [2.0.0] - 2026-01-29

### Added
- 6 阶段工作流
- 本地模板融合
- 复杂度评估
- 维度覆盖度验证

## [1.0.0] - 2026-01-20

### Added
- 初始版本
- 端到端交付基础流程
