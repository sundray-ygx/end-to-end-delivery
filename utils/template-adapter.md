# 模板适配器 (Template Adapter)

## 概述

模板适配器提供统一的模板调用接口，封装复杂度评估、模板选择、模板加载等功能，为各代理提供简单易用的模板服务。

## 核心功能

### 1. 自动模式选择

根据复杂度自动选择合适的开发模式和模板。

### 2. 模板加载与渲染

封装模板加载和变量替换逻辑。

### 3. 缓存管理

管理模板缓存，提高性能。

### 4. 错误处理

统一处理模板相关的错误。

## API 接口

### 1. getRequirementsTemplate(complexity)

获取需求模板。

```javascript
/**
 * 获取需求模板
 * @param {string} complexity - 复杂度等级 (high/medium/low)
 * @returns {Object} 模板信息
 */
async function getRequirementsTemplate(complexity) {
  const mode = complexity === 'high' ? 'waterfall' : 'agile';

  if (mode === 'waterfall') {
    return {
      mode: 'waterfall',
      templates: [
        'requirements/waterfall/user-requirements-spec-v2.2.md',
        'requirements/waterfall/system-requirements-spec-v3.9.md',
      ],
    };
  } else {
    return {
      mode: 'agile',
      templates: [
        'requirements/agile/Epic.md',
        'requirements/agile/Feature.md',
        'requirements/agile/Story.md',
      ],
    };
  }
}
```

### 2. getDesignTemplate(complexity)

获取设计模板。

```javascript
/**
 * 获取设计模板
 * @param {string} complexity - 复杂度等级 (high/medium/low)
 * @returns {Object} 模板信息
 */
async function getDesignTemplate(complexity) {
  const templateMap = {
    high: 'design/overall-design-spec-v4.1.md',
    medium: 'design/module-detailed-design-spec-v3.6.md',
    low: 'design/module-mini-design-spec-v1.4.md',
  };

  return {
    template: templateMap[complexity],
    needsModuleBreakdown: complexity === 'high',
  };
}
```

### 3. getCodingChecklist(language)

获取编码 checklist。

```javascript
/**
 * 获取编码 checklist
 * @param {string} language - 编程语言
 * @returns {string} Checklist 模板路径
 */
async function getCodingChecklist(language) {
  const checklistMap = {
    python: 'coding/coding-checklist-python.md',
    go: 'coding/coding-checklist-go.md',
    javascript: 'coding/coding-checklist-js.md',
    typescript: 'coding/coding-checklist-js.md',
    // ... 其他语言
  };

  return checklistMap[language] || 'coding/coding-checklist-generic.md';
}
```

### 4. renderTemplate(templatePath, variables)

渲染模板。

```javascript
/**
 * 渲染模板
 * @param {string} templatePath - 模板路径
 * @param {Object} variables - 模板变量
 * @returns {Promise<string>} 渲染后的内容
 */
async function renderTemplate(templatePath, variables) {
  return await loadTemplate(templatePath, variables);
}
```

### 5. evaluateComplexity(requirements)

评估需求复杂度。

```javascript
/**
 * 评估需求复杂度
 * @param {Object} requirements - 需求信息
 * @returns {Promise<Object>} 复杂度评估结果
 */
async function evaluateComplexity(requirements) {
  // 调用复杂度评估工具
  const result = await evaluate(requirements);

  return {
    level: result.level,        // 'high', 'medium', 'low'
    score: result.score,        // 综合得分
    mode: result.mode,          // 'waterfall', 'agile'
    details: result.details,    // 各维度得分
  };
}
```

### 6. detectProjectLanguage(projectPath)

检测项目语言。

```javascript
/**
 * 检测项目语言
 * @param {string} projectPath - 项目路径
 * @returns {Promise<string>} 检测到的语言
 */
async function detectProjectLanguage(projectPath) {
  return await detectLanguage(projectPath);
}
```

## 使用示例

### 示例 1: Discovery Agent 使用

