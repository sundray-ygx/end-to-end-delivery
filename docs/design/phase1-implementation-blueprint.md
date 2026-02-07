# Phase 1: 快速见效 - 实施蓝图

## 文档信息

- **创建时间**: 2025-02-07
- **实施阶段**: Phase 1 - 快速见效
- **预计工期**: 1-2周
- **复杂度等级**: 中等（总分: 9/20）

## 1. 设计任务书

### 1.1 需求跟踪

| 需求ID | 需求描述 | 优先级 | 本阶段覆盖 |
|--------|----------|--------|------------|
| REQ-P0-1 | 插件架构混乱（19个命令导致用户困惑） | P0 | ✅ 完全覆盖 |
| REQ-P0-2 | 功能重叠严重（E2D 和 Speckit 工作流选择困难） | P0 | ⚠️ 部分覆盖 |
| REQ-P0-3 | 文档冗余重复（README 过长 470 行） | P0 | ✅ 完全覆盖 |
| REQ-OPT-1 | 19 个命令 → 3 个核心命令 | P1 | ✅ 完全覆盖 |
| REQ-OPT-2 | 统一 E2D 和 Speckit 为统一框架 | P1 | ⚠️ 部分覆盖 |
| REQ-OPT-3 | README 长度减少 50% | P1 | ✅ 完全覆盖 |
| REQ-OPT-4 | 新用户上手时间减半 | P1 | ✅ 完全覆盖 |

### 1.2 模块整体目标

- **功能目标**: 命令分层组织，用户快速找到所需命令
- **性能目标**: 命令加载时间不受影响（≤ 100ms）
- **资源开销**: 无额外资源消耗
- **安全性**: 保持现有权限控制
- **可靠性**: 100% 向后兼容，现有命令不破坏
- **可维护性**: 清晰的目录结构，易于扩展

## 2. 对外接口

### 2.1 命令接口（保持不变）

所有现有命令接口保持不变，确保向后兼容：

```bash
# Core Commands
/deliver "feature description"
/discovery "feature description"
/design

# Workflow Commands
/speckit-workflow "feature description"
/specify "feature description"
/plan
/tasks
/analyze

# Utility Commands
/exploration
/implement
/verify
/delivery
/speckit-branch "feature description"
/speckit-guard
/speckit-tasks
/speckit-analyze
/speckit-checklist
/ui-design "design brief"
/diagnose "problem description"
/instinct-export
/instinct-import <file>
/instinct-status
/evolve
```

### 2.2 配置接口

插件配置保持不变，仅更新目录结构引用。

## 3. 概要说明

### 3.1 背景描述

#### 3.1.1 工作原理

Claude Code 插件系统通过 `plugin.json` 中的 `"commands": "./commands"` 配置来加载命令。当前所有命令文件平铺在 `commands/` 目录下，导致用户难以理解命令层次关系。

#### 3.1.2 应用场景

- 新用户安装插件后，面对 19 个命令不知所措
- 现有用户需要查找特定命令时，需要浏览所有命令文件
- 维护者需要添加新命令时，不清楚应该放在什么位置

#### 3.1.3 对手分析

**优势**:
- 清晰的命令分层结构
- 降低新用户上手难度
- 提高代码可维护性

**劣势**:
- 需要迁移现有文件
- 可能需要更新文档引用
- 需要充分测试向后兼容性

### 3.2 方案选型

| 方案 | 描述 | 优势 | 劣势 | 评分 |
|------|------|------|------|------|
| A. 虚拟分组（仅README） | 仅在文档中分组，不改变文件结构 | 无风险 | 不解决实际问题 | 3/10 |
| B. 目录重组 | 创建 core/workflow/utility 子目录 | 清晰直观 | 需要迁移文件 | 9/10 |
| C. 命令别名 | 创建简短别名指向完整命令 | 保持兼容 | 增加复杂度 | 6/10 |

**推荐方案**: 方案 B - 目录重组

**理由**:
1. 直接解决核心问题（命令组织混乱）
2. 清晰直观，易于理解
3. 风险可控（充分测试确保兼容性）
4. 为后续阶段打基础

### 3.3 静态结构

```
commands/
├── core/                    # Core Commands (3个)
│   ├── deliver.md
│   ├── discovery.md
│   └── design.md
├── workflow/                # Workflow Commands (5个)
│   ├── speckit-workflow.md
│   ├── specify.md
│   ├── plan.md
│   ├── tasks.md
│   └── analyze.md
└── utility/                 # Utility Commands (11个)
    ├── exploration.md
    ├── implement.md
    ├── verify.md
    ├── delivery.md
    ├── speckit-branch.md
    ├── speckit-guard.md
    ├── speckit-tasks.md
    ├── speckit-analyze.md
    ├── speckit-checklist.md
    ├── ui-design.md
    ├── diagnose.md
    ├── instinct-export.md
    ├── instinct-import.md
    ├── instinct-status.md
    └── evolve.md
```

