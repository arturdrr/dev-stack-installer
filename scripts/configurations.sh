#!/bin/bash
# scripts/configurations.sh

log_info "Applying shell configurations..."

# Detect current shell
CURRENT_SHELL=$(basename "$SHELL")
CONFIG_FILE=""
SHELL_INIT_CMD=""

if [ "$CURRENT_SHELL" = "bash" ]; then
    CONFIG_FILE="$HOME/.bashrc"
    SHELL_INIT_CMD="bash"
elif [ "$CURRENT_SHELL" = "zsh" ]; then
    CONFIG_FILE="$HOME/.zshrc"
    SHELL_INIT_CMD="zsh"
else
    log_warning "Unsupported shell: $CURRENT_SHELL. Configuration will be appended to ~/.bashrc."
    CONFIG_FILE="$HOME/.bashrc"
    SHELL_INIT_CMD="bash" # Fallback to bash init commands
fi

CONFIG_BLOCK_HEADER="# --- Dev Stack Installer Configuration ---"

# Create .zshrc if it doesn't exist and zsh is detected
if [ "$CURRENT_SHELL" = "zsh" ] && [ ! -f "$CONFIG_FILE" ]; then
    log_info "Creating $CONFIG_FILE for zsh..."
    touch "$CONFIG_FILE"
fi

# Check if the configuration block already exists
if grep -q "$CONFIG_BLOCK_HEADER" "$CONFIG_FILE"; then
    log_warning "Configuration block already exists in $CONFIG_FILE. Skipping."
else
    if [ "${DRY_RUN:-false}" = true ]; then
        log_warning "DRY RUN: Would append configuration block to $CONFIG_FILE."
    else
        log_info "Appending configuration block to $CONFIG_FILE..."
        cat >> "$CONFIG_FILE" << EOL

# --- Dev Stack Installer Configuration ---
alias ls='eza'
alias ll='eza -la --git'
alias tree='eza --tree'
alias cat='bat --paging=always'
alias grep='rg'
alias find='fd'
alias top='btop'
alias df='duf'
alias du='du-dust'
alias ping='gping'

eval "$(zoxide init $SHELL_INIT_CMD)"
eval "$(starship init $SHELL_INIT_CMD)"
# --- End Dev Stack Installer Configuration ---

EOL
        log_success "Configuration applied. Please restart your shell or run 'source $CONFIG_FILE'"
    fi
fi