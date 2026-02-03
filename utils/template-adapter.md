# 模板适配器 (Template Adapter)

## 概述

模板适配器提供统一的模板维度提取接口，封装复杂度评估、模板选择、维度加载等功能，为各代理提供简单易用的模板维度服务。

## 核心功能

### 1. 自动模式选择

根据复杂度自动选择合适的开发模式和模板。

### 2. 模板维度提取

封装模板加载和维度提取逻辑。

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

获取编码 checklist 并提取审查维度。

```javascript
/**
 * 获取编码 checklist 并提取审查维度
 * @param {string} language - 编程语言
 * @returns {Object} 包含 checklist 路径和审查维度的对象
 */
async function getCodingChecklist(language) {
  const checklistMap = {
    python: 'coding/coding-checklist-python.md',
    go: 'coding/coding-checklist-go.md',
    javascript: 'coding/coding-checklist-js.md',
    typescript: 'coding/coding-checklist-js.md',
    // ... 其他语言
  };

  const checklistPath = checklistMap[language] || 'coding/coding-checklist-generic.md';

  // 加载 checklist 并提取审查维度
  const dimensions = await extractChecklistDimensions(checklistPath);

  return {
    path: checklistPath,
    dimensions: dimensions,
  };
}
```

### 4. getTestingChecklist(language)

获取测试 checklist 并提取审查维度。

```javascript
/**
 * 获取测试 checklist 并提取审查维度
 * @param {string} language - 编程语言
 * @returns {Object} 包含 checklist 路径、审查维度和 Skill 映射的对象
 */
async function getTestingChecklist(language) {
  const checklistMap = {
    python: 'testing/testing-checklist-python.md',
    javascript: 'testing/testing-checklist-js.md',
    typescript: 'testing/testing-checklist-js.md',
    go: 'testing/testing-checklist-go.md',
    java: 'testing/testing-checklist-java.md',
    rust: 'testing/testing-checklist-rust.md',
    c: 'testing/testing-checklist-c-cpp.md',
    cpp: 'testing/testing-checklist-c-cpp.md',
    shell: 'testing/testing-checklist-shell.md',
  };

  const checklistPath = checklistMap[language] || 'testing/testing-checklist-generic.md';

  // 加载 checklist 并提取审查维度
  const dimensions = await extractChecklistDimensions(checklistPath);

  // Skill 映射（立即集成）
  const skillMapping = {
    python: 'python-development:python-testing-patterns',
    javascript: 'javascript-typescript:javascript-testing-patterns',
    typescript: 'javascript-typescript:javascript-testing-patterns',
    shell: 'shell-scripting:bats-testing-patterns',
    // 其他语言暂无对应 skill，使用 checklist
  };

  return {
    path: checklistPath,
    dimensions: dimensions,
    skill: skillMapping[language] || null,
  };
}
```

### 5. renderTemplate(templatePath, variables)

渲染模板（已弃用，保留用于向后兼容）。

**注意**: 新的实现应使用 extractTemplateDimensions() 提取分析维度。

```javascript
/**
 * 渲染模板（已弃用）
 * @param {string} templatePath - 模板路径
 * @param {Object} variables - 模板变量
 * @returns {Promise<string>} 渲染后的内容
 * @deprecated 请使用 extractTemplateDimensions() 提取分析维度
 */
async function renderTemplate(templatePath, variables) {
  return await loadTemplate(templatePath, variables);
}
```

### 6. extractTemplateDimensions(templatePath)

提取模板的分析维度。

**重要**: 支持自动回退到插件默认模板，当本地模板不存在时自动使用插件内置模板。

