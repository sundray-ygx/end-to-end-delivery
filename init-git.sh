#!/bin/bash
# Git initialization and commit script for end-to-end-delivery plugin

set -e

REPO_DIR="/root/claude-workspace/end-to-end-delivery"
cd "$REPO_DIR"

echo "=== Initializing Git repository ==="

# Initialize git repository
git init

# Configure git user
git config user.name "Claude Code User"
git config user.email "claude@example.com"

echo "=== Adding all files to git ==="

# Add all files
git add .

echo "=== Creating initial commit ==="

# Create initial commit
git commit -m "Initial commit: end-to-end-delivery plugin v1.0.0

- 6 specialized agents for each delivery phase
- 2 core skills (end-to-end-workflow, template-adapter)
- 7 commands for complete workflow control
- 3 quality rules (phase-gates, quality-standards, evidence-first)

Core principles:
- Evidence Before Claims
- Quality First
- Continuous Learning

Integrates best practices from:
- superpowers: Subagent-Driven Development
- everything-claude-code: TDD Workflow
- feature-dev: Architecture Design

Co-Authored-By: Claude <noreply@anthropic.com>"

echo ""
echo "=== Git repository initialized successfully ==="
echo "Repository location: $REPO_DIR"
echo ""
echo "Next steps:"
echo "1. Run: bash create-github-repo.sh"
echo "   or manually create GitHub repo and run:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/end-to-end-delivery.git"
echo "   git branch -M main"
echo "   git push -u origin main"
