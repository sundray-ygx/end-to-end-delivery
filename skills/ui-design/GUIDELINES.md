# UI/UX 设计规范检查清单

本文档提供完整的UI/UX设计规范审查清单，整合自 Vercel Web Interface Guidelines 和 ui-ux-pro-max 的最佳实践。

## 规则类别优先级

| 优先级 | 类别 | 影响范围 | 域 |
|--------|------|----------|-----|
| 1 | **无障碍 (Accessibility)** | CRITICAL | `ux` |
| 2 | **触摸交互 (Touch & Interaction)** | CRITICAL | `ux` |
| 3 | **性能 (Performance)** | HIGH | `ux` |
| 4 | **布局响应 (Layout & Responsive)** | HIGH | `ux` |
| 5 | **字体色彩 (Typography & Color)** | MEDIUM | `typography`, `color` |
| 6 | **动效 (Animation)** | MEDIUM | `ux` |
| 7 | **样式选择 (Style Selection)** | MEDIUM | `style`, `product` |
| 8 | **图表数据 (Charts & Data)** | LOW | `chart` |

---

## 1. 无障碍 (Accessibility) - CRITICAL

### 1.1 色彩对比度
- **规则**: `color-contrast`
- **要求**: 普通文本最低4.5:1对比度，大文本（18px+）3:1
- **检查点**:
  - [ ] 正文文本与背景对比度 ≥ 4.5:1
  - [ ] 标题文本与背景对比度 ≥ 3:1
  - [ ] 交互元素（按钮、链接）有足够对比度
  - [ ] 图标与背景对比度 ≥ 3:1

### 1.2 焦点状态
- **规则**: `focus-states`
- **要求**: 所有交互元素可见焦点环
- **检查点**:
  - [ ] 按钮有明显的焦点样式
  - [ ] 链接有焦点样式
  - [ ] 表单输入有焦点样式
  - [ ] 焦点顺序符合逻辑（Tab键导航）
  - [ ] 焦点样式不被`outline: none`移除

### 1.3 替代文本
- **规则**: `alt-text`
- **要求**: 有意义图片提供描述性alt文本
- **检查点**:
  - [ ] 信息性图片有描述性alt
  - [ ] 装饰性图片使用`alt=""`或`role="presentation"`
  - [ ] 功能性图标有aria-label
  - [ ] 复杂图表有详细描述

### 1.4 ARIA标签
- **规则**: `aria-labels`
- **要求**: 纯图标按钮提供aria-label
- **检查点**:
  - [ ] 图标按钮（如搜索、菜单）有aria-label
  - [ ] 关闭按钮有aria-label="Close"
  - [ ] 汉堡菜单有aria-label="Open menu"
  - [ ] 社交图标链接有aria-label

### 1.5 键盘导航
- **规则**: `keyboard-nav`
- **要求**: Tab顺序与视觉顺序一致
- **检查点**:
  - [ ] 所有交互元素可通过Tab访问
  - [ ] Tab顺序从左到右、从上到下
  - [ ] 焦点不被样式隐藏
  - [ ] 下拉菜单可通过键盘操作

### 1.6 表单标签
- **规则**: `form-labels`
- **要求**: 使用带for属性的label
- **检查点**:
  - [ ] 每个输入框有关联的label
  - [ ] label的for属性与input的id匹配
  - [ ] 必填字段有明确指示
  - [ ] 错误消息与输入框关联

---

## 2. 触摸交互 (Touch & Interaction) - CRITICAL

### 2.1 触摸目标尺寸
- **规则**: `touch-target-size`
- **要求**: 最小44x44px触摸目标
- **检查点**:
  - [ ] 按钮最小44x44px
  - [ ] 链接文本（如"click here"）扩大点击区域
  - [ ] 图标按钮有padding满足44px要求
  - [ ] 紧密排列的按钮有间距

### 2.2 悬停vs点击
- **规则**: `hover-vs-tap`
- **要求**: 主要交互使用click/tap，避免仅hover
- **检查点**:
  - [ ] 关键操作不依赖hover
  - [ ] 移动设备hover效果有fallback
  - [ ] 下拉菜单支持点击触发
  - [ ] 工具提示在触摸设备可访问

### 2.3 加载按钮
- **规则**: `loading-buttons`
- **要求**: 异步操作期间禁用按钮
- **检查点**:
  - [ ] 表单提交时按钮禁用
  - [ ] 加载状态有视觉指示
  - [ ] 禁用状态有样式差异
  - [ ] 加载完成前防止重复提交

