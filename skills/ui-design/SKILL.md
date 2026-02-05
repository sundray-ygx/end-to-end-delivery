---
name: ui-design
description: "UI/UX设计能力闭环 - 整合设计系统生成、高质量实现、规范验证三大能力。支持67种样式、96种调色板、57种字体搭配、13种技术栈。"
license: MIT
---

# UI/UX 设计能力闭环

这是一个完整的端到端UI/UX设计技能，整合了三大插件的核心优势：

| 能力层 | 来源 | 描述 |
|--------|------|------|
| **设计系统生成** | ui-ux-pro-max | 67种样式、96种调色板、57种字体搭配，智能推荐设计系统 |
| **高质量实现** | frontend-design | 独特美学方向、艺术性设计、避免通用AI美学 |
| **规范验证** | web-design-guidelines | Vercel Web Interface Guidelines审查、无障碍性检查 |

## 何时使用

当用户请求以下操作时触发此技能：

### 设计/创建类
- "设计/创建/构建 UI组件"
- "制作落地页/仪表板/管理面板"
- "实现/开发 前端界面"

### 审查/验证类
- "审查/检查/验证 UI代码"
- "改进/优化/增强 现有设计"
- "是否符合Web界面规范"

### 系统类
- "生成设计系统"
- "创建视觉规范"
- "UI/UX最佳实践"

---

## 工作流程

### 阶段1: 需求分析

从用户请求中提取关键信息：

```
产品类型: [SaaS | 电商 | 作品集 | 仪表板 | 落地页 | 其他]
行业领域: [医疗 | 金融科技 | 游戏 | 教育 | 美业 | 其他]
风格关键词: [极简 | 俏皮 | 专业 | 优雅 | 暗色模式 | 其他]
技术栈: [html-tailwind | React | Next.js | Vue | Svelte | 其他]
```

### 阶段2: 设计系统生成（必需）

**始终从生成设计系统开始**，使用设计系统生成脚本：

```bash
python3 skills/ui-design/scripts/design_system.py "<产品类型> <行业> <关键词>" --project-name "项目名称"
```

此命令将：
1. 跨5个域并行搜索（product、style、color、landing、typography）
2. 应用推理规则选择最佳匹配
3. 返回完整设计系统：pattern、style、colors、typography、effects
4. 包含需避免的反模式

**输出格式选项：**
```bash
# ASCII盒格式（默认）- 适合终端显示
python3 skills/ui-design/scripts/design_system.py "fintech crypto" --project-name "CryptoApp"

# Markdown格式 - 适合文档
python3 skills/ui-design/scripts/design_system.py "fintech crypto" --project-name "CryptoApp" --format markdown
```

### 阶段3: 设计实现

基于生成的设计系统，使用以下原则实现代码：

#### 美学方向确定

在设计思维阶段，明确一个大胆的美学方向：

| 方向类型 | 示例 |
|----------|------|
| 极简/极繁 | brutalist minimalism, maximalist chaos |
| 复古/未来 | retro-futuristic, art deco/geometric |
| 自然/工业 | organic/natural, industrial/utilitarian |
| 情感/风格 | playful/toy-like, luxury/refined, editorial/magazine |

**关键原则：** 选择清晰的概念方向并精确执行。大胆的极繁主义和精致的极简主义都有效 - 关键在于意图性，而非强度。

#### 字体选择

- **避免通用字体：** Arial、Inter、Roboto、系统字体
- **选择独特字体：** 搭配独特的显示字体和精致的正文字体
- **使用Google Fonts：** 探索意外的、有性格的字体选择

#### 色彩主题

- **坚持cohesive美学：** 使用CSS变量保持一致性
- **主导色 + 强调色：** 比均匀分布的调色板更好
- **避免陈词滥调：** 特别是白色背景上的紫色渐变

#### 动效

- **优先CSS-only解决方案：** 对于HTML
- **React使用Motion库：** 当可用时
- **聚焦高影响力时刻：** 一个精心编排的页面加载（带staggered reveals）比分散的微交互更有效
- **滚动触发和悬停状态：** 创造惊喜效果

