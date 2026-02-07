#!/usr/bin/env python3
"""
History to Instincts Converter

将 ~/.claude/history.jsonl 转换为可用的观察数据或直接提取 Instincts

用法:
  python3 utils/history-to-instincts.py --analyze      # 分析模式
  python3 utils/history-to-instincts.py --to-observations  # 转换为观察数据
  python3 utils/history-to-instincts.py --extract-instincts # 提取 instincts
  python3 utils/history-to-instincts.py --export-yaml   # 导出为 YAML 格式
"""

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

# 配置
HISTORY_FILE = Path.home() / ".claude" / "history.jsonl"
OBSERVATIONS_FILE = Path.home() / ".claude" / "homunculus" / "observations.jsonl"
INSTINCTS_DIR = Path.home() / ".claude" / "homunculus" / "instincts" / "personal"


def load_history():
    """加载历史记录"""
    entries = []
    with open(HISTORY_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    entries.append(json.loads(line))
                except:
                    pass
    return entries


def analyze_patterns(entries):
    """分析历史模式"""
    print("=" * 60)
    print("历史记录分析")
    print("=" * 60)
    print()

    # 基本统计
    print(f"总记录数: {len(entries)}")

    timestamps = [e.get('timestamp', 0) for e in entries if e.get('timestamp')]
    if timestamps:
        ts_min = min(timestamps) / 1000
        ts_max = max(timestamps) / 1000
        dt_min = datetime.fromtimestamp(ts_min)
        dt_max = datetime.fromtimestamp(ts_max)
        print(f"时间范围: {dt_min.strftime('%Y-%m-%d %H:%M')} 到 {dt_max.strftime('%Y-%m-%d %H:%M')}")
        print(f"持续时间: {(ts_max - ts_min) / 86400:.1f} 天")

    # 命令分析
    displays = [e.get('display', '') for e in entries]
    print(f"\n唯一命令数: {len(set(displays))}")

    print("\n前 50 个最常用命令:")
    for cmd, count in Counter(displays).most_common(50):
        bar = '█' * min(50, count // 2)
        print(f"  {count:4d}  {cmd:50s} {bar}")

    # 项目分析
    projects = [e.get('project', '') for e in entries]
    print(f"\n项目数: {len(set(projects))}")
    print("\n前 10 个项目:")
    for proj, count in Counter(projects).most_common(10):
        print(f"  {count:4d}  {proj}")

    # 会话分析
    sessions = [e.get('sessionId', '') for e in entries]
    print(f"\n总会话数: {len(set(sessions))}")

    # 模式识别
    print("\n" + "=" * 60)
    print("识别的模式")
    print("=" * 60)

    # 识别以 / 开头的命令（Claude Code 命令）
    commands = [d for d in displays if d.startswith('/')]
    print(f"\nClaude Code 命令: {len(commands)}")
    print("前 20 个:")
    for cmd, count in Counter(commands).most_common(20):
        print(f"  {count:4d}  {cmd}")

    # 识别中文命令
    chinese_commands = [d for d in displays if any('\u4e00' <= c <= '\u9fff' for c in d)]
    print(f"\n中文命令: {len(chinese_commands)}")
    print("前 20 个:")
    for cmd, count in Counter(chinese_commands).most_common(20):
        if len(cmd) > 50:
            cmd = cmd[:50] + "..."
        print(f"  {count:4d}  {cmd}")

    # 识别工作流模式
    print("\n" + "=" * 60)
    print("潜在的工作流模式")
    print("=" * 60)

    # 按项目分组，识别每个项目的常用命令
    project_commands = defaultdict(list)
    for e in entries:
        proj = e.get('project', '')
        cmd = e.get('display', '')
        if proj and cmd:
            project_commands[proj].append(cmd)

    print("\n各项目的常用命令:")
    proj_count = Counter(project_commands.keys())
    for proj, _ in proj_count.most_common(5):
        print(f"\n  {proj}:")
        cmds = project_commands[proj]
        cmd_count = Counter(cmds)
        for cmd, count in cmd_count.most_common(5):
            display_cmd = cmd[:50] + "..." if len(cmd) > 50 else cmd
            print(f"    {count:3d}  {display_cmd}")


def convert_to_observations(entries):
    """将历史记录转换为观察数据格式"""
    OBSERVATIONS_FILE.parent.mkdir(parents=True, exist_ok=True)

    # 转换每个历史条目为观察记录
    observations = []
    for entry in entries:
        timestamp = entry.get('timestamp', 0)
        if timestamp:
            dt = datetime.fromtimestamp(timestamp / 1000)
            iso_time = dt.isoformat() + 'Z'
        else:
            iso_time = datetime.utcnow().isoformat() + 'Z'

        observation = {
            'timestamp': iso_time,
            'event': 'user_command',
            'command': entry.get('display', ''),
            'project': entry.get('project', ''),
            'session': entry.get('sessionId', ''),
            'source': 'history.jsonl'
        }
        observations.append(observation)

    # 写入文件
    with open(OBSERVATIONS_FILE, 'a') as f:
        for obs in observations:
            f.write(json.dumps(obs) + '\n')

    print(f"✅ 已写入 {len(observations)} 条观察记录到 {OBSERVATIONS_FILE}")


def extract_instincts(entries):
    """从历史记录中提取 Instincts"""
    INSTINCTS_DIR.mkdir(parents=True, exist_ok=True)

    # 分析命令模式
    displays = [e.get('display', '') for e in entries]

    # 提取常用命令模式
    command_patterns = []
    for cmd, count in Counter(displays).most_common():
        if count >= 3:  # 至少出现 3 次
            # 计算置信度（基于出现频率）
            confidence = min(0.95, 0.3 + (count / len(entries)) * 10)

            # 确定领域
            if cmd.startswith('/'):
                domain = 'claude-commands'
            elif any(c in cmd for c in ['git', 'commit', 'push', 'pull', 'branch']):
                domain = 'git-workflow'
            elif any(c in cmd for c in ['test', 'spec', 'mock']):
                domain = 'testing'
            elif any(c in cmd for c in ['部署', '发布', 'build']):
                domain = 'deployment'
            elif any('\u4e00' <= c <= '\u9fff' for c in cmd):
                domain = 'chinese-workflow'
            else:
                domain = 'general'

            command_patterns.append({
                'command': cmd,
                'count': count,
                'confidence': confidence,
                'domain': domain
            })

    # 按领域分组
    by_domain = defaultdict(list)
    for p in command_patterns:
        by_domain[p['domain']].append(p)

    # 为每个领域创建 Instinct
    for domain, patterns in by_domain.items():
        if not patterns:
            continue

        # 选择该领域中最有代表性的模式
        patterns.sort(key=lambda x: -x['confidence'])

        instinct_id = f"{domain.replace('-', '-')}-patterns"
        trigger_examples = [p['command'] for p in patterns[:5]]

        # 创建 Instinct YAML
        output = f"""---
id: {instinct_id}
trigger: when user uses commands in {domain} domain
confidence: {sum(p['confidence'] for p in patterns) / len(patterns):.2f}
domain: {domain}
source: history-analysis
---
## Context

用户在 {domain} 领域中有 {len(patterns)} 种常用命令模式。

## Trigger Patterns

用户经常使用以下命令:

"""

        for p in patterns[:10]:
            output += f"- `{p['command']}` (使用 {p['count']} 次, 置信度 {p['confidence']:.0%})\n"

        output += f"""
## Action

当用户请求 {domain} 相关操作时:

1. 识别具体的命令模式
2. 根据历史使用频率预测下一步操作
3. 提供符合该领域惯例的建议
4. 考虑用户在此领域的常用工作流

## Statistics

- 总命令数: {len(patterns)}
- 总使用次数: {sum(p['count'] for p in patterns)}
- 平均置信度: {sum(p['confidence'] for p in patterns) / len(patterns):.0%}
"""

        # 写入文件
        output_file = INSTINCTS_DIR / f"{domain}-instincts.yaml"
        with open(output_file, 'w') as f:
            f.write(output)

        print(f"✅ 已创建 Instinct: {output_file}")

    print(f"\n总共创建了 {len(by_domain)} 个 Instinct 文件")


def export_as_yaml(entries, output_file=None):
    """导出为 YAML 格式"""
    if output_file is None:
        output_file = Path.cwd() / "history-instincts.yaml"

    # 分析数据
    displays = [e.get('display', '') for e in entries]

    yaml_content = f"""# History Instincts Export
# Generated: {datetime.utcnow().isoformat()}
# Source: ~/.claude/history.jsonl
# Total entries: {len(entries)}

version: "2.0"
exported_by: "history-to-instincts converter"
export_date: "{datetime.utcnow().isoformat()}"

instincts:
"""

    # 添加常用命令作为 instincts
    for cmd, count in Counter(displays).most_common(50):
        if count < 3:
            continue

        confidence = min(0.95, 0.3 + (count / len(entries)) * 10)

        # 确定领域
        if cmd.startswith('/'):
            domain = 'claude-commands'
        elif any(c in cmd for c in ['git', 'commit', 'push', 'pull']):
            domain = 'git-workflow'
        elif any(c in cmd for c in ['test', 'spec']):
            domain = 'testing'
        elif any('\u4e00' <= c <= '\u9fff' for c in cmd):
            domain = 'chinese-workflow'
        else:
            domain = 'general'

        # 生成安全的 ID
        safe_id = cmd.lower().replace('/', '-').replace(' ', '-')[:30]
        safe_id = ''.join(c if c.isalnum() or c in '-_' else '-' for c in safe_id)

        yaml_content += f"""  - id: {safe_id}
    trigger: "{cmd[:50]}"
    action: "Execute or assist with this command pattern"
    confidence: {confidence:.1f}
    domain: {domain}
    observations: {count}

"""

    with open(output_file, 'w') as f:
        f.write(yaml_content)

    print(f"✅ 已导出到 {output_file}")


def main():
    parser = argparse.ArgumentParser(description='将 history.jsonl 转换为 Instincts')
    parser.add_argument('--analyze', action='store_true', help='分析历史模式')
    parser.add_argument('--to-observations', action='store_true', help='转换为观察数据')
    parser.add_argument('--extract-instincts', action='store_true', help='提取 Instincts')
    parser.add_argument('--export-yaml', nargs='?', const='history-instincts.yaml', help='导出为 YAML 格式')
    parser.add_argument('--all', action='store_true', help='执行所有操作')

    args = parser.parse_args()

    # 加载历史记录
    print(f"正在加载 {HISTORY_FILE}...")
    entries = load_history()
    print(f"已加载 {len(entries)} 条记录\n")

    if args.all:
        args.analyze = True
        args.to_observations = True
        args.extract_instincts = True
        args.export_yaml = args.export_yaml or 'history-instincts.yaml'

    if not any([args.analyze, args.to_observations, args.extract_instincts, args.export_yaml]):
        parser.print_help()
        return

    if args.analyze:
        analyze_patterns(entries)
        print()

    if args.to_observations:
        print("转换为观察数据...")
        convert_to_observations(entries)
        print()

    if args.extract_instincts:
        print("提取 Instincts...")
        extract_instincts(entries)
        print()

    if args.export_yaml:
        print(f"导出为 YAML...")
        export_as_yaml(entries, args.export_yaml if isinstance(args.export_yaml, str) else None)
        print()


if __name__ == '__main__':
    main()
