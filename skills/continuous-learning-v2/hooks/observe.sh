#!/bin/bash
# Continuous Learning v2 - Observation Hook
#
# Captures tool use events for pattern analysis.
# Claude Code passes hook data via stdin as JSON.

set -e

CONFIG_DIR="${HOME}/.claude/homunculus"
OBSERVATIONS_FILE="${CONFIG_DIR}/observations.jsonl"
MAX_FILE_SIZE_MB=10

# Ensure directory exists
mkdir -p "$CONFIG_DIR"

# Skip if disabled
if [ -f "$CONFIG_DIR/disabled" ]; then
  exit 0
fi

# Read JSON from stdin (Claude Code hook format)
INPUT_JSON=$(cat)

# Exit if no input
if [ -z "$INPUT_JSON" ]; then
  exit 0
fi

# Parse using python (pass JSON via environment to avoid shell escaping issues)
export INPUT_JSON
PARSED=$(python3 << 'PYEOF'
import json
import os
import sys

try:
    input_json = os.environ.get('INPUT_JSON', '')
    if not input_json:
        print(json.dumps({'parsed': False, 'error': 'No input'}))
        sys.exit(0)

    data = json.loads(input_json)

    # Extract fields - Claude Code hook format
    hook_type = data.get('hook_type', 'unknown')  # PreToolUse or PostToolUse
    tool_name = data.get('tool_name', data.get('tool', 'unknown'))
    tool_input = data.get('tool_input', data.get('input', {}))
    tool_output = data.get('tool_output', data.get('output', ''))
    session_id = data.get('session_id', 'unknown')

    # Truncate large inputs/outputs
    if isinstance(tool_input, dict):
        tool_input_str = json.dumps(tool_input)[:5000]
    else:
        tool_input_str = str(tool_input)[:5000]

    if isinstance(tool_output, dict):
        tool_output_str = json.dumps(tool_output)[:5000]
    else:
        tool_output_str = str(tool_output)[:5000]

    # Determine event type
    event = 'tool_start' if 'Pre' in hook_type else 'tool_complete'

    print(json.dumps({
        'parsed': True,
        'event': event,
        'tool': tool_name,
        'input': tool_input_str if event == 'tool_start' else None,
        'output': tool_output_str if event == 'tool_complete' else None,
        'session': session_id
    }))
except Exception as e:
    print(json.dumps({'parsed': False, 'error': str(e)}))
PYEOF
)

# Check if parsing succeeded
PARSED_OK=$(echo "$PARSED" | python3 -c "import json,sys; print(json.load(sys.stdin).get('parsed', False))")

if [ "$PARSED_OK" != "True" ]; then
  # Fallback: log raw input for debugging
  timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
  echo "{\"timestamp\":\"$timestamp\",\"event\":\"parse_error\",\"raw\":$(echo "$INPUT_JSON" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()[:1000]))')}" >> "$OBSERVATIONS_FILE"
  exit 0
fi

# Archive if file too large
if [ -f "$OBSERVATIONS_FILE" ]; then
  file_size_mb=$(du -m "$OBSERVATIONS_FILE" 2>/dev/null | cut -f1)
  if [ "${file_size_mb:-0}" -ge "$MAX_FILE_SIZE_MB" ]; then
    archive_dir="${CONFIG_DIR}/observations.archive"
    mkdir -p "$archive_dir"
    mv "$OBSERVATIONS_FILE" "$archive_dir/observations-$(date +%Y%m%d-%H%M%S).jsonl"
  fi
fi

# Build and write observation
timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

export PARSED
export OBSERVATIONS_FILE
export timestamp

python3 << 'PYEOF'
import json
import os

parsed = json.loads(os.environ.get('PARSED', '{}'))
observation = {
    'timestamp': os.environ.get('timestamp', ''),
    'event': parsed.get('event', ''),
    'tool': parsed.get('tool', ''),
    'session': parsed.get('session', '')
}

if parsed.get('input'):
    observation['input'] = parsed['input']
if parsed.get('output'):
    observation['output'] = parsed['output']

with open(os.environ.get('OBSERVATIONS_FILE'), 'a') as f:
    f.write(json.dumps(observation) + '\n')
PYEOF

# Signal observer if running
OBSERVER_PID_FILE="${CONFIG_DIR}/.observer.pid"
if [ -f "$OBSERVER_PID_FILE" ]; then
  observer_pid=$(cat "$OBSERVER_PID_FILE")
  if kill -0 "$observer_pid" 2>/dev/null; then
    kill -USR1 "$observer_pid" 2>/dev/null || true
  fi
fi

exit 0
