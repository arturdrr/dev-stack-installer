# 🚀 Dev Stack Installer

![GitHub release](https://img.shields.io/github/v/release/arturdrr/dev-stack-installer)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Build Status](https://img.shields.io/github/actions/workflow/status/arturdrr/dev-stack-installer/test.yml)
![Platform](https://img.shields.io/badge/Platform-Debian%2FUbuntu-orange)

**Complete Developer Environment Setup for Debian/Ubuntu**

One-command installation of all essential development tools and modern CLI utilities.

## ⚡ Quick Start

```bash
git clone https://github.com/arturdrr/dev-stack-installer.git
cd dev-stack-installer
chmod +x install.sh
./install.sh --dry-run # Preview installation
./install.sh # Install everything
```

## 🛠️ What Gets Installed
- **Modern CLI Tools**: bat, eza, fzf, ripgrep, dust, duf
- **Editors**: VS Code, Vim, nano
- **Development Environments**: Node.js, Python, Git
- **Containerization**: Docker and Docker Compose for web development.

## 📊 Installation Options

The installation is modular. You can install everything or pick the parts you need.

### Core Modules
- `./install.sh --cli-tools` - CLI utilities only
- `./install.sh --dev-env` - Development environments (Node, Python)
- `./install.sh --editors` - Text editors only

### Installation Profiles
- `./install.sh --profile-web-dev` - Installs tools for web development (Docker, Docker Compose)

## 🤝 Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License
MIT License - see [LICENSE](LICENSE) file.
