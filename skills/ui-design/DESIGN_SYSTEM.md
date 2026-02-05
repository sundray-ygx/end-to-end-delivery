# 设计系统生成指南

本文档提供设计系统生成的详细指南，整合自 ui-ux-pro-max 插件的核心能力。

## 概述

设计系统生成器通过跨5个域（product、style、color、landing、typography）的智能搜索和推理规则，为项目生成完整的设计系统推荐。

## 使用方法

### 基本用法

```bash
python3 skills/ui-design/scripts/design_system.py "<查询>" --project-name "项目名称"
```

**示例：**
```bash
# SaaS仪表板项目
python3 skills/ui-design/scripts/design_system.py "SaaS analytics dashboard" --project-name "DataViz Pro"

# 电商网站
python3 skills/ui-design/scripts/design_system.py "e-commerce fashion luxury" --project-name "LuxeStyle"

# 美业服务
python3 skills/ui-design/scripts/design_system.py "beauty spa wellness elegant" --project-name "Serenity Spa"
```

### 输出格式选项

```bash
# ASCII盒格式（默认）- 适合终端显示
python3 skills/ui-design/scripts/design_system.py "fintech crypto" --project-name "CryptoApp"

# Markdown格式 - 适合文档
python3 skills/ui-design/scripts/design_system.py "fintech crypto" --project-name "CryptoApp" --format markdown
```

### 持久化设计系统

保存设计系统到文件，使用MASTER.md + pages/覆盖模式：

```bash
# 保存全局设计系统
python3 skills/ui-design/scripts/design_system.py "<query>" --project-name "Project" --persist

# 保存全局设计系统 + 页面特定覆盖
python3 skills/ui-design/scripts/design_system.py "<query>" --project-name "Project" --persist --page "dashboard"
```

**文件结构：**
```
design-system/
└── <project-slug>/
    ├── MASTER.md          # 全局设计规则（单一真实来源）
    └── pages/             # 页面特定覆盖
        ├── dashboard.md   # 仪表板页面覆盖
        ├── checkout.md    # 结账页面覆盖
        └── ...
```

---

## 生成流程

### 第一步：产品类型识别

首先搜索产品域，识别产品类别：

```python
# 输入: "beauty spa wellness elegant"
# 输出: Product Type = "Beauty/Spa"
```

### 第二步：推理规则应用

根据产品类别应用推理规则，获取风格优先级：

```
Category: Beauty/Spa
→ Style Priority: ["Minimalism", "Soft Design", "Elegant"]
→ Color Mood: "Soft, Pastel"
→ Typography Mood: "Elegant, Refined"
```

### 第三步：多域搜索

使用风格优先级作为提示，并行搜索5个域：

| 域 | 搜索内容 | 返回结果数 |
|----|----------|-----------|
| `product` | 产品类型推荐 | 1 |
| `style` | UI风格（带优先级提示） | 3 |
| `color` | 产品类型配色方案 | 2 |
| `landing` | 页面结构/CTA策略 | 2 |
| `typography` | 字体搭配 | 2 |

### 第四步：最佳匹配选择

使用优先级关键词从搜索结果中选择最佳匹配：

```python
# 风格匹配逻辑：
# 1. 优先精确风格名称匹配
# 2. 按关键词匹配度评分
# 3. 选择最高分结果
```

### 第五步：生成完整设计系统