#### 空间构成

- **非常规布局：** 非对称、重叠、对角线流、打破网格的元素
- **慷慨的留白 OR 受控的密度：** 根据美学方向选择

#### 背景与视觉细节

- **创造氛围和深度：** 而非默认为纯色
- **添加contextual效果：** 匹配整体美学
- **创意形式：** gradient meshes、noise textures、geometric patterns、layered transparencies、dramatic shadows、decorative borders、custom cursors、grain overlays

**永远避免的通用AI美学：**
- 过度使用的字体系列（Inter、Roboto、Arial、系统字体）
- 陈词滥调的配色方案（特别是白色背景上的紫色渐变）
- 可预测的布局和组件模式
- 缺乏上下文特定character的cookie-cutter设计

### 阶段4: 设计验证

实现完成后，进行规范验证：

#### Web Interface Guidelines审查

使用Vercel Web Interface Guidelines进行审查，检查：

| 类别 | 优先级 | 检查项 |
|------|--------|--------|
| **无障碍** | CRITICAL | color-contrast, focus-states, alt-text, aria-labels, keyboard-nav, form-labels |
| **触摸交互** | CRITICAL | touch-target-size, hover-vs-tap, loading-buttons, error-feedback, cursor-pointer |
| **性能** | HIGH | image-optimization, reduced-motion, content-jumping |
| **布局响应** | HIGH | viewport-meta, readable-font-size, horizontal-scroll, z-index-management |
| **字体色彩** | MEDIUM | line-height, line-length, font-pairing |
| **动效** | MEDIUM | duration-timing, transform-performance, loading-states |
| **样式选择** | MEDIUM | style-match, consistency, no-emoji-icons |
| **图表数据** | LOW | chart-type, color-guidance, data-table |

#### 预交付检查清单

在交付UI代码之前，验证以下项目：

**视觉质量**
- [ ] 没有使用emoji作为图标（使用SVG代替）
- [ ] 所有图标来自一致的图标集（Heroicons/Lucide）
- [ ] 品牌logo正确（从Simple Icons验证）
- [ ] 悬停状态不会导致布局偏移
- [ ] 直接使用主题颜色（bg-primary）而非var()包装器

**交互**
- [ ] 所有可点击元素都有`cursor-pointer`
- [ ] 悬停状态提供清晰的视觉反馈
- [ ] 过渡平滑（150-300ms）
- [ ] 键盘导航可见焦点状态

**亮/暗模式**
- [ ] 亮模式文本有足够对比度（最低4.5:1）
- [ ] 玻璃/透明元素在亮模式下可见
- [ ] 两种模式下边框都可见
- [ ] 交付前测试两种模式

**布局**
- [ ] 浮动元素与边缘有适当间距
- [ ] 没有内容隐藏在固定导航栏后面
- [ ] 响应式：375px、768px、1024px、1440px
- [ ] 移动端无水平滚动

**无障碍**
- [ ] 所有图片都有alt文本
- [ ] 表单输入有标签
- [ ] 颜色不是唯一指示器
- [ ] 尊重`prefers-reduced-motion`

---

## 设计系统持久化（可选）

使用MASTER.md + pages/ 覆盖模式保存设计系统：

```bash
python3 skills/ui-design/scripts/design_system.py "<query>" --project-name "Project" --persist
```

这将创建：
- `design-system/<project>/MASTER.md` — 全局单一真实来源，包含所有设计规则
- `design-system/<project>/pages/` — 页面特定覆盖的文件夹

**带页面特定覆盖：**
```bash
python3 skills/ui-design/scripts/design_system.py "<query>" --project-name "Project" --persist --page "dashboard"
```

**分层检索逻辑：**
1. 构建特定页面时，首先检查`design-system/pages/<page-name>.md`
2. 如果页面文件存在，其规则**覆盖**Master文件
3. 如果不存在，严格遵循Master文件规则

---

## 补充搜索（按需）

获得设计系统后，使用域搜索获取额外细节：

```bash
python3 skills/ui-design/scripts/search.py "<keyword>" --domain <domain>
```

