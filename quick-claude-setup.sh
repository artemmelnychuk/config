#!/bin/bash
# Quick Claude Code Setup for Embedded Devices

set -e

echo "Quick Claude Code Setup..."

# Install claude-code
echo "Installing @anthropic-ai/claude-code..."
sudo npm install -g @anthropic-ai/claude-code

# Create symlink
NPM_PREFIX=$(npm config get prefix)
CLAUDE_PATH="${NPM_PREFIX}/lib/node_modules/@anthropic-ai/claude-code/cli.js"
sudo ln -sf "$CLAUDE_PATH" /usr/local/bin/claude

echo "✓ Setup complete! Run 'claude --help' to get started."
