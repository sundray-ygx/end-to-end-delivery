# 测试模板使用说明

本目录包含各种编程语言的单元测试审查维度模板，用于在实施阶段进行测试质量审查。

## 模板列表

| 文件 | 语言/框架 | 描述 |
|------|----------|------|
| `testing-checklist-python.md` | Python | pytest、fixtures、mocking、参数化、异步等 |
| `testing-checklist-js.md` | JavaScript/TypeScript | Jest、Vitest、Testing Library、快照、React组件等 |
| `testing-checklist-go.md` | Go | testing 包、表格驱动、接口、并发等 |
| `testing-checklist-java.md` | Java | JUnit、Mockito、参数化等 |
| `testing-checklist-rust.md` | Rust | 内置测试框架、属性测试等 |
| `testing-checklist-c-cpp.md` | C/C++ | Google Test、Catch2 等 |
| `testing-checklist-shell.md` | Shell | Bats、shunit2 等 |
| `testing-checklist-generic.md` | 通用 | 语言无关的测试维度 |

## 使用方式

### 1. 自动加载

Template Adapter 会根据项目语言自动加载对应的测试 checklist：

```javascript
// 检测项目语言
const language = await detectProjectLanguage(projectPath);

// 获取测试 checklist
const testingChecklist = await getTestingChecklist(language);

// 提取审查维度
const dimensions = testingChecklist.dimensions;
```

### 2. 语言映射

```javascript
const TESTING_CHECKLIST_MAP = {
  python: 'testing-checklist-python.md',
  javascript: 'testing-checklist-js.md',
  typescript: 'testing-checklist-js.md',
  go: 'testing-checklist-go.md',
  java: 'testing-checklist-java.md',
  rust: 'testing-checklist-rust.md',
  c: 'testing-checklist-c-cpp.md',
  cpp: 'testing-checklist-c-cpp.md',
  shell: 'testing-checklist-shell.md',
  // 其他语言使用通用模板
  default: 'testing-checklist-generic.md',
};
```

## 审查流程

### 在实施阶段

1. **检测语言**：自动检测项目使用的编程语言
2. **加载 Checklist**：加载对应的测试 checklist
3. **提取维度**：从 checklist 中提取审查维度
4. **集成 Skill**：调用对应的 testing-patterns skill（如适用）
5. **深度审查**：基于维度对测试代码进行深度分析
6. **生成报告**：输出测试质量审查报告

### 审查输出

实施阶段会生成以下输出：

```
docs/
└── 06_测试质量审查报告.md
```

## 与 Skills 集成

### 自动调用映射

| 语言 | 对应 Skill |
|------|-----------|
| Python | `python-development:python-testing-patterns` |
| JavaScript | `javascript-typescript:javascript-testing-patterns` |
| TypeScript | `javascript-typescript:javascript-testing-patterns` |
| Shell | `shell-scripting:bats-testing-patterns` |
| 其他 | *暂无对应 skill，使用 checklist* |

## 核心测试维度

### 通用维度（所有语言）

1. **测试结构** - AAA 模式、命名规范、文件组织
2. **测试覆盖** - 快乐路径、边界条件、错误场景
3. **测试隔离** - 独立性、无共享状态、资源清理
4. **断言质量** - 完整性、准确性、可读性
5. **Mock 隔离** - 外部依赖隔离、使用合理性
6. **可维护性** - 代码质量、执行效率

### 语言特定维度

- **Python**：Fixture 使用、参数化测试、异步测试、属性测试
- **JS/TS**：Testing Library、Jest Mocks、快照测试、React 组件测试
- **Go**：表格驱动测试、接口 Mock、并发测试、基准测试
- **Java**：JUnit 参数化、Mockito、Spring 测试
- **Rust**：属性测试、文档测试、Unsafe 测试
- **C/C++**：内存管理、异常测试、模板测试
- **Shell**：命令 Mock、输出验证、可移植性

## 质量评估

每个 checklist 包含质量评估矩阵，按以下维度评分：

| 维度 | 权重 | 评分标准 |
|-----|------|---------|
| 测试结构 | 10-15% | AAA模式清晰、命名规范 |
| 测试覆盖 | 20-25% | 快乐/边界/错误场景完整 |
| Mock/隔离 | 10-15% | 正确隔离、不过度 |
| 断言质量 | 10-15% | 完整、准确 |
| 覆盖率 | 10% | ≥80% |
| 可维护性 | 5-10% | 代码清晰、高效 |

### 质量等级

- **4.5-5.0**: 优秀 - 测试质量卓越
- **4.0-4.4**: 良好 - 测试质量优秀，有小幅改进空间
- **3.5-3.9**: 合格 - 测试质量达标，有明显改进空间
- **3.0-3.4**: 需改进 - 测试存在较多问题
- **< 3.0**: 不合格 - 测试质量严重不足

## 扩展指南

### 添加新语言支持

1. 创建 `testing-checklist-{language}.md`
2. 遵循现有模板结构
3. 包含语言特定的测试维度
4. 更新 `utils/template-adapter.md` 中的映射
5. 更新本 README 的模板列表

### 模板结构规范

```markdown
# {语言} 单元测试 Checklist

> 本文档提供 {语言} 单元测试的审查维度框架
> 基于 {测试框架} 等最佳实践

## 审查维度说明
[说明文档用途]

---

## 维度 1: {维度名称}
### 1.1 {子维度}
**维度说明**: [说明]
**审查要点**: [checklist]
**深度分析方向**: [指导]
**相关模式**: [skill 映射]

---

## 质量评估矩阵
[评分表格]

## 审查结果汇总模板
[报告模板]
```

## 参考资料

- [Python Testing Patterns](https://github.com/anthropics/claude-code-workflows/tree/main/plugins/python-development/skills/python-testing-patterns)
- [JavaScript Testing Patterns](https://github.com/anthropics/claude-code-workflows/tree/main/plugins/javascript-typescript/skills/javascript-testing-patterns)
- [Shell Testing Patterns](https://github.com/anthropics/claude-code-workflows/tree/main/plugins/shell-scripting/skills/bats-testing-patterns)
