# 语言检测工具 (Language Detector)

## 概述

语言检测工具自动识别项目使用的编程语言，为编码 checklist 加载和代码规范检查提供依据。

## 检测方法

### 方法 1: 文件扩展名检测

通过分析项目中的文件扩展名来判断使用的主要编程语言。

```javascript
const LANGUAGE_MAP = {
  // Python
  '.py': 'python',

  // Go
  '.go': 'go',

  // JavaScript/TypeScript
  '.js': 'javascript',
  '.jsx': 'javascript',
  '.ts': 'typescript',
  '.tsx': 'typescript',
  '.mjs': 'javascript',
  '.cjs': 'javascript',

  // C/C++
  '.c': 'c',
  '.cpp': 'cpp',
  '.cc': 'cpp',
  '.cxx': 'cpp',
  '.h': 'c',
  '.hpp': 'cpp',
  '.hxx': 'cpp',

  // Shell
  '.sh': 'shell',
  '.bash': 'shell',
  '.zsh': 'shell',
  '.fish': 'shell',

  // Rust
  '.rs': 'rust',

  // Java
  '.java': 'java',

  // Kotlin
  '.kt': 'kotlin',
  '.kts': 'kotlin',

  // Swift
  '.swift': 'swift',

  // Ruby
  '.rb': 'ruby',

  // PHP
  '.php': 'php',

  // C#
  '.cs': 'csharp',

  // Other
  '.pl': 'perl',
  '.pm': 'perl',
  '.lua': 'lua',
  '.r': 'r',
  '.R': 'r',
  '.scala': 'scala',
  '.ex': 'elixir',
  '.exs': 'elixir',
  '.erl': 'erlang',
  '.hs': 'haskell',
  '.fs': 'fsharp',
  '.v': 'verilog',
  '.sv': 'systemverilog',
};
```

### 方法 2: 配置文件检测

通过项目的配置文件来判断编程语言。

```javascript
const CONFIG_FILE_MAP = {
  'package.json': 'javascript/typescript',
  'tsconfig.json': 'typescript',
  'go.mod': 'go',
  'Cargo.toml': 'rust',
  'requirements.txt': 'python',
  'setup.py': 'python',
  'pyproject.toml': 'python',
  'pom.xml': 'java',
  'build.gradle': 'java',
  'Gemfile': 'ruby',
  'composer.json': 'php',
  'pubspec.yaml': 'dart',
  'Cargo.toml': 'rust',
};
```

### 方法 3: 目录结构检测

通过项目的目录结构来判断编程语言。

```javascript
const DIRECTORY_STRUCTURE_MAP = {
  'src/main/java': 'java',
  'app/src/main': 'android',
  'src/main/cpp': 'cpp',
  '__tests__': 'javascript/typescript',
  'test': 'python/go/rust/etc',
  'tests': 'python/go/rust/etc',
  'spec': 'ruby',
};
```

## 检测流程

### Step 1: 扫描项目文件

```javascript
async function scanProjectFiles(projectPath) {
  const files = await glob('**/*', {
    cwd: projectPath,
    ignore: ['node_modules/**', 'dist/**', 'build/**', '.git/**'],
  });
  return files;
}
```

### Step 2: 统计文件类型

```javascript
function countFileTypes(files) {
  const counts = {};

  for (const file of files) {
    const ext = path.extname(file);
    if (ext) {
      counts[ext] = (counts[ext] || 0) + 1;
    }
  }

  return counts;
}
```

### Step 3: 确定主要语言

```javascript
function determinePrimaryLanguage(counts) {
  // 按文件数量排序
  const sorted = Object.entries(counts)
    .sort((a, b) => b[1] - a[1]);

  // 获取最多的文件类型
  const topExt = sorted[0]?.[0];
  const language = LANGUAGE_MAP[topExt];

  return language;
}
```

### Step 4: 验证结果

```javascript
function validateLanguage(projectPath, detectedLanguage) {
  // 通过配置文件验证
  const configFiles = fs.readdirSync(projectPath);
  const configLanguage = detectFromConfig(configFiles);

  // 如果配置文件检测到的语言与文件扩展名检测一致，则确认
  if (configLanguage && configLanguage.includes(detectedLanguage)) {
    return detectedLanguage;
  }

  // 否则返回配置文件检测到的语言
  return configLanguage || detectedLanguage;
}
```

## 语言与 Checklist 映射

```javascript
const CHECKLIST_MAP = {
  'python': 'coding-checklist-python.md',
  'go': 'coding-checklist-go.md',
  'javascript': 'coding-checklist-js.md',
  'typescript': 'coding-checklist-js.md', // TypeScript 与 JavaScript 共用
  'java': 'coding-checklist-java.md',
  'cpp': 'coding-checklist-c-cpp.md',
  'c': 'coding-checklist-c-cpp.md',
  'shell': 'coding-checklist-shell.md',
  'rust': 'coding-checklist-rust.md',
  // 其他语言...
};
```