### 3.4 对插件总体架构的影响

**影响评估**: ✅ 低风险

- **plugin.json**: `"commands": "./commands"` 配置递归搜索子目录
- **现有功能**: 无任何功能变更
- **兼容性**: 100% 向后兼容（Claude Code 自动递归查找命令）
- **文档**: 需要更新 README.md 中的目录结构引用

### 3.5 概要流程

```
开始
  ↓
创建目录结构 (core/workflow/utility)
  ↓
移动命令文件到对应目录
  ↓
更新 README.md 中的目录结构
  ↓
验证命令引用正确性
  ↓
测试所有命令可用性
  ↓
结束
```

### 3.6 关键特性设计

#### 3.6.1 向后兼容性设计

Claude Code 插件系统自动递归搜索 `commands/` 目录下的所有 `*.md` 文件，因此：
- 移动文件后，命令路径自动更新
- 无需修改 `plugin.json`
- 所有命令保持可用

**验证方法**:
```bash
# 测试所有命令是否可用
for cmd in deliver discovery design speckit-workflow specify plan tasks analyze exploration implement verify delivery speckit-branch speckit-guard speckit-tasks speckit-analyze speckit-checklist ui-design diagnose instinct-export instinct-import instinct-status evolve; do
  echo "Testing: /$cmd"
done
```

#### 3.6.2 README 重构设计

**目标**: 将 README 从 470 行减少到 < 250 行

**策略**:
1. **快速开始** (50 行): 3 步上手指南
2. **核心概念** (50 行): 工作流架构 + 核心原则
3. **命令参考** (链接到详细文档): 仅列出命令分类和快速链接
4. **详细文档链接**: 移动详细内容到 `docs/` 目录

**新的 README 结构**:
```markdown
# 端到端价值交付闭环插件

[徽章区]

## 快速开始 (50行)
[安装 + 核心命令]

## 核心概念 (50行)
[工作流架构 + 核心原则]

## 命令参考
### Core Commands
- /deliver - 完整端到端流程 [详情](docs/commands/core.md)
- /discovery - 需求发现 [详情](docs/commands/core.md)
- /design - 架构设计 [详情](docs/commands/core.md)

### Workflow Commands
- /speckit-workflow - Speckit 规范化工作流 [详情](docs/commands/workflow.md)
...

### Utility Commands
- /exploration - 代码库探索 [详情](docs/commands/utility.md)
...

## 详细文档
- [完整命令参考](docs/commands/README.md)
- [配置指南](docs/configuration.md)
- [最佳实践](docs/best-practices.md)

## 贡献 & 许可证
```

### 3.7 方案风险分析

| 风险 | 影响 | 概率 | 缓解措施 |
|------|------|------|----------|
| Claude Code 不支持递归搜索命令 | 高 | 低 | 官方文档确认支持递归搜索 |
| 现有命令引用路径失效 | 中 | 中 | 无影响（命令名不变） |
| README 链接失效 | 中 | 中 | 充分测试所有链接 |
| 用户困惑（文件位置变化） | 低 | 高 | 清晰的迁移说明 |

## 4. 数据结构设计

### 4.1 配置文件定义

**plugin.json** (无变化):
```json
{
  "commands": "./commands"
}
```

### 4.2 全局数据结构定义

无新增数据结构。

## 5. 流程设计

### 5.1 命令重组流程

#### 5.1.1 静态结构

```
Task 1: 命令重组
├── 输入: 现有 19 个命令文件
├── 输出: 分层的目录结构
└── 步骤:
    1. 创建 core/, workflow/, utility/ 目录
    2. 移动命令文件到对应目录
    3. 验证文件完整性
```

#### 5.1.2 处理流程

```bash
# Step 1: 创建目录
mkdir -p commands/core commands/workflow commands/utility

# Step 2: 移动 Core Commands
mv commands/deliver.md commands/core/
mv commands/discovery.md commands/core/
mv commands/design.md commands/core/

# Step 3: 移动 Workflow Commands
mv commands/speckit-workflow.md commands/workflow/
# ... (其他 workflow 命令)

# Step 4: 移动 Utility Commands
mv commands/exploration.md commands/utility/
# ... (其他 utility 命令)

# Step 5: 验证
find commands -name "*.md" | wc -l  # 应该是 19
```

#### 5.1.3 关键算法描述

命令分类算法：
```python
def categorize_command(command_name: str) -> str:
    """根据命令名称确定分类"""
    core_commands = ['deliver', 'discovery', 'design']
    workflow_commands = [
        'speckit-workflow', 'specify', 'plan',
        'tasks', 'analyze'
    ]

    if command_name in core_commands:
        return 'core'
    elif command_name in workflow_commands:
        return 'workflow'
    else:
        return 'utility'
```

