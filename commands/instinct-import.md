---
description: 从文件导入 Instincts（v3.0 continuous-learning-v2）
argument-hint: 导入文件路径
---

# Instinct Import Command

从文件导入 instincts。

## 使用方法

```bash
/instinct-import <file>
```

## 功能

- 从 JSON 文件导入 instincts
- 合并现有 instincts
- 更新置信度评分

## 输出

```bash
# 运行 instinct CLI
python3 "${CLAUDE_PLUGIN_ROOT}/skills/continuous-learning-v2/scripts/instinct-cli.py" import "${FILE}"
```