```javascript
// 在 Discovery Agent 中使用

async function generateRequirementsDocument(requirements) {
  // 1. 评估复杂度
  const complexity = await templateAdapter.evaluateComplexity(requirements);

  // 2. 获取需求模板
  const templateInfo = await templateAdapter.getRequirementsTemplate(complexity.level);

  // 3. 渲染模板
  const documents = [];
  for (const templatePath of templateInfo.templates) {
    const content = await templateAdapter.renderTemplate(templatePath, {
      projectName: requirements.projectName,
      requirementDescription: requirements.description,
      // ... 其他变量
    });
    documents.push(content);
  }

  return {
    mode: templateInfo.mode,
    complexity: complexity,
    documents,
  };
}
```

### 示例 2: Design Agent 使用

```javascript
// 在 Design Agent 中使用

async function generateDesignDocument(requirements, design) {
  // 1. 获取复杂度（来自 Discovery Agent）
  const complexity = requirements.complexity;

  // 2. 获取设计模板
  const templateInfo = await templateAdapter.getDesignTemplate(complexity.level);

  // 3. 渲染模板
  const document = await templateAdapter.renderTemplate(templateInfo.template, {
    moduleName: design.moduleName,
    architecture: design.architecture,
    // ... 其他变量
  });

  // 4. 如果需要模块拆分
  if (templateInfo.needsModuleBreakdown) {
    const modules = await generateModuleDesigns(design.modules);
    return {
      document,
      modules,
    };
  }

  return { document };
}
```

### 示例 3: Implementation Agent 使用

```javascript
// 在 Implementation Agent 中使用

async function applyCodingStandards(projectPath) {
  // 1. 检测项目语言
  const language = await templateAdapter.detectProjectLanguage(projectPath);

  // 2. 获取编码 checklist
  const checklistPath = await templateAdapter.getCodingChecklist(language);

  // 3. 加载 checklist
  const checklist = await templateAdapter.renderTemplate(checklistPath, {});

  // 4. 应用编码规范
  await applyChecklist(projectPath, checklist, language);

  return {
    language,
    checklist,
  };
}
```

### 示例 4: Verification Agent 使用

```javascript
// 在 Verification Agent 中使用

async function verifyDocumentFormat(document, expectedTemplate) {
  // 1. 加载预期模板
  const template = await loadTemplateFile(expectedTemplate);

  // 2. 提取模板结构
  const structure = extractTemplateStructure(template);

  // 3. 验证文档结构
  const result = verifyStructure(document, structure);

  return result;
}
```

### 示例 5: Delivery Agent 使用

```javascript
// 在 Delivery Agent 中使用

async function generateDeliveryDocuments(deliveryInfo) {
  // 1. 获取交付模板
  const templatePath = 'templates/delivery/delivery-report.md';

  // 2. 渲染模板
  const document = await templateAdapter.renderTemplate(templatePath, {
    projectName: deliveryInfo.projectName,
    version: deliveryInfo.version,
    changes: deliveryInfo.changes,
    // ... 其他变量
  });

  return document;
}
```

## 配置管理

### 初始化配置

```javascript
const templateAdapter = new TemplateAdapter({
  templatesPath: 'templates',
  cacheEnabled: true,
  validateOnLoad: true,
  fallbackToDefault: true,
  customPath: '.claude/templates',
});
```

### 运行时配置

```javascript
// 更新配置
templateAdapter.updateConfig({
  cacheEnabled: false,
});

// 获取当前配置
const config = templateAdapter.getConfig();
```

## 错误处理

### 统一错误格式

```javascript
class TemplateAdapterError extends Error {
  constructor(code, message, details) {
    super(message);
    this.code = code;
    this.details = details;
  }
}

// 错误代码
const ErrorCodes = {
  TEMPLATE_NOT_FOUND: 'TEMPLATE_NOT_FOUND',
  MISSING_VARIABLE: 'MISSING_VARIABLE',
  INVALID_TEMPLATE: 'INVALID_TEMPLATE',
  EVALUATION_FAILED: 'EVALUATION_FAILED',
  LANGUAGE_DETECTION_FAILED: 'LANGUAGE_DETECTION_FAILED',
};
```

### 错误处理示例