```javascript
/**
 * 提取模板的分析维度（支持自动回退到插件默认模板）
 * @param {string} templatePath - 模板路径（相对路径）
 * @returns {Promise<Object>} 提取的分析维度
 *
 * 模板查找顺序：
 * 1. 项目根目录/.claude/templates/{templatePath}
 * 2. 项目根目录/templates/{templatePath}
 * 3. 插件目录/templates/{templatePath}（默认回退）
 */
async function extractTemplateDimensions(templatePath) {
  // 使用 template-loader 的 loadTemplate 函数（支持回退）
  const templateContent = await loadTemplateWithFallback(templatePath);

  // 提取分析维度
  const dimensions = parseTemplateDimensions(templateContent);

  return dimensions;
}

/**
 * 加载模板（支持回退到插件默认模板）
 * @param {string} templatePath - 模板相对路径
 * @returns {Promise<string>} 模板内容
 */
async function loadTemplateWithFallback(templatePath) {
  const searchPaths = [
    path.join(process.cwd(), '.claude', 'templates', templatePath),
    path.join(process.cwd(), 'templates', templatePath),
    // 插件默认模板路径
    path.join(PLUGIN_ROOT_DIR, 'templates', templatePath)
  ];

  for (const templateFile of searchPaths) {
    try {
      return await fs.readFile(templateFile, 'utf-8');
    } catch (error) {
      continue; // 继续尝试下一个路径
    }
  }

  throw new TemplateAdapterError('TEMPLATE_NOT_FOUND',
    `无法找到模板文件: ${templatePath}`,
    { searchedPaths: searchPaths });
}
```

### 7. evaluateComplexity(requirements)

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

### 8. detectProjectLanguage(projectPath)

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

### 9. getE2ETestingFramework(projectPath)

检测项目的 E2E 测试框架。

```javascript
/**
 * 检测 E2E 测试框架
 * @param {string} projectPath - 项目路径
 * @returns {Object} 框架信息
 */
async function getE2ETestingFramework(projectPath) {
  // 检测 Playwright
  if (fs.existsSync(path.join(projectPath, 'playwright.config.ts'))) {
    return {
      framework: 'playwright',
      config: 'playwright.config.ts',
      testDir: 'tests/e2e',
      command: 'npx playwright test'
    };
  }

  // 检测 Cypress
  if (fs.existsSync(path.join(projectPath, 'cypress.config.ts'))) {
    return {
      framework: 'cypress',
      config: 'cypress.config.ts',
      testDir: 'cypress/e2e',
      command: 'npx cypress run'
    };
  }

  // 默认推荐 Playwright
  return {
    framework: 'playwright',
    recommended: true,
    installCommand: 'npm install -D @playwright/test'
  };
}
```

### 10. getPerformanceTestingTools()

获取性能测试工具配置。

```javascript
/**
 * 获取性能测试工具配置
 * @returns {Object} 工具配置
 */
async function getPerformanceTestingTools() {
  return {
    primary: {
      name: 'k6',
      install: {
        macos: 'brew install k6',
        linux: 'curl https://github.com/grafana/k6/releases/download/v0.47.0/k6-v0.47.0-linux-amd64.tar.gz -L | tar xvz'
      },
      config: 'k6/config',
      tests: 'k6/tests'
    },
    secondary: {
      name: 'JMeter',
      description: '用于复杂性能测试场景',
      install: '从 https://jmeter.apache.org/download_jmeter.cgi 下载'
    },
    profiling: {
      cpu: 'perf, flamegraph',
      memory: 'heapdump, valgrind',
      network: 'wireshark, tcpdump'
    }
  };
}
```

### 11. extractTestCasesFromDesign(designDoc)

从设计文档提取测试用例。

```javascript
/**
 * 从设计文档提取业务逻辑测试用例
 * @param {string} designDoc - 设计文档路径
 * @returns {Array} 测试用例列表
 */
async function extractTestCasesFromDesign(designDoc) {
  const content = await fs.readFile(designDoc, 'utf-8');

  // 提取 "业务逻辑相关的测试用例" 章节
  const testCasesSection = extractSection(content, '业务逻辑相关的测试用例');

  // 解析测试用例
  const testCases = parseTestCases(testCasesSection);

  return testCases;
}
```

### 12. extractUserStoriesFromDiscovery(discoveryDoc)

从需求文档提取 User Story 验收标准。

```javascript
/**
 * 从需求文档提取 User Story 验收标准
 * @param {string} discoveryDoc - 需求文档路径
 * @returns {Array} User Stories with Given-When-Then
 */
async function extractUserStoriesFromDiscovery(discoveryDoc) {
  const content = await fs.readFile(discoveryDoc, 'utf-8');

  // 提取 Story 章节的 A/C 验收条件
  const stories = extractStories(content);

  // 解析 Given-When-Then
  return stories.map(story => ({
    title: story.title,
    userStory: story.userStory,
    acceptanceCriteria: {
      given: story.given,
      when: story.when,
      then: story.then
    }
  }));
}
```

