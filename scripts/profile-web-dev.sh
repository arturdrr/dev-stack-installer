#!/bin/bash
# scripts/profile-web-dev.sh

log_info "Installing Web Development Profile tools..."

if [ "${DRY_RUN:-false}" = true ]; then
    log_warning "DRY RUN: Would add Docker's official GPG key and repository."
    log_warning "DRY RUN: Would install packages: docker-ce, docker-ce-cli, containerd.io, docker-compose-plugin."
    log_warning "DRY RUN: Would add user '${USER}' to the 'docker' group."
else
    # Add Docker's official GPG key
    log_info "Adding Docker GPG key..."
    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg

    # Add the Docker repository to Apt sources
    log_info "Adding Docker repository..."
    echo \
      "deb [arch=\"$(dpkg --print-architecture)\" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
      \"$(. /etc/os-release && echo \"$VERSION_CODENAME\")\" stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    
    # Update apt and install docker
    log_info "Updating package list and installing Docker..."
    sudo apt-get update
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

    # Add user to docker group to run docker without sudo
    log_info "Adding current user (${USER}) to the 'docker' group..."
    sudo usermod -aG docker "${USER}"
    log_warning "You may need to log out and log back in for the group change to take effect."

    log_success "Web Development Profile installed."
fi