### 2.4 错误反馈
- **规则**: `error-feedback`
- **要求**: 错误消息显示在问题附近
- **检查点**:
  - [ ] 表单验证错误显示在字段下方
  - [ ] 错误消息使用红色和图标
  - [ ] 成功消息有确认反馈
  - [ ] 错误状态有aria-live="polite"

### 2.5 光标样式
- **规则**: `cursor-pointer`
- **要求**: 可点击元素添加cursor-pointer
- **检查点**:
  - [ ] 按钮有cursor-pointer
  - [ ] 可点击卡片有cursor-pointer
  - [ ] 交互式元素有悬停光标变化
  - [ ] 非交互元素不使用pointer

---

## 3. 性能 (Performance) - HIGH

### 3.1 图片优化
- **规则**: `image-optimization`
- **要求**: 使用WebP、srcset、lazy loading
- **检查点**:
  - [ ] 图片使用现代格式（WebP/AVIF）
  - [ ] 响应式图片使用srcset
  - [ ] 非首屏图片使用lazy loading
  - [ ] 图片大小经过压缩优化

### 3.2 减少动效
- **规则**: `reduced-motion`
- **要求**: 检查prefers-reduced-motion
- **检查点**:
  - [ ] 使用`@media (prefers-reduced-motion)`
  - [ ] 尊重系统动画设置
  - [ ] 关键动画有禁用选项
  - [ ] 减少动效时仍保持功能

### 3.3 内容跳转
- **规则**: `content-jumping`
- **要求**: 为异步内容预留空间
- **检查点**:
  - [ ] 图片加载前预留空间
  - [ ] 骨架屏匹配实际内容高度
  - [ ] 动态内容插入不导致布局偏移
  - [ ] 使用min-height防止CLS

---

## 4. 布局响应 (Layout & Responsive) - HIGH

### 4.1 视口元标签
- **规则**: `viewport-meta`
- **要求**: width=device-width initial-scale=1
- **检查点**:
  - [ ] 包含viewport meta标签
  - [ ] 设置width=device-width
  - [ ] 设置initial-scale=1
  - [ ] 避禁user-scalable=no（除非必要）

### 4.2 可读字体大小
- **规则**: `readable-font-size`
- **要求**: 移动端正文最小16px
- **检查点**:
  - [ ] 移动端基础字体≥16px
  - [ ] 行高1.5-1.75
  - [ ] 段落长度≤75字符
  - [ ] 文本可缩放200%

### 4.3 水平滚动
- **规则**: `horizontal-scroll`
- **要求**: 确保内容适合视口宽度
- **检查点**:
  - [ ] 移动端无意外水平滚动
  - [ ] 表格可滚动或响应式
  - [ ] 代码块可横向滚动
  - [ ] 预格式化文本不破坏布局

### 4.4 Z-index管理
- **规则**: `z-index-management`
- **要求**: 定义z-index比例（10, 20, 30, 50）
- **检查点**:
  - [ ] 使用预定义z-index值
  - [ ] 避免z-index: 9999
  - [ ] 模态框z-index最高（50+）
  - [ ] 下拉菜单z-index中等（30）

---

## 5. 字体色彩 (Typography & Color) - MEDIUM

### 5.1 行高
- **规则**: `line-height`
- **要求**: 正文使用1.5-1.75
- **检查点**:
  - [ ] 正文行高1.5-1.75
  - [ ] 标题行高1.1-1.3
  - [ ] 表单输入行高正常
  - [ ] 列表项行高一致

### 5.2 行长度
- **规则**: `line-length`
- **要求**: 限制每行65-75字符
- **检查点**:
  - [ ] 正文段落≤75字符
  - [ ] 使用max-width限制
  - [ ] 移动端自动换行
  - [ ] 长URL可换行

### 5.3 字体搭配
- **规则**: `font-pairing`
- **要求**: 标题/正文字体性格匹配
- **检查点**:
  - [ ] 标题和正文字体协调
  - [ ] 避免过于相似的字体
  - [ ] 字重有层次感
  - [ ] 保持字体数量≤3种

---

## 6. 动效 (Animation) - MEDIUM

### 6.1 持续时间与缓动
- **规则**: `duration-timing`
- **要求**: 微交互使用150-300ms
- **检查点**:
  - [ ] 悬停效果150-300ms
  - [ ] 页面过渡300-500ms
  - [ ] 使用缓动函数（ease-out）
  - [ ] 避免线性动画

