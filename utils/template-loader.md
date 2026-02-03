# 模板加载工具 (Template Loader)

## 概述

模板加载工具负责读取、解析、渲染本地模板文件，支持变量替换和模板继承，为各代理提供标准化的文档输出格式。

## 模板目录结构

```
{项目根目录}/templates/
├── requirements/           # 需求模板
│   ├── waterfall/         # 瀑布流模式
│   │   ├── user-requirements-spec-v2.2.md
│   │   └── system-requirements-spec-v3.9.md
│   └── agile/             # 敏捷模式
│       ├── Epic.md
│       ├── Feature.md
│       ├── Story.md
│       ├── Tech.md
│       └── Task.md
├── design/                # 设计模板
│   ├── overall-design-spec-v4.1.md
│   ├── module-detailed-design-spec-v3.6.md
│   └── module-mini-design-spec-v1.4.md
└── coding/                # 编码 checklist
    ├── coding-checklist-python.md
    ├── coding-checklist-go.md
    ├── coding-checklist-js.md
    └── ...
```

## 模板选择逻辑

### 需求模板选择

| 复杂度 | 开发模式 | 用户需求模板 | 系统需求模板 |
|--------|---------|-------------|-------------|
| 高 | 瀑布流 | user-requirements-spec-v2.2.md | system-requirements-spec-v3.9.md |
| 中/低 | 敏捷 | Epic.md → Feature.md → Story.md | - |

### 设计模板选择

| 复杂度 | 设计模板 |
|--------|---------|
| 高 | overall-design-spec-v4.1.md + 模块拆分 |
| 中 | module-detailed-design-spec-v3.6.md |
| 低 | module-mini-design-spec-v1.4.md |

### 编码模板选择

| 语言 | Checklist 模板 | 检测规则 |
|------|---------------|---------|
| Python | coding-checklist-python.md | .py 文件 |
| Go | coding-checklist-go.md | .go 文件 |
| JavaScript/TypeScript | coding-checklist-js.md | .js, .ts 文件 |
| C/C++ | coding-checklist-c-cpp.md | .c, .cpp, .h 文件 |
| Shell | coding-checklist-shell.md | .sh 文件 |

## 模板变量语法

### 基础变量

使用 `{{variableName}}` 语法插入变量：

```markdown
# {{projectName}} 需求规格

## 需求概述
{{requirementDescription}}

## 目标用户
{{targetUsers}}
```

### 条件渲染

```markdown
{{#if isHighComplexity}}
## 风险分析
{{riskAnalysis}}
{{/if}}
```

### 循环渲染

```markdown
## 功能列表
{{#each features}}
- {{name}}: {{description}}
{{/each}}
```

### 默认值

```markdown
{{version="1.0.0"}}
{{author="Unknown"}}
```

## 模板渲染 API

### loadTemplate(templatePath, variables)

加载并渲染模板。

**重要**: 此函数实现了模板回退机制，当本地模板不存在时自动使用插件默认模板。

```javascript
/**
 * 加载并渲染模板（支持自动回退到插件默认模板）
 * @param {string} templatePath - 模板文件路径（相对路径）
 * @param {Object} variables - 模板变量
 * @returns {Promise<string>} 渲染后的内容
 *
 * 模板查找顺序：
 * 1. 项目根目录/.claude/templates/{templatePath}
 * 2. 项目根目录/templates/{templatePath}
 * 3. 插件目录/templates/{templatePath}（默认回退）
 */
async function loadTemplate(templatePath, variables) {
  const searchPaths = [
    path.join(process.cwd(), '.claude', 'templates', templatePath),
    path.join(process.cwd(), 'templates', templatePath),
    // 插件默认模板路径（通过环境变量或配置获取）
    path.join(PLUGIN_ROOT_DIR, 'templates', templatePath)
  ];

  // 依次尝试读取模板文件
  for (const templateFile of searchPaths) {
    try {
      const content = await fs.readFile(templateFile, 'utf-8');
      return renderTemplate(content, variables);
    } catch (error) {
      // 继续尝试下一个路径
      continue;
    }
  }

  // 所有路径都失败，抛出错误
  throw new TemplateLoaderError('TEMPLATE_NOT_FOUND',
    `无法找到模板文件: ${templatePath}`,
    { searchedPaths: searchPaths });
}
```

### getTemplatePath(category, type, complexity)

根据类别、类型、复杂度获取模板路径。

```javascript
/**
 * 获取模板路径
 * @param {string} category - 模板类别 (requirements/design/coding)
 * @param {string} type - 模板类型
 * @param {string} complexity - 复杂度等级 (high/medium/low)
 * @returns {string} 模板文件路径
 */
function getTemplatePath(category, type, complexity) {
  // 实现模板选择逻辑
}
```

