#!/bin/bash
# GitHub repository creation and push script for end-to-end-delivery plugin

set -e

REPO_DIR="/root/claude-workspace/end-to-end-delivery"
REPO_NAME="end-to-end-delivery"
REPO_DESCRIPTION="端到端价值交付闭环开发流程 - 整合superpowers、everything-claude-code、feature-dev三大插件优势"

cd "$REPO_DIR"

echo "=== Creating GitHub repository ==="

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "ERROR: GitHub CLI (gh) is not installed"
    echo ""
    echo "Please install it first:"
    echo "  # On Linux"
    echo "  curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg"
    echo "  echo \"deb [arch=\$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main\" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null"
    echo "  sudo apt update"
    echo "  sudo apt install gh"
    echo ""
    echo "  # Then authenticate"
    echo "  gh auth login"
    echo ""
    echo "Or create the repository manually at:"
    echo "  https://github.com/new"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo "ERROR: GitHub CLI is not authenticated"
    echo ""
    echo "Please run: gh auth login"
    exit 1
fi

# Create repository and push
echo "Creating repository: $REPO_NAME"
gh repo create "$REPO_NAME" \
  --public \
  --description "$REPO_DESCRIPTION" \
  --source="$REPO_DIR" \
  --push \
  --branch=main

echo ""
echo "=== Repository created successfully ==="
echo ""
echo "Repository URL: https://github.com/$(gh auth status | head -1 | awk '{print $3}')/$REPO_NAME"
echo ""
echo "You can now:"
echo "  - View the repository at the URL above"
echo "  - Clone it with: git clone https://github.com/$(gh auth status | head -1 | awk '{print $3}')/$REPO_NAME.git"
echo "  - Share the README.md link with others"
