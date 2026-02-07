# 端到端价值交付闭环插件 (End-to-End Delivery)

整合 superpowers、everything-claude-code、feature-dev 三大插件精华，形成的完整端到端价值交付闭环开发流程。

**版本**: v3.1 | **许可**: MIT | **作者**: Claude Code User

---

## 快速开始

### 1. 安装插件

```bash
# 插件安装位置
~/.claude/plugins/cache/local-plugins/end-to-end-delivery/
```

### 2. 配置权限

在 `.claude/settings.local.json` 中添加：

```json
{
  "permissions": {
    "allow": ["Skill(end-to-end-delivery:*)"]
  }
}
```

### 3. 开始使用

```bash
# 启动完整的端到端流程
/deliver "实现用户登录功能"

# 或使用 Speckit 规范化工作流
/speckit-workflow "实现用户登录功能"

# 或分阶段执行
/discovery "实现用户登录功能"
/exploration
/design
/implement
/verify
/delivery
```

---

## 核心概念

### 工作流架构

```
Discovery → Exploration → Design → Implementation → Verification → Delivery
    ↓           ↓            ↓         ↓            ↓          ↓
 需求发现   代码库探索    架构设计    实施执行     质量验证    价值交付
    ↓           ↓            ↓         ↓            ↓          ↓
 澄清问题    映射架构    多方案对比   TDD执行     全面验证    模式提取
 定义标准    识别模式    权衡分析    两阶段审查   质量门禁    知识沉淀
```

### 核心原则

1. **Evidence Before Claims** - 证据优先于断言
2. **Quality First** - 质量第一
3. **Continuous Learning** - 持续学习

### 核心特点

- **端到端闭环**: 从需求到交付的完整流程
- **质量优先**: 严格的质量门禁和验证（测试覆盖率 ≥ 80%）
- **证据优先**: 所有结论基于验证证据
- **持续学习**: Instincts 自动提取和演化可复用知识
- **Speckit 工作流**: 规范化开发流程（可选）
- **诊断系统**: 整合的调试、诊断、修复能力
- **多语言支持**: Python/Go/C/C++ 全栈开发

---

## 命令参考

### Core Commands (核心命令)

| 命令 | 描述 | 文档 |
|------|------|------|
| `/deliver` | 完整端到端流程 | [详情](docs/commands/README.md#deliver) |
| `/discovery` | 需求发现阶段 | [详情](docs/commands/README.md#discovery) |
| `/design` | 架构设计阶段 | [详情](docs/commands/README.md#design) |

### Workflow Commands (工作流命令)

| 命令 | 描述 | 文档 |
|------|------|------|
| `/speckit-workflow` | Speckit 规范化工作流 | [详情](docs/commands/README.md#speckit-workflow) |
| `/speckit-analyze` | 一致性分析 | [详情](docs/commands/README.md#speckit-analyze) |
| `/speckit-tasks` | 任务依赖管理 | [详情](docs/commands/README.md#speckit-tasks) |

### Utility Commands (工具命令)

| 命令 | 描述 | 文档 |
|------|------|------|
| `/exploration` | 代码库探索 | [详情](docs/commands/README.md#exploration) |
| `/implement` | 实施执行 | [详情](docs/commands/README.md#implement) |
| `/verify` | 质量验证 | [详情](docs/commands/README.md#verify) |
| `/delivery` | 价值交付 | [详情](docs/commands/README.md#delivery) |
| `/speckit-branch` | 智能分支管理 | [详情](docs/commands/README.md#speckit-branch) |
| `/speckit-guard` | 宪法治理检查 | [详情](docs/commands/README.md#speckit-guard) |
| `/speckit-checklist` | 质量检查清单 | [详情](docs/commands/README.md#speckit-checklist) |
| `/diagnose` | 诊断专家 | [详情](docs/commands/README.md#diagnose) |
| `/ui-design` | UI/UX 设计 | [详情](docs/commands/README.md#ui-design) |
| `/instinct-status` | Instincts 状态 | [详情](docs/commands/README.md#instinct-status) |
| `/instinct-export` | 导出 Instincts | [详情](docs/commands/README.md#instinct-export) |
| `/instinct-import` | 导入 Instincts | [详情](docs/commands/README.md#instinct-import) |
| `/evolve` | 演化 Instincts | [详情](docs/commands/README.md#evolve) |

---

## 详细文档

- [完整命令参考](docs/commands/README.md) - 所有命令的详细文档
- [架构设计](docs/architecture.md) - 目录结构和架构说明
- [配置指南](docs/configuration.md) - 安装和配置说明
- [最佳实践](docs/best-practices.md) - 使用建议和技巧
- [变更日志](CHANGELOG.md) - 版本更新记录

---

## Speckit 规范化工作流

可选集成的 Speckit 框架增强功能：

```
Specify → Plan → Tasks → Analyze → Implement
   ↓        ↓       ↓        ↓         ↓
智能分支  宪法检查  任务分解   一致性    TDD执行
```

**核心能力**:
- 智能分支管理 (`/speckit-branch`)
- 宪法治理检查 (`/speckit-guard`)
- 一致性分析 (`/speckit-analyze`)
- 任务依赖管理 (`/speckit-tasks`)
- 质量检查清单 (`/speckit-checklist`)

---

## 质量标准

| 指标 | 标准 |
|------|------|
| 测试覆盖率 | ≥ 80% (语句、分支、函数) |
| 函数长度 | ≤ 50 行 |
| 文件长度 | ≤ 800 行 |
| 嵌套深度 | ≤ 4 层 |

**铁律**: NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE

---

## 目录结构

```
commands/
├── core/           # 核心命令 (3个)
├── workflow/       # 工作流命令 (3个)
└── utility/        # 工具命令 (13个)

agents/             # 9 个代理
skills/             # 17+ 个技能
templates/          # 需求/设计/编码/测试模板
docs/               # 详细文档
```

完整结构请参考 [架构文档](docs/architecture.md)。

---

## 最佳实践

1. **从小开始** - 先在简单功能上实践，逐步增加复杂度
2. **频繁验证** - 每个小步骤后验证，不要等到最后
3. **及时沟通** - 遇到问题及时使用 `/diagnose`
4. **记录决策** - 架构决策自动记录在实施蓝图
5. **持续改进** - 每次交付后使用 `/delivery` 提取模式

更多最佳实践请参考 [最佳实践文档](docs/best-practices.md)。

---

## 贡献

欢迎贡献改进!

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'feat: add AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

---

## 致谢

感谢以下项目的启发:
- [superpowers](https://github.com/obra/superpowers)
- [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
- [claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

---

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

**核心原则**: Evidence Before Claims, Quality First, Continuous Learning

**记住**: 端到端价值交付闭环不是一次性的活动，而是一个持续改进的循环。每一次交付都是学习的机会，每一次学习都让下一次交付更好。
