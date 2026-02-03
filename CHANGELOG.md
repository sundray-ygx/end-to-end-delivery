# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
