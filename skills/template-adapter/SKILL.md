---
name: template-adapter
description: 本地开发流程模板适配器 - 融合本地开发流程模板、自动适配和加载、支持自定义扩展
---

# 本地开发流程模板适配器

## 概述

本技能支持融合本地的开发流程模板，让端到端交付流程能够适应不同团队和项目的特定需求。

## 模板位置

### 插件默认模板
```
{插件目录}/templates/
├── project-structure/     # 项目结构模板
├── documentation/         # 文档模板
├── custom-workflow/       # 自定义工作流模板
└── coding-standards/      # 代码规范模板（预留）
```

插件实际安装位置：
- **缓存目录**: `~/.claude/plugins/cache/local-plugins/end-to-end-delivery/1.0.0/templates/`
- **市场目录**: `~/.claude/plugins/marketplaces/end-to-end-delivery/templates/`

### 项目本地模板
```
{项目根目录}/.claude/templates/
├── workflow/              # 工作流模板
├── documents/             # 文档模板
└── standards/             # 规范模板
```

## 模板类型

### 1. 工作流模板

定义端到端流程的执行方式:

```markdown
# custom-workflow.md

## 工作流配置

### 阶段顺序
- Discovery
- Exploration
- Design
- Implementation
- Verification
- Delivery

### 自定义阶段
- Pre-check: 在 Discovery 之前
- Post-deploy: 在 Delivery 之后

### 阶段配置
```json
{
  "discovery": {
    "required": true,
    "autoApprove": false,
    "templates": ["requirement-analysis.md"]
  },
  "design": {
    "required": true,
    "parallel": true,
    "options": 3
  }
}
```
```

### 2. 文档模板

定义各种文档的格式:

```markdown
# requirement-template.md

# [Feature Name] 需求规格

## 背景
- 问题陈述: {{problem}}
- 业务价值: {{value}}
- 目标用户: {{users}}

## 功能需求
{% for requirement in requirements %}
### {{requirement.id}}: {{requirement.title}}
{{requirement.description}}
{% endfor %}

## 验收标准
{% for ac in acceptance_criteria %}
- {{ac}}
{% endfor %}
```

### 3. 代码规范模板

定义项目的代码规范:

```markdown
# coding-standards.md

## 命名规范
- 文件: {{file_naming}}
- 变量: {{variable_naming}}
- 函数: {{function_naming}}

## 代码组织
- 最大函数长度: {{max_function_length}}
- 最大文件长度: {{max_file_length}}
- 最大嵌套深度: {{max_nesting_depth}}

## 测试要求
- 最小覆盖率: {{min_coverage}}%
- 关键代码覆盖率: {{critical_coverage}}%
```

### 4. 项目结构模板

定义项目的目录结构:

```markdown
# project-structure.md

## 推荐结构
```
{{project_name}}/
├── src/
│   ├── components/
│   ├── services/
│   ├── utils/
│   └── types/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docs/
├── scripts/
└── config/
```

## 说明
- `src/`: 源代码
- `tests/`: 测试代码
- `docs/`: 项目文档
- `scripts/`: 构建脚本
- `config/`: 配置文件
```

## 模板加载

### 自动加载

插件启动时自动加载模板:

1. **插件默认模板**
   - 从插件安装目录加载 (`~/.claude/plugins/cache/local-plugins/end-to-end-delivery/1.0.0/templates/`)
   - 作为后备模板

2. **项目本地模板**
   - 从 `{项目根目录}/.claude/templates/` 加载
   - 覆盖默认模板

3. **全局模板**
   - 从 `~/.claude/templates/` 加载
   - 覆盖项目模板

### 加载优先级

```
全局模板 > 项目模板 > 插件默认模板
```

## 模板适配

### 变量替换

模板支持变量替换:

```markdown
# 模板
# {{feature_name}} 需求规格

## 背景
- 创建时间: {{timestamp}}
- 创建者: {{author}}

## 功能
{{feature_description}}

## 验收标准
{% for ac in acceptance_criteria %}
- {{ac}}
{% endfor %}
```

### 适配规则

1. **内置变量**
   - `{{feature_name}}`: 功能名称
   - `{{timestamp}}`: 当前时间
   - `{{author}}`: 当前用户
   - `{{project_name}}`: 项目名称

2. **上下文变量**
   - 从当前会话上下文提取
   - 从项目配置读取
   - 从用户输入获取

3. **自定义变量**
   - 在模板中定义
   - 从配置文件加载
   - 动态生成

## 模板使用

### 在技能中使用

```markdown
# 使用模板
使用 `template-adapter` 技能加载需求模板:

1. 加载模板: `requirement-template.md`
2. 填充变量:
   - feature_name: "用户登录"
   - feature_description: "..."
   - acceptance_criteria: ["..."]
3. 生成文档
```

### 在命令中使用

```bash
# 使用特定模板
/deliver "实现用户登录" --template custom-workflow.md

# 使用项目模板
/deliver "实现用户登录" --template .claude/templates/workflow.md
```

## 自定义模板

### 创建模板

1. 在项目目录创建模板文件:
```bash
mkdir -p .claude/templates
nano .claude/templates/my-workflow.md
```

2. 定义模板内容:
```markdown
# 我的工作流

## Discovery
- 使用我自己的需求分析方法
- 输出格式: 自定义

## Design
- 必须包含架构图
- 必须有性能分析

## Implementation
- 严格的 TDD
- 代码审查必须通过
```

