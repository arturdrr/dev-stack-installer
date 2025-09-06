#!/bin/bash
# scripts/editors.sh

log_info "Installing editors..."

if [ "${DRY_RUN:-false}" = true ]; then
    log_warning "DRY RUN: Would install snapd and VS Code."
else
    log_info "Installing VS Code via snap..."
    # Ensure snapd is installed
    sudo apt-get install -y snapd
    # Install VS Code
    sudo snap install code --classic
    log_success "VS Code installed."
fi
