#!/bin/bash
# scripts/base-system.sh

log_info "Installing base system packages..."

if [ "${DRY_RUN:-false}" = true ]; then
    log_warning "DRY RUN: Would run 'sudo apt-get update'"
    log_warning "DRY RUN: Would install packages: build-essential, git, curl, wget, python3-pip, python3-venv, python3-dev"
else
    sudo apt-get update
    sudo apt-get install -y build-essential git curl wget python3-pip python3-venv python3-dev
    log_success "Base system packages installed."
fi