3. 在插件中引用:
```markdown
使用模板: `.claude/templates/my-workflow.md`
```

## 模板示例

### 完整的工作流模板

```markdown
# custom-workflow.md

## 阶段配置

### Discovery
- 模板: `templates/requirement-analysis.md`
- 输出: `docs/requirements/{{feature_name}}.md`
- 门禁: 需求明确、验收标准清晰

### Exploration
- 模板: `templates/codebase-analysis.md`
- 输出: `docs/analysis/{{feature_name}}.md`
- 门禁: 代码库理解完整

### Design
- 模板: `templates/architecture-design.md`
- 输出: `docs/design/{{feature_name}}.md`
- 门禁: 方案明确、蓝图详细

### Implementation
- 模板: `templates/implementation.md`
- 输出: 源代码 + 测试
- 门禁: 测试通过、覆盖率达标

### Verification
- 模板: `templates/verification.md`
- 输出: `docs/verification/{{feature_name}}.md`
- 门禁: 所有验证通过

### Delivery
- 模板: `templates/delivery.md`
- 输出: 变更日志、发布说明
- 门禁: 交付物完整

## 自定义检查点
- [ ] 代码审查通过
- [ ] 安全审查通过
- [ ] 性能测试通过

## 自定义输出
- PR 模板: `.claude/pr-template.md`
- 发布说明: `.claude/release-template.md`
```

### 完整的文档模板

```markdown
# requirement-template.md

# {{feature_name}} 需求规格

## 元数据
- **创建时间**: {{timestamp}}
- **创建者**: {{author}}
- **状态**: Draft → Review → Approved
- **优先级**: High / Medium / Low

## 背景
### 问题陈述
{{problem_statement}}

### 业务价值
{{business_value}}

### 目标用户
{{target_users}}

## 功能需求
{% for req in requirements %}
### {{req.id}}: {{req.title}}
**描述**: {{req.description}}
**优先级**: {{req.priority}}
**依赖**: {{req.dependencies}}
{% endfor %}

## 验收标准
{% for ac in acceptance_criteria %}
#### AC-{{loop.index}}: {{ac}}
- Given: {{ac.given}}
- When: {{ac.when}}
- Then: {{ac.then}}
{% endfor %}

## 非功能需求
### 性能
{% for perf in performance %}
- {{perf.metric}}: {{perf.target}}
{% endfor %}

### 安全
{% for sec in security %}
- {{sec.requirement}}
{% endfor %}

### 兼容性
{% for compat in compatibility %}
- {{compat.platform}}: {{compat.version}}
{% endfor %}

## 约束与假设
### 约束
{% for constraint in constraints %}
- {{constraint}}
{% endfor %}

### 假设
{% for assumption in assumptions %}
- {{assumption}}
{% endfor %}

## 风险识别
{% for risk in risks %}
### {{risk.id}}: {{risk.title}}
- **影响**: {{risk.impact}}
- **概率**: {{risk.probability}}
- **缓解**: {{risk.mitigation}}
{% endfor %}

## 成功标准
{% for success in success_criteria %}
- [ ] {{success}}
{% endfor %}

## 附录
### 参考文档
{% for ref in references %}
- [{{ref.title}}]({{ref.url}})
{% endfor %}

### 相关功能
{% for related in related_features %}
- {{related.name}}: {{related.description}}
{% endfor %}
```

## 模板验证

### 验证规则

1. **语法检查**
   - 模板语法正确
   - 变量引用有效
   - 循环结构完整

2. **变量检查**
   - 所有变量已定义
   - 必需变量已提供
   - 默认值已设置

3. **内容检查**
   - 必需章节存在
   - 格式符合规范
   - 语言清晰明确

### 验证命令

```bash
# 验证模板
/validate-template custom-workflow.md

# 验证所有模板
/validate-templates
```

## 模板管理

### 列出模板

```bash
# 列出所有可用模板
/list-templates

# 列出特定类型的模板
/list-templates --type workflow
```

### 更新模板

```bash
# 更新默认模板
/update-default-templates

# 同步项目模板
/sync-templates
```

### 删除模板

```bash
# 删除项目模板
/remove-template custom-workflow.md

# 重置为默认模板
/reset-templates
```

## 最佳实践

### 1. 模板设计
- 保持简洁
- 清晰的结构
- 明确的变量

### 2. 变量命名
- 使用描述性名称
- 避免缩写
- 保持一致性

### 3. 文档化
- 提供使用说明
- 包含示例
- 说明变量含义

### 4. 版本控制
- 纳入 Git 管理
- 标记版本
- 记录变更

## 示例项目

### 完整的项目模板结构

```
my-project/
├── .claude/
│   ├── templates/
│   │   ├── workflow.md
│   │   ├── requirements.md
│   │   ├── design.md
│   │   └── pr-description.md
│   └── config.json
├── src/
├── tests/
└── docs/
```

### 配置文件

```json
// .claude/config.json
{
  "templates": {
    "workflow": ".claude/templates/workflow.md",
    "requirements": ".claude/templates/requirements.md",
    "design": ".claude/templates/design.md"
  },
  "variables": {
    "project_name": "my-project",
    "team": "backend",
    "min_coverage": 80
  },
  "settings": {
    "auto_validate": true,
    "auto_sync": false
  }
}
```

---

**记住**: 模板是为了让流程更高效，而不是增加复杂度。保持简单，逐步改进。