| 需求 | 域 | 示例 |
|------|-----|------|
| 更多样式选项 | `style` | `--domain style "glassmorphism dark"` |
| 图表推荐 | `chart` | `--domain chart "real-time dashboard"` |
| UX最佳实践 | `ux` | `--domain ux "animation accessibility"` |
| 替代字体 | `typography` | `--domain typography "elegant luxury"` |
| 落地页结构 | `landing` | `--domain landing "hero social-proof"` |

---

## 专业UI通用规则

这些是经常被忽视但使UI看起来不专业的问题：

### 图标与视觉元素

| 规则 | 做 | 不要 |
|------|----|----- |
| **无emoji图标** | 使用SVG图标（Heroicons、Lucide、Simple Icons） | 使用🎨🚀⚙️等emoji作为UI图标 |
| **稳定的悬停状态** | 使用悬停时的颜色/不透明度过渡 | 使用导致布局偏移的scale变换 |
| **正确的品牌logo** | 从Simple Icons研究官方SVG | 猜测或使用错误的logo路径 |
| **一致的图标尺寸** | 使用固定viewBox（24x24）和w-6 h-6 | 随机混合不同图标尺寸 |

### 交互与光标

| 规则 | 做 | 不要 |
|------|----|----- |
| **光标pointer** | 给所有可点击/可悬停的卡片添加`cursor-pointer` | 在交互元素上保留默认光标 |
| **悬停反馈** | 提供视觉反馈（颜色、阴影、边框） | 元素可交互的没有指示 |
| **平滑过渡** | 使用`transition-colors duration-200` | 瞬间状态变化或太慢（>500ms） |

### 亮/暗模式对比度

| 规则 | 做 | 不要 |
|------|----|----- |
| **亮模式玻璃卡片** | 使用`bg-white/80`或更高不透明度 | 使用`bg-white/10`（太透明） |
| **亮模式文本对比度** | 使用`#0F172A`（slate-900）作为文本 | 使用`#94A3B8`（slate-400）作为正文文本 |
| **弱化文本亮色** | 使用`#475569`（slate-600）最低 | 使用gray-400或更浅 |
| **边框可见性** | 在亮模式下使用`border-gray-200` | 使用`border-white/10`（不可见） |

---

## 技术栈指南

| 技术栈 | 聚焦 |
|--------|------|
| `html-tailwind` | Tailwind工具类、响应式、a11y（默认） |
| `react` | 状态、hooks、性能、模式 |
| `nextjs` | SSR、路由、图片、API路由 |
| `vue` | Composition API、Pinia、Vue Router |
| `svelte` | Runes、stores、SvelteKit |
| `swiftui` | Views、State、Navigation、Animation |
| `react-native` | Components、Navigation、Lists |
| `flutter` | Widgets、State、Layout、Theming |
| `shadcn` | shadcn/ui组件、主题、表单、模式 |
| `jetpack-compose` | Composables、Modifiers、State Hoisting、Recomposition |

---

## 使用技巧

1. **关键词要具体** - "医疗SaaS仪表板" > "app"
2. **多次搜索** - 不同的关键词揭示不同的洞察
3. **组合域** - 样式 + 字体 + 色彩 = 完整设计系统
4. **始终检查UX** - 搜索"animation"、"z-index"、"accessibility"以发现常见问题
5. **使用stack标志** - 获取特定实现的最佳实践
6. **迭代** - 如果第一次搜索不匹配，尝试不同的关键词

---

## 重要提示

**避免通用AI美学：** 记住，Claude能够做出非凡的创意工作。不要退缩，展示跳出思维定式并完全致力于独特愿景时能真正创造什么。

**变化是关键：** 不要每次都收敛到常见选择。在亮色和暗色主题、不同字体、不同美学之间变化。永远不要跨代收敛到常见选择（例如Space Grotesk）。

**匹配复杂度：** 将实现复杂度与美学愿景匹配。极繁主义设计需要大量动画和效果的详细代码。极简主义或精致设计需要克制、精确和对间距、字体和微妙细节的仔细关注。优雅来自于很好地执行愿景。