#### 5.1.4 数据结构定义

```typescript
interface CommandCategory {
    name: string;
    description: string;
    commands: string[];
}

const categories: CommandCategory[] = [
    {
        name: 'core',
        description: '核心命令 - 端到端流程主要入口',
        commands: ['deliver', 'discovery', 'design']
    },
    {
        name: 'workflow',
        description: '工作流命令 - 规范化开发流程',
        commands: ['speckit-workflow', 'specify', 'plan', 'tasks', 'analyze']
    },
    {
        name: 'utility',
        description: '工具命令 - 辅助和诊断功能',
        commands: ['exploration', 'implement', 'verify', 'delivery', ...]
    }
];
```

#### 5.1.5 函数列表

| 函数 | 描述 |
|------|------|
| `create_directories()` | 创建 core/workflow/utility 目录 |
| `move_command_files()` | 移动命令文件到对应目录 |
| `verify_file_count()` | 验证所有文件已移动 |
| `validate_commands()` | 验证命令可用性 |

#### 5.1.6 设计要点检视

- [x] 目录结构清晰
- [x] 命令分类合理
- [x] 向后兼容性保证
- [x] 可扩展性（未来可添加新分类）

### 5.2 README 重构流程

#### 5.2.1 静态结构

```
Task 2: README 重构
├── 输入: 现有 README.md (470 行)
├── 输出: 新 README.md (<250 行) + 详细文档
└── 步骤:
    1. 提取详细内容到独立文档
    2. 重写 README（精简版）
    3. 创建详细命令参考文档
    4. 验证所有链接
```

#### 5.2.2 处理流程

```markdown
# 新 README.md 结构
1. 标题 + 徽章 (10 行)
2. 快速开始 (50 行)
3. 核心概念 (50 行)
4. 命令参考 (80 行 - 仅列出和链接)
5. 详细文档链接 (20 行)
6. 贡献 & 许可证 (30 行)
---
总计: ~240 行
```

#### 5.2.3 关键算法描述

内容迁移算法：
```python
def migrate_readme_content():
    """将 README 详细内容迁移到 docs/"""
    detailed_sections = [
        '目录结构',
        '质量标准',
        '最佳实践',
        '配置',
        '与其他插件的关系'
    ]

    for section in detailed_sections:
        extract_section_from_readme(section)
        create_doc_file(section)
        replace_section_with_link(section)
```

#### 5.2.4 数据结构定义

```typescript
interface ReadmeSection {
    title: string;
    lines: number;
    action: 'keep' | 'compress' | 'move';
    target?: string;
}

const section_plan: ReadmeSection[] = [
    { title: '概述', lines: 30, action: 'compress', target: '核心概念' },
    { title: '最新特性', lines: 100, action: 'compress', target: '快速开始' },
    { title: '目录结构', lines: 100, action: 'move', target: 'docs/architecture.md' },
    { title: '质量标准', lines: 50, action: 'move', target: 'docs/quality.md' },
    { title: '配置', lines: 30, action: 'move', target: 'docs/configuration.md' },
    { title: '最佳实践', lines: 50, action: 'move', target: 'docs/best-practices.md' },
];
```

#### 5.2.5 函数列表

| 函数 | 描述 |
|------|------|
| `extract_sections()` | 提取需要移动的章节 |
| `create_doc_files()` | 创建详细文档文件 |
| `rewrite_readme()` | 重写 README（精简版） |
| `validate_links()` | 验证所有链接有效 |

#### 5.2.6 设计要点检视

- [x] README 长度目标明确 (<250 行)
- [x] 内容迁移计划完整
- [x] 链接结构清晰
- [x] 保持核心信息可见

## 6. 总结

### 6.1 关联分析

本阶段实施为后续阶段打基础：
- **Phase 2**: 在分层结构基础上实现工作流引擎
- **Phase 3**: 基于新结构实现文档动态生成

### 6.2 遗留问题解决

| 问题 | 解决状态 | 备注 |
|------|----------|------|
| 命令架构混乱 | ✅ Phase 1 解决 | 分层组织 |
| 功能重叠严重 | ⚠️ 部分解决 | Phase 2 完整解决 |
| 文档冗余重复 | ✅ Phase 1 解决 | README 重构 |
| 工作流统一 | ⏳ Phase 2 解决 | 需要工作流引擎 |

## 7. 变更控制

### 7.1 变更列表

| 版本 | 日期 | 变更内容 | 作者 |
|------|------|----------|------|
| v1.0 | 2025-02-07 | 初始版本 | implementation-agent |

---

**技术栈**: Shell, Markdown, JSON
**实施方式**: 文件重组 + 文档重构
**测试策略**: 手动验证所有命令可用性
