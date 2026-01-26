#!/bin/bash
# Copy remaining plugin files from source to target

SOURCE="/root/.claude/plugins/marketplaces/end-to-end-delivery"
TARGET="/root/claude-workspace/end-to-end-delivery"

echo "=== Copying remaining plugin files ==="

# Create directories
mkdir -p "$TARGET/commands"
mkdir -p "$TARGET/agents"
mkdir -p "$TARGET/skills/end-to-end-workflow"
mkdir -p "$TARGET/skills/template-adapter"
mkdir -p "$TARGET/rules"
mkdir -p "$TARGET/templates/custom-workflow"
mkdir -p "$TARGET/templates/documentation"

# Copy remaining commands (5 files)
echo "Copying commands..."
cp "$SOURCE/commands/implement.md" "$TARGET/commands/"
cp "$SOURCE/commands/verify.md" "$TARGET/commands/"
cp "$SOURCE/commands/discovery.md" "$TARGET/commands/"
cp "$SOURCE/commands/design.md" "$TARGET/commands/"
cp "$SOURCE/commands/exploration.md" "$TARGET/commands/"

# Copy remaining agents (5 files)
echo "Copying agents..."
cp "$SOURCE/agents/exploration-agent.md" "$TARGET/agents/"
cp "$SOURCE/agents/design-agent.md" "$TARGET/agents/"
cp "$SOURCE/agents/implementation-agent.md" "$TARGET/agents/"
cp "$SOURCE/agents/verification-agent.md" "$TARGET/agents/"
cp "$SOURCE/agents/delivery-agent.md" "$TARGET/agents/"

# Copy skills (2 files)
echo "Copying skills..."
cp "$SOURCE/skills/end-to-end-workflow/SKILL.md" "$TARGET/skills/end-to-end-workflow/"
cp "$SOURCE/skills/template-adapter/SKILL.md" "$TARGET/skills/template-adapter/"

# Copy rules (3 files)
echo "Copying rules..."
cp "$SOURCE/rules/phase-gates.md" "$TARGET/rules/"
cp "$SOURCE/rules/quality-standards.md" "$TARGET/rules/"
cp "$SOURCE/rules/evidence-first.md" "$TARGET/rules/"

# Copy templates (3 files)
echo "Copying templates..."
cp "$SOURCE/templates/custom-workflow/simple-workflow.md" "$TARGET/templates/custom-workflow/"
cp "$SOURCE/templates/documentation/pr-template.md" "$TARGET/templates/documentation/"
cp "$SOURCE/templates/documentation/release-notes-template.md" "$TARGET/templates/documentation/"

echo "=== Copy complete ==="
echo "Total files copied: 18"
echo ""
echo "Directory structure:"
tree -L 2 "$TARGET" 2>/dev/null || find "$TARGET" -type f | sort