### validateTemplate(templatePath)

验证模板文件是否存在且格式正确。

```javascript
/**
 * 验证模板文件
 * @param {string} templatePath - 模板文件路径
 * @returns {boolean} 模板是否有效
 */
function validateTemplate(templatePath) {
  // 1. 检查文件是否存在
  // 2. 检查文件格式
  // 3. 检查必需变量
  // 4. 返回验证结果
}
```

## 使用示例

### 示例 1: 渲染需求模板

```javascript
// 瀑布流模式 - 用户需求规格
const userRequirements = await loadTemplate(
  'requirements/waterfall/user-requirements-spec-v2.2.md',
  {
    projectName: '用户认证系统',
    version: '1.0.0',
    author: '张三',
    requirementDescription: '实现完整的用户认证功能...',
    targetUsers: '企业用户',
    // ... 其他变量
  }
);
```

### 示例 2: 渲染敏捷需求模板

```javascript
// 敏捷模式 - Epic
const epic = await loadTemplate(
  'requirements/agile/Epic.md',
  {
    title: '用户认证',
    painPoints: ['无统一认证', '安全性不足'],
    value: '提升安全性和用户体验',
    targetUsers: '企业用户',
    background: '现状描述...',
    solution: '方案描述...',
    mvp: '核心功能列表',
    metrics: '成效指标',
    workload: '3人月',
    risks: '风险列表',
    dependencies: '依赖列表'
  }
);
```

### 示例 3: 渲染设计模板

```javascript
// 总体设计
const overallDesign = await loadTemplate(
  'design/overall-design-spec-v4.1.md',
  {
    moduleName: '用户认证系统',
    version: '1.0.0',
    architect: '李四',
    background: '背景描述',
    designGoals: '设计目标',
    externalInterface: '对外接口',
    architectureOverview: '架构概述',
    moduleDecomposition: '模块分解',
    dataFlow: '数据流',
    keyFeatures: '关键特性',
    riskAnalysis: '风险分析',
    // ... 其他变量
  }
);
```

## 模板缓存

为了提高性能，已加载的模板会被缓存：

```javascript
const templateCache = new Map();

async function loadTemplateWithCache(templatePath, variables) {
  // 检查缓存
  if (templateCache.has(templatePath)) {
    const template = templateCache.get(templatePath);
    return renderTemplate(template, variables);
  }

  // 加载模板
  const content = await fs.readFile(templatePath, 'utf-8');
  templateCache.set(templatePath, content);

  return renderTemplate(content, variables);
}
```

## 自定义模板

### 用户自定义模板

用户可以在项目目录下创建自定义模板：

```
{项目}/.claude/templates/
├── requirements/
│   └── custom-requirements.md
├── design/
│   └── custom-design.md
└── coding/
    └── custom-checklist.md
```

### 模板优先级

1. 用户自定义模板 (`.claude/templates/`)
2. 项目模板 (`templates/`)
3. 插件默认模板

## 模板验证

### 必需变量检查

每个模板应声明必需的变量：

```markdown
---
required:
  - projectName
  - version
  - author
---
```

加载时会检查必需变量是否提供。

### 模板格式检查

- 检查 Markdown 语法
- 检查变量语法
- 检查条件/循环语法

## 错误处理

```javascript
try {
  const content = await loadTemplate(templatePath, variables);
} catch (error) {
  if (error.code === 'TEMPLATE_NOT_FOUND') {
    console.error(`模板文件不存在: ${templatePath}`);
    // 使用默认模板或返回错误
  } else if (error.code === 'MISSING_VARIABLE') {
    console.error(`缺少必需变量: ${error.variable}`);
    // 提示用户提供变量
  } else {
    console.error(`模板加载失败: ${error.message}`);
  }
}
```

## 配置选项

```json
{
  "templates": {
    "path": "templates",
    "cache": true,
    "validate": true,
    "fallbackToDefault": true,
    "customPath": ".claude/templates"
  }
}
```

## 与代理集成

- **Discovery Agent**: 加载需求模板，输出结构化需求文档
- **Design Agent**: 加载设计模板，输出架构设计文档
- **Implementation Agent**: 加载编码 checklist，提供编码规范
- **Verification Agent**: 使用模板验证输出文档格式
- **Delivery Agent**: 加载交付模板，生成标准化交付文档

## 最佳实践

1. **模板复用**: 尽量复用现有模板，避免重复创建
2. **变量命名**: 使用清晰、一致的变量命名规范
3. **模板版本**: 模板文件名包含版本号，便于管理
4. **模板文档**: 为复杂模板提供使用文档
5. **模板测试**: 定期测试模板渲染是否正确