```
┌────────────────────────────────────────────────────────────┐
│  TARGET: PROJECT NAME - RECOMMENDED DESIGN SYSTEM          │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  PATTERN: Hero + Features + CTA                            │
│     Conversion: Social proof near CTA                      │
│     CTA: Above fold                                        │
│     Sections:                                              │
│       1. Hero                                              │
│       2. Features                                          │
│       3. Social Proof                                      │
│       4. CTA                                               │
│                                                            │
│  STYLE: Minimalism                                         │
│     Keywords: clean, simple, whitespace, functional        │
│     Best For: SaaS, professional services                  │
│     Performance: High | Accessibility: High                │
│                                                            │
│  COLORS:                                                   │
│     Primary:    #2563EB                                    │
│     Secondary:  #3B82F6                                    │
│     CTA:        #F97316                                    │
│     Background: #F8FAFC                                    │
│     Text:       #1E293B                                    │
│                                                            │
│  TYPOGRAPHY: Inter / Inter                                 │
│     Mood: Clean, Professional, Modern                      │
│     Google Fonts: https://fonts.google.com/...             │
│                                                            │
│  KEY EFFECTS:                                              │
│     Subtle hover transitions, micro-interactions            │
│                                                            │
│  AVOID (Anti-patterns):                                    │
│     Cluttered layouts + Overly saturated colors            │
│                                                            │
│  PRE-DELIVERY CHECKLIST:                                   │
│     [ ] No emojis as icons (use SVG: Heroicons/Lucide)     │
│     [ ] cursor-pointer on all clickable elements           │
│     [ ] Hover states with smooth transitions (150-300ms)   │
│     ...                                                    │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## 设计系统组件

### Pattern（页面模式）

- **Name**: 模式名称（如"Hero + Features + CTA"）
- **Sections**: 章节顺序
- **CTA Placement**: 主要CTA位置
- **Color Strategy**: 色彩策略
- **Conversion Optimization**: 转化优化建议

### Style（风格）

- **Name**: 风格类别（如"Minimalism"、"Glassmorphism"）
- **Type**: 风格类型
- **Keywords**: 关键词描述
- **Best For**: 最佳适用场景
- **Performance**: 性能评级
- **Accessibility**: 无障碍评级

### Colors（色彩）

| 角色 | Hex值 | CSS变量 |
|------|-------|---------|
| Primary | 主色 | `--color-primary` |
| Secondary | 辅色 | `--color-secondary` |
| CTA/Accent | 强调色 | `--color-cta` |
| Background | 背景色 | `--color-background` |
| Text | 文本色 | `--color-text` |

### Typography（字体）

- **Heading Font**: 标题字体
- **Body Font**: 正文字体
- **Mood/Style**: 字体情绪/风格
- **Google Fonts URL**: Google Fonts链接
- **CSS Import**: CSS导入代码

---

## 推理规则示例

### 按产品类别的风格优先级

| 产品类别 | 风格优先级 | 色彩情绪 | 字体情绪 |
|----------|-----------|----------|----------|
| **SaaS** | Minimalism + Flat Design | Professional, Trust | Clean, Modern |
| **E-commerce** | Clean + Bold | Vibrant, High Contrast | Bold, Readable |
| **Beauty/Spa** | Minimalism + Soft Design | Soft, Pastel | Elegant, Refined |
| **Fintech** | Minimalism + Corporate | Professional, Blue | Professional, Trust |
| **Gaming** | Cyberpunk + Neon | Vibrant, High Contrast | Bold, Dynamic |
| **Healthcare** | Clean + Professional | Calm, Trust | Professional, Clear |

---

## 分层检索逻辑

使用持久化设计系统时，遵循以下检索逻辑：

```
构建页面时：
1. 检查 design-system/<project>/pages/<page-name>.md
2. 如果存在 → 使用其规则（覆盖Master）
3. 如果不存在 → 使用 design-system/<project>/MASTER.md
```

### MASTER.md 内容

全局设计规则，包括：
- 色彩调色板
- 字体搭配
- 间距变量
- 阴影深度
- 组件规范（按钮、卡片、输入框、模态框）
- 页面模式
- 反模式

### 页面覆盖内容

页面特定偏差，包括：
- 布局覆盖（最大宽度、布局类型）
- 间距覆盖（内容密度）
- 字体覆盖（特定页面的字体大小）
- 色彩覆盖（特定页面的色彩使用）
- 组件覆盖（页面特定组件）
- 页面特定组件
- 建议

---

## 命令行参数

```bash
usage: design_system.py [-h] [--project-name PROJECT_NAME] [--format {ascii,markdown}]
                        [--persist] [--page PAGE] [--output-dir OUTPUT_DIR]
                        query

Generate Design System from query.

positional arguments:
  query                 Search query (e.g., "SaaS dashboard", "e-commerce luxury")

options:
  -h, --help            show this help message and exit
  --project-name PROJECT_NAME, -p PROJECT_NAME
                        Project name for output header
  --format {ascii,markdown}, -f {ascii,markdown}
                        Output format (default: ascii)
  --persist             Save design system to design-system/ folder
  --page PAGE           Optional page name for page-specific override file
  --output-dir OUTPUT_DIR
                        Optional output directory (defaults to current working directory)
```

---

## 示例输出

### Markdown格式

```markdown
## Design System: SERENITY SPA

### Pattern
- **Name:** Hero + Features + CTA
- **Conversion Focus:** Social proof near CTA
- **CTA Placement:** Above fold
- **Sections:** Hero > Features > Testimonials > CTA

### Style
- **Name:** Soft Design
- **Keywords:** gentle, rounded, pastel, inviting, warmth
- **Best For:** Wellness, beauty, childcare, healthcare
- **Performance:** High | **Accessibility:** High

### Colors
| Role | Hex |
|------|-----|
| Primary | `#FBCFE8` |
| Secondary | `#FDF2F8` |
| CTA | `#EC4899` |
| Background | `#FFF5F7` |
| Text | `#831843` |

### Typography
- **Heading:** Playfair Display
- **Body:** Lato
- **Mood:** Elegant, Reminiscent, High-contrast, Luxurious
```

---

## 注意事项

1. **关键词要具体** - "医疗SaaS仪表板"比"app"能产生更好的结果
2. **查询包含产品类型** - 确保推理规则能正确匹配
3. **风格关键词可选** - 但能提高匹配精度
4. **持久化前先验证** - 确认设计系统满意后再持久化
5. **页面覆盖按需创建** - 不是所有页面都需要覆盖文件
