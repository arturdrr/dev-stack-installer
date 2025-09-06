#!/bin/bash
set -e

echo "Verifying installed tools..."

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# List of tools to verify
TOOLS=("exa" "bat" "rg" "fd" "fzf" "zoxide" "starship")

for tool in "${TOOLS[@]}"; do
    if command_exists "$tool"; then
        echo "✅ $tool is installed."
    else
        echo "❌ $tool is NOT installed."
        exit 1
    fi
done

echo "All essential tools verified successfully!"
