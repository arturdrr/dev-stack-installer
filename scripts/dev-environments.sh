#!/bin/bash
# scripts/dev-environments.sh

log_info "Setting up development environments..."

if [ "${DRY_RUN:-false}" = true ]; then
    log_warning "DRY RUN: Would set up Node.js via NodeSource."
    log_warning "DRY RUN: Would install npm packages: eslint, prettier."
else
    # Install Node.js and npm
    log_info "Installing Node.js..."
    curl -fsSL https://deb.nodesource.com/setup_current.x | sudo -E bash -
    sudo apt-get install -y nodejs

    # Install global npm packages
    log_info "Installing global npm packages (eslint, prettier)..."
    sudo npm install -g eslint prettier

    log_success "Development environments set up."
fi
