#!/bin/bash
# scripts/configurations.sh

log_info "Applying shell configurations..."

BASHRC_FILE="$HOME/.bashrc"
CONFIG_BLOCK_HEADER="# --- Dev Stack Installer Configuration ---"

# Check if the configuration block already exists
if grep -q "$CONFIG_BLOCK_HEADER" "$BASHRC_FILE"; then
    log_warning "Configuration block already exists in $BASHRC_FILE. Skipping."
else
    if [ "${DRY_RUN:-false}" = true ]; then
        log_warning "DRY RUN: Would append configuration block to $BASHRC_FILE."
    else
        log_info "Appending configuration block to $BASHRC_FILE..."
        cat >> "$BASHRC_FILE" << 'EOL'

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

eval "$(zoxide init bash)"
eval "$(starship init bash)"
# --- End Dev Stack Installer Configuration ---

EOL
        log_success "Configuration applied. Please restart your shell or run 'source ~/.bashrc'"
    fi
fi
