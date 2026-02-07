# 配置指南

## 安装

### 1. 插件安装

插件通过本地插件方式安装：

```bash
# 实际运行位置
~/.claude/plugins/cache/local-plugins/end-to-end-delivery/

# 源位置
~/.claude/plugins/marketplaces/end-to-end-delivery/
```

### 2. 权限配置

在 `.claude/settings.local.json` 中添加技能权限：

```json
{
  "permissions": {
    "allow": [
      "Skill(end-to-end-delivery:ui-design)",
      "Skill(end-to-end-delivery:diagnostic-pro)",
      "Skill(end-to-end-delivery:continuous-learning-v2)",
      "Skill(end-to-end-delivery:eval-harness)",
      "Skill(end-to-end-delivery:python-patterns)",
      "Skill(end-to-end-delivery:python-testing)",
      "Skill(end-to-end-delivery:golang-patterns)",
      "Skill(end-to-end-delivery:golang-testing)",
      "Skill(end-to-end-delivery:c-cpp-patterns)",
      "Skill(end-to-end-delivery:c-cpp-testing)",
      "Skill(end-to-end-delivery:speckit-workflow)",
      "Skill(end-to-end-delivery:speckit-branch)",
      "Skill(end-to-end-delivery:speckit-guard)",
      "Skill(end-to-end-delivery:speckit-tasks)",
      "Skill(end-to-end-delivery:speckit-analyze)",
      "Skill(end-to-end-delivery:speckit-checklist)",
      "Skill(end-to-end-delivery:end-to-end-workflow)",
      "Skill(end-to-end-delivery:template-adapter)"
    ]
  }
}
```

## 配置选项

### Instinct 学习配置

`skills/continuous-learning-v2/config.json`:

```json
{
  "enabled": true,
  "autoExport": false,
  "maxInstincts": 1000,
  "minConfidence": 0.3
}
```

### 模板路径配置

`utils/template-adapter.md`:

```yaml
templatePaths:
  requirements: "./templates/requirements"
  design: "./templates/design"
  coding: "./templates/coding"
  testing: "./templates/testing"
  documentation: "./templates/documentation"
```

## 环境变量

支持以下环境变量（可选）：

```bash
# Instinct 数据目录
export E2D_INSTINCT_DIR="$HOME/.e2d/instincts"

# 模板目录
export E2D_TEMPLATE_DIR="$HOME/.e2d/templates"

# 日志级别
export E2D_LOG_LEVEL="info"
```

## 质量标准配置

### 测试覆盖率

默认要求：**≥ 80%**

可在项目级配置中调整（不推荐）：

```json
{
  "quality": {
    "minCoverage": 80,
    "minBranchCoverage": 80,
    "minFunctionCoverage": 80
  }
}
```

### 代码质量标准

| 指标 | 标准 |
|------|------|
| 函数长度 | ≤ 50 行 |
| 文件长度 | ≤ 800 行 |
| 嵌套深度 | ≤ 4 层 |

## 最佳实践配置

### 1. 项目初始化

```bash
# 创建项目目录
mkdir my-project && cd my-project

# 初始化 Git
git init

# 配置 E2D
mkdir -p .claude
cat > .claude/settings.local.json << EOF
{
  "permissions": {
    "allow": ["Skill(end-to-end-delivery:*)"]
  }
}
EOF
```

### 2. 持续学习配置

```bash
# 启用自动观察
mkdir -p .git/hooks
cp ~/.claude/plugins/marketplaces/end-to-end-delivery/skills/continuous-learning-v2/hooks/observe.sh .git/hooks/post-commit

# 确保可执行
chmod +x .git/hooks/post-commit
```

### 3. Speckit 配置

对于使用 Speckit 工作流的项目：

```bash
# 创建 Speckit 配置
cat > .speckit.yaml << EOF
project:
  name: "My Project"
  version: "1.0.0"

workflow:
  type: "speckit"
  phases:
    - specify
    - plan
    - tasks
    - analyze
    - implement

quality:
  minConfidence: 0.7
  requireConsistency: true
EOF
```

## 故障排除

### 命令未找到

确保：
1. `plugin.json` 中的 `commands` 路径正确
2. 命令文件在正确的目录（core/workflow/utility）
3. 文件扩展名是 `.md`

### 技能未加载

检查：
1. `settings.local.json` 权限配置
2. `plugin.json` 中的 `skills` 路径
3. 技能目录中有 `SKILL.md` 文件

### Instincts 未更新

确认：
1. Git hook 已正确安装
2. `observe.sh` 有执行权限
3. `.e2d/instincts/` 目录可写