### 13. getBlackboxTestingChecklist()

获取黑盒测试 checklist。

```javascript
/**
 * 获取黑盒测试 checklist
 * @returns {Object} 黑盒测试维度
 */
async function getBlackboxTestingChecklist() {
  const checklistPath = 'templates/testing/blackbox-testing-checklist.md';

  // 加载 checklist 并提取审查维度
  const dimensions = await extractChecklistDimensions(checklistPath);

  return {
    path: checklistPath,
    dimensions: dimensions,
  };
}
```

## 使用示例

### 示例 1: Discovery Agent 使用

```javascript
// 在 Discovery Agent 中使用

async function analyzeRequirements(requirements) {
  // 1. 评估复杂度
  const complexity = await templateAdapter.evaluateComplexity(requirements);

  // 2. 获取需求模板并提取分析维度
  const templateInfo = await templateAdapter.getRequirementsTemplate(complexity.level);

  // 3. 基于模板维度进行深度需求分析
  const dimensions = [];
  for (const templatePath of templateInfo.templates) {
    const dimension = await templateAdapter.extractTemplateDimensions(templatePath);
    dimensions.push(dimension);
  }

  return {
    mode: templateInfo.mode,
    complexity: complexity,
    dimensions: dimensions,
  };
}
```

### 示例 2: Design Agent 使用

```javascript
// 在 Design Agent 中使用

async function analyzeDesign(requirements, design) {
  // 1. 获取复杂度（来自 Discovery Agent）
  const complexity = requirements.complexity;

  // 2. 获取设计模板并提取分析维度
  const templateInfo = await templateAdapter.getDesignTemplate(complexity.level);

  // 3. 基于模板维度进行深度架构设计分析
  const dimensions = await templateAdapter.extractTemplateDimensions(templateInfo.template);

  // 4. 如果需要模块拆分
  if (templateInfo.needsModuleBreakdown) {
    const modules = await analyzeModuleDesigns(design.modules);
    return {
      dimensions,
      modules,
    };
  }

  return { dimensions };
}
```

### 示例 3: Implementation Agent 使用

```javascript
// 在 Implementation Agent 中使用

async function applyCodingStandards(projectPath) {
  // 1. 检测项目语言
  const language = await templateAdapter.detectProjectLanguage(projectPath);

  // 2. 获取编码 checklist 并提取审查维度
  const checklistInfo = await templateAdapter.getCodingChecklist(language);

  // 3. 基于checklist维度进行深度代码审查
  const reviewResults = await reviewCodeByDimensions(projectPath, checklistInfo.dimensions);

  return {
    language,
    dimensions: checklistInfo.dimensions,
    reviewResults,
  };
}
```

### 示例 4: Implementation Agent 测试维度审查使用

```javascript
// 在 Implementation Agent 中进行测试维度审查

async function applyTestingPatterns(projectPath) {
  // 1. 检测项目语言
  const language = await templateAdapter.detectProjectLanguage(projectPath);

  // 2. 获取测试 checklist 并提取审查维度
  const testingChecklist = await templateAdapter.getTestingChecklist(language);

  // 3. 如果有对应的 Skill，调用获取最佳实践
  let bestPractices = null;
  if (testingChecklist.skill) {
    bestPractices = await callSkill(testingChecklist.skill);
  }

  // 4. 基于测试维度进行深度测试审查
  const testReviewResults = await reviewTestsByDimensions(
    projectPath,
    testingChecklist.dimensions,
    bestPractices
  );

  return {
    language,
    dimensions: testingChecklist.dimensions,
    skill: testingChecklist.skill,
    bestPractices,
    reviewResults: testReviewResults,
  };
}
```

### 示例 5: Verification Agent 使用

```javascript
// 在 Verification Agent 中使用

async function verifyDimensionCoverage(document, expectedTemplate) {
  // 1. 加载预期模板并提取维度
  const templateDimensions = await templateAdapter.extractTemplateDimensions(expectedTemplate);

  // 2. 验证文档维度覆盖度
  const result = verifyDimensionCoverageInDocument(document, templateDimensions);

  return result;
}
```

