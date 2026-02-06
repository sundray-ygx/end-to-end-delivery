---
description: 导出 Instincts 到文件，用于分享或备份（v3.0 continuous-learning-v2）
argument-hint: (可选) 导出选项
---

# /instinct-export - Instinct 导出命令 v3.0

导出 instincts 到文件，用于分享或备份。

## 使用方法

```bash
/instinct-export
```

## 功能

- 将所有 instincts 导出到 JSON 文件
- 支持按域过滤
- 生成可分享的导出文件

## 输出

```bash
# 运行 instinct CLI
python3 "${CLAUDE_PLUGIN_ROOT}/skills/continuous-learning-v2/scripts/instinct-cli.py" export
```
