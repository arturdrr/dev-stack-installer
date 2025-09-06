#!/bin/bash
# scripts/cli-tools.sh

log_info "Installing modern CLI tools..."

CLI_TOOLS=(
    "eza" 
    "bat" 
    "fzf" 
    "ripgrep" 
    "fd-find" 
    "du-dust" 
    "duf" 
    "htop" 
    "btop" 
    "tmux" 
    "jq" 
    "git-delta" 
    "gping"
)

if [ "${DRY_RUN:-false}" = true ]; then
    log_warning "DRY RUN: Would install apt packages: ${CLI_TOOLS[*]}"
    log_warning "DRY RUN: Would install zoxide via curl script."
    log_warning "DRY RUN: Would install starship via curl script."
else
    # Install tools from apt
    log_info "Installing tools via apt..."
    sudo apt-get install -y "${CLI_TOOLS[@]}"

    # Install zoxide
    log_info "Installing zoxide..."
    curl -sS https://raw.githubusercontent.com/ajeetdsouza/zoxide/main/install.sh | bash

    # Install starship
    log_info "Installing starship..."
    curl -sS https://starship.rs/install.sh | sh -s -- -y

    log_success "Modern CLI tools installed."
fi