## 使用示例

### 示例 1: 检测项目语言

```javascript
const language = await detectLanguage('/path/to/project');
console.log(`项目主要语言: ${language}`);
// 输出: 项目主要语言: typescript
```

### 示例 2: 获取对应的 Checklist

```javascript
const language = await detectLanguage('/path/to/project');
const checklistPath = CHECKLIST_MAP[language];
console.log(`编码规范: ${checklistPath}`);
// 输出: 编码规范: coding-checklist-js.md
```

### 示例 3: 多语言项目

```javascript
const languages = await detectAllLanguages('/path/to/project');
console.log(`项目使用的语言: ${languages.join(', ')}`);
// 输出: 项目使用的语言: typescript, python, shell
```

## 多语言项目处理

对于多语言项目，按以下优先级处理：

1. **主要语言**: 文件数量最多的语言
2. **配置文件语言**: 通过配置文件确定的语言
3. **核心语言**: 核心业务逻辑使用的语言

### 多语言项目示例

```
project/
├── frontend/      # TypeScript (100 files)
├── backend/       # Python (50 files)
└── scripts/       # Shell (5 files)
```

检测结果：主要语言为 `typescript`。

## 编码规范检查

### 检查流程

```javascript
async function checkCodingStandards(projectPath) {
  // 1. 检测语言
  const language = await detectLanguage(projectPath);

  // 2. 获取对应的 checklist
  const checklistPath = CHECKLIST_MAP[language];
  if (!checklistPath) {
    console.warn(`未找到语言 ${language} 的编码规范 checklist`);
    return null;
  }

  // 3. 加载 checklist
  const checklist = await loadTemplate(`coding/${checklistPath}`);

  // 4. 逐项检查
  const results = await executeChecklist(projectPath, checklist);

  return results;
}
```

### 检查项示例

```markdown
# Python 编码规范 Checklist

## 1. 命名规范
- [ ] 变量使用 snake_case
- [ ] 函数使用 snake_case
- [ ] 类使用 PascalCase
- [ ] 常量使用 UPPER_SNAKE_CASE

## 2. 代码格式
- [ ] 遵循 PEP 8 规范
- [ ] 使用 4 空格缩进
- [ ] 每行不超过 79 字符
- [ ] 使用 black 格式化

## 3. 类型注解
- [ ] 函数有类型注解
- [ ] 使用 typing 模块
- [ ] 避免 any 类型

## 4. 文档字符串
- [ ] 函数有 docstring
- [ ] 类有 docstring
- [ ] 模块有 docstring

## 5. 错误处理
- [ ] 使用具体异常类型
- [ ] 捕获异常不过于宽泛
- [ ] 有适当的日志记录
```

## 配置选项

```json
{
  "languageDetection": {
    "methods": [
      "fileExtension",
      "configFile",
      "directoryStructure"
    ],
    "ignorePatterns": [
      "node_modules/**",
      "dist/**",
      "build/**",
      ".git/**",
      "vendor/**"
    ],
    "multiLanguage": {
      "strategy": "primary",
      "primary": "fileCount"
    }
  }
}
```

## 与代理集成

- **Implementation Agent**:
  1. 检测项目语言
  2. 加载对应的编码 checklist
  3. 在编码过程中检查清单项
  4. 生成符合规范的代码

- **Verification Agent**:
  1. 检测项目语言
  2. 验证代码是否符合对应语言的编码规范
  3. 生成规范检查报告

## 注意事项

1. **准确性**: 文件扩展名检测可能不准确，建议结合多种方法
2. **多语言项目**: 需要明确主要语言和检查策略
3. **自定义扩展**: 支持用户添加新的语言映射
4. **性能优化**: 大型项目需要考虑扫描性能，可以使用缓存

## 扩展支持

### 添加新语言支持

```javascript
// 1. 添加文件扩展名映射
LANGUAGE_MAP['.xyz'] = 'xyzlang';

// 2. 添加配置文件映射
CONFIG_FILE_MAP['xyz.config'] = 'xyzlang';

// 3. 添加 checklist 映射
CHECKLIST_MAP['xyzlang'] = 'coding-checklist-xyz.md';

// 4. 创建对应的 checklist 模板
// templates/coding/coding-checklist-xyz.md
```

### 自定义检测规则

```javascript
// 用户可以自定义检测规则
const customRules = {
  fileExtensions: {
    '.xyz': 'xyzlang',
  },
  configFiles: {
    'xyz.config': 'xyzlang',
  },
};
```