### 6.2 变换性能
- **规则**: `transform-performance`
- **要求**: 使用transform/opacity，不用width/height
- **检查点**:
  - [ ] 动画使用transform
  - [ ] 淡入淡出使用opacity
  - [ ] 避免动画width/height/left/top
  - [ ] 使用will-change提示

### 6.3 加载状态
- **规则**: `loading-states`
- **要求**: 骨架屏或加载指示器
- **检查点**:
  - [ ] 数据加载显示骨架屏
  - [ ] 长时间加载有进度指示
  - [ ] 加载状态匹配内容形状
  - [ ] 加载完成平滑过渡

---

## 7. 样式选择 (Style Selection) - MEDIUM

### 7.1 风格匹配
- **规则**: `style-match`
- **要求**: 样式与产品类型匹配
- **检查点**:
  - [ ] SaaS产品使用简洁风格
  - [ ] 电商使用吸引眼球风格
  - [ ] 医疗使用专业可信风格
  - [ ] 儿童产品使用俏皮风格

### 7.2 一致性
- **规则**: `consistency`
- **要求**: 所有页面使用相同样式
- **检查点**:
  - [ ] 按钮样式一致
  - [ ] 间距系统一致
  - [ ] 颜色使用一致
  - [ ] 字体使用一致

### 7.3 无Emoji图标
- **规则**: `no-emoji-icons`
- **要求**: 使用SVG图标，不用emoji
- **检查点**:
  - [ ] UI使用SVG图标
  - [ ] 图标集一致（Heroicons/Lucide）
  - [ ] 不用emoji作为功能图标
  - [ ] emoji仅用于内容

---

## 8. 图表数据 (Charts & Data) - LOW

### 8.1 图表类型
- **规则**: `chart-type`
- **要求**: 图表类型与数据类型匹配
- **检查点**:
  - [ ] 趋势数据使用折线图
  - [ ] 比较数据使用柱状图
  - [ ] 占比数据使用饼图
  - [ ] 时间轴使用甘特图

### 8.2 色彩指导
- **规则**: `color-guidance`
- **要求**: 使用可访问调色板
- **检查点**:
  - [ ] 图表使用对比色
  - [ ] 色盲友好配色
  - [ ] 不仅依赖颜色传达信息
  - [ ] 使用图案/标签辅助

### 8.3 数据表格
- **规则**: `data-table`
- **要求**: 提供表格替代方案用于无障碍
- **检查点**:
  - [ ] 复杂图表提供数据表格
  - [ ] 表格有语义化HTML
  - [ ] 表头使用<th>
  - [ ] 排序功能可访问

---

## 专业UI通用规则

### 图标与视觉元素

| 规则 | 要求 |
|------|------|
| **无emoji图标** | 使用SVG图标（Heroicons、Lucide、Simple Icons） |
| **稳定的悬停状态** | 使用颜色/不透明度过渡，避免导致布局偏移的scale |
| **正确的品牌logo** | 从Simple Icons验证官方SVG |
| **一致的图标尺寸** | 使用固定viewBox（24x24）和w-6 h-6 |

### 交互与光标

| 规则 | 要求 |
|------|------|
| **光标pointer** | 所有可点击/可悬停元素添加`cursor-pointer` |
| **悬停反馈** | 提供视觉反馈（颜色、阴影、边框） |
| **平滑过渡** | 使用`transition-colors duration-200`（150-300ms） |

### 亮/暗模式对比度

| 规则 | 亮模式 | 暗模式 |
|------|--------|--------|
| **玻璃卡片** | `bg-white/80`或更高 | `bg-black/50` |
| **文本对比** | `#0F172A`（slate-900） | `#F8FAFC`（slate-50） |
| **弱化文本** | `#475569`（slate-600）最低 | `#94A3B8`（slate-400） |
| **边框可见性** | `border-gray-200` | `border-white/10` |

---

## 使用Web Interface Guidelines审查

Vercel Web Interface Guidelines是最新的Web界面设计规范，包含：

1. **语义化HTML** - 使用正确的HTML5元素
2. **无障碍** - ARIA、键盘导航、焦点管理
3. **响应式** - 移动优先、流体布局
4. **性能** - 图片优化、懒加载、代码分割
5. **国际化** - RTL支持、多语言

获取最新规则：
```bash
curl https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```