```javascript
try {
  const document = await templateAdapter.renderTemplate(templatePath, variables);
} catch (error) {
  if (error.code === 'TEMPLATE_NOT_FOUND') {
    console.error(`模板文件不存在: ${error.details.templatePath}`);
    // 使用默认模板或返回错误
  } else if (error.code === 'MISSING_VARIABLE') {
    console.error(`缺少必需变量: ${error.details.variable}`);
    // 提示用户提供变量
  } else {
    console.error(`模板适配器错误: ${error.message}`);
  }
}
```

## 缓存策略

### 模板缓存

```javascript
class TemplateCache {
  constructor(maxSize = 100) {
    this.cache = new Map();
    this.maxSize = maxSize;
  }

  get(key) {
    return this.cache.get(key);
  }

  set(key, value) {
    if (this.cache.size >= this.maxSize) {
      // 删除最早的缓存项
      const firstKey = this.cache.keys().next().value;
      this.cache.delete(firstKey);
    }
    this.cache.set(key, value);
  }

  clear() {
    this.cache.clear();
  }
}
```

### 缓存使用

```javascript
const templateCache = new TemplateCache();

async function loadTemplateWithCache(templatePath) {
  // 检查缓存
  const cached = templateCache.get(templatePath);
  if (cached) {
    return cached;
  }

  // 加载模板
  const content = await fs.readFile(templatePath, 'utf-8');
  templateCache.set(templatePath, content);

  return content;
}
```

## 与代理集成

### Discovery Agent

```javascript
// 在 discovery-agent.md 中添加

## 工具集成

使用模板适配器增强需求输出：

1. **复杂度评估**: 调用 `evaluateComplexity()` 评估需求复杂度
2. **模板选择**: 根据复杂度自动选择合适的模板
3. **文档生成**: 使用 `renderTemplate()` 生成标准化文档
```

### Design Agent

```javascript
// 在 design-agent.md 中添加

## 工具集成

使用模板适配器增强设计输出：

1. **模板获取**: 调用 `getDesignTemplate()` 获取设计模板
2. **文档渲染**: 使用 `renderTemplate()` 渲染设计文档
3. **模块拆分**: 高复杂度时自动进行模块拆分
```

### Implementation Agent

```javascript
// 在 implementation-agent.md 中添加

## 工具集成

使用模板适配器增强编码规范：

1. **语言检测**: 调用 `detectProjectLanguage()` 检测项目语言
2. **Checklist 加载**: 调用 `getCodingChecklist()` 获取编码规范
3. **规范检查**: 在编码过程中检查清单项
```

### Verification Agent

```javascript
// 在 verification-agent.md 中添加

## 工具集成

使用模板适配器验证文档格式：

1. **模板验证**: 验证输出文档是否符合模板格式
2. **结构检查**: 检查文档结构的完整性
3. **格式报告**: 生成格式验证报告
```

### Delivery Agent

```javascript
// 在 delivery-agent.md 中添加

## 工具集成

使用模板适配器生成标准化文档：

1. **模板选择**: 根据交付类型选择合适的模板
2. **文档生成**: 使用 `renderTemplate()` 生成标准化文档
3. **格式验证**: 验证生成的文档格式
```

## 最佳实践

1. **统一接口**: 所有代理通过模板适配器调用模板功能
2. **错误处理**: 统一处理模板相关错误
3. **缓存管理**: 合理使用缓存提高性能
4. **配置管理**: 支持灵活的配置选项
5. **扩展性**: 易于添加新的模板和功能

## 配置文件示例

```json
{
  "templateAdapter": {
    "enabled": true,
    "templatesPath": "templates",
    "cacheEnabled": true,
    "cacheMaxSize": 100,
    "validateOnLoad": true,
    "fallbackToDefault": true,
    "customPath": ".claude/templates",
    "complexity": {
      "thresholds": {
        "high": 12,
        "medium": 8
      },
      "weights": {
        "functional": 1.0,
        "technical": 1.2,
        "scale": 1.0,
        "risk": 1.5
      }
    },
    "languageDetection": {
      "methods": ["fileExtension", "configFile"],
      "ignorePatterns": ["node_modules/**", "dist/**"]
    }
  }
}
```
