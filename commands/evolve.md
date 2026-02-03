---
description: 演化 Instincts 为 Skills/Commands/Agents（v3.0 continuous-learning-v2 演化系统）
argument-hint: (可选) 演化选项
---

# Evolve Command

演化 instincts 为更高层次的结构（skills/commands/agents）。

## 使用方法

```bash
/evolve                    # 分析所有 instincts 并建议演化
/evolve --domain testing   # 仅演化测试域的 instincts
/evolve --dry-run          # 显示将要创建的内容而不实际创建
/evolve --threshold 5      # 需要 5+ 相关 instincts 才能聚类
```

## 功能

分析 instincts 并将相关的聚类为：
- **Commands**: 用户会显式请求的操作
- **Skills**: 自动触发行为
- **Agents**: 复杂的多步骤流程

## 演化规则

### → Command（用户调用）
当 instincts 描述用户会显式请求的操作时：
- 多个 instincts 关于"当用户要求..."
- 触发器如"当创建新 X"
- 可重复的序列

### → Skill（自动触发）
当 instincts 描述应该自动发生的行为时：
- 模式匹配触发器
- 错误处理响应
- 代码风格强制执行

### → Agent（复杂流程）
当 instincts 描述复杂的多步骤流程时：
- 需要多步骤才能完成
- 需要工具调用
- 需要决策树

## 输出

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/continuous-learning-v2/scripts/instinct-cli.py" evolve "$@"
```