### 示例 6: Delivery Agent 使用

```javascript
// 在 Delivery Agent 中使用

async function generateDeliverySummary(phaseAnalysis) {
  // 1. 基于各阶段维度分析成果生成交付总结
  const summary = {
    discovery: phaseAnalysis.discovery.dimensions,
    design: phaseAnalysis.design.dimensions,
    implementation: phaseSearch.implementation.dimensions,
    verification: phaseSearch.verification.dimensions,
  };

  // 2. 生成端到端价值交付总结报告
  const report = generateEndToEndSummary(summary);

  return report;
}
```

### 示例 7: Verification Agent 黑盒测试使用

```javascript
// 在 Verification Agent 中进行黑盒测试验证

async function verifyBlackboxTests(projectPath) {
  // 1. 检测 E2E 测试框架
  const e2eFramework = await templateAdapter.getE2ETestingFramework(projectPath);

  // 2. 获取性能测试工具配置
  const perfTools = await templateAdapter.getPerformanceTestingTools();

  // 3. 获取黑盒测试 checklist 并提取审查维度
  const blackboxChecklist = await templateAdapter.getBlackboxTestingChecklist();

  // 4. 从 Discovery 阶段提取 User Stories（用于 E2E 测试）
  const discoveryDoc = path.join(projectPath, 'docs/01_需求发现报告.md');
  const userStories = await templateAdapter.extractUserStoriesFromDiscovery(discoveryDoc);

  // 5. 从 Design 阶段提取测试用例（用于集成测试）
  const designDoc = path.join(projectPath, 'docs/02_设计分析报告.md');
  const testCases = await templateAdapter.extractTestCasesFromDesign(designDoc);

  // 6. 基于黑盒测试维度进行深度审查
  const blackboxReviewResults = await reviewBlackboxTestsByDimensions(
    projectPath,
    blackboxChecklist.dimensions,
    {
      e2eFramework,
      perfTools,
      userStories,
      testCases
    }
  );

  return {
    e2eFramework,
    perfTools,
    userStories,
    testCases,
    reviewResults: blackboxReviewResults,
  };
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

使用模板适配器增强需求分析：

1. **复杂度评估**: 调用 `evaluateComplexity()` 评估需求复杂度
2. **模板选择**: 根据复杂度自动选择合适的模板
3. **维度分析**: 使用 `extractTemplateDimensions()` 提取分析维度并进行深度分析
```

### Design Agent

```javascript
// 在 design-agent.md 中添加

## 工具集成

使用模板适配器增强设计分析：

1. **模板获取**: 调用 `getDesignTemplate()` 获取设计模板
2. **维度提取**: 使用 `extractTemplateDimensions()` 提取设计维度
3. **维度分析**: 基于提取的维度进行深度架构设计分析
```

### Implementation Agent

```javascript
// 在 implementation-agent.md 中添加

## 工具集成

使用模板适配器增强编码规范审查：

1. **语言检测**: 调用 `detectProjectLanguage()` 检测项目语言
2. **Checklist 加载**: 调用 `getCodingChecklist()` 获取编码规范并提取审查维度
3. **维度审查**: 基于checklist维度进行深度代码审查

使用模板适配器增强测试维度审查：

1. **语言检测**: 调用 `detectProjectLanguage()` 检测项目语言
2. **测试 Checklist 加载**: 调用 `getTestingChecklist()` 获取测试规范并提取审查维度
3. **Skill 集成**: 如果有对应的 testing-patterns skill，自动调用获取最佳实践
4. **测试维度审查**: 基于测试checklist维度进行深度测试审查
```

### Verification Agent

```javascript
// 在 verification-agent.md 中添加

## 工具集成

使用模板适配器验证维度覆盖度：

1. **模板验证**: 验证输出文档是否覆盖了模板提供的维度
2. **维度检查**: 检查文档维度的完整性
3. **覆盖度报告**: 生成维度覆盖度验证报告
```

### Delivery Agent

```javascript
// 在 delivery-agent.md 中添加

## 工具集成

使用模板适配器生成交付总结：

1. **维度汇总**: 汇总各阶段的维度分析成果
2. **价值总结**: 基于维度分析生成端到端价值交付总结
3. **模式提取**: 提取符合企业标准的价值模式
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
