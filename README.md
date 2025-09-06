# 🚀 Dev Stack Installer

[![Release](https://img.shields.io/github/v/release/arturdrr/dev-stack-installer)](https://github.com/arturdrr/dev-stack-installer/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/arturdrr/dev-stack-installer/blob/main/LICENSE)
[![Build Status](https://github.com/arturdrr/dev-stack-installer/actions/workflows/test.yml/badge.svg)](https://github.com/arturdrr/dev-stack-installer/actions/workflows/test.yml)
[![Platform](https://img.shields.io/badge/Platform-Debian%2FUbuntu-orange)](https://github.com/arturdrr/dev-stack-installer)
[![Shell](https://img.shields.io/badge/Shell-Bash-green)](https://github.com/arturdrr/dev-stack-installer)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Complete Developer Environment Setup for Debian/Ubuntu**

One-command installation of all essential development tools and modern CLI utilities - **100% Free & Open Source**.

---

## ✨ Features

- **🎯 Modular Installation**: Choose what to install (`--cli-tools`, `--dev-env`, `--editors`)
- **🛡️ Anti-Redundancy**: Smart detection prevents duplicate installations
- **⚡ 50+ Essential Tools**: Modern CLI utilities, editors, and development environments  
- **🆓 100% Open Source**: All tools are free and open source
- **🖥️ Terminal-First**: Complete workflow without leaving the command line
- **🔧 Idempotent**: Safe to run multiple times
- **🎨 Multi-Shell Support**: Bash, Zsh, Fish compatible

---

### 📊 What Makes This Different
- **Zero Configuration**: Works out of the box
- **Anti-Redundancy**: Smart detection prevents conflicts  
- **Community Driven**: Based on developer feedback
- **Future Proof**: Regular updates with latest tools

---

## 🚀 Quick Start

```bash
git clone https://github.com/arturdrr/dev-stack-installer.git
cd dev-stack-installer
chmod +x install.sh
./install.sh --dry-run # Preview what will be installed
./install.sh # Install everything
```

---

## 🛠️ What Gets Installed

### Modern CLI Tools
- **bat** - cat with syntax highlighting
- **exa** - ls replacement with git integration  
- **fzf** - command-line fuzzy finder
- **ripgrep** - ultra-fast text search
- **fd-find** - simple, fast alternative to find
- **dust** - human-readable disk usage
- **duf** - disk usage utility with visual output
- **zoxide** - smarter cd command
- **starship** - cross-shell prompt

### Multiple Editors
- **Neovim** - modern vim with LSP support
- **Helix** - modern modal editor written in Rust
- **Micro** - terminal-based text editor
- **Vim** - classic modal editor
- **Emacs** - extensible text editor
- **Nano** - simple terminal editor

### Development Environments
- **Node.js** (via NVM) - JavaScript runtime
- **Python** - with pip and virtualenv
- **Git** - with optimized configuration

### System Tools
- **tmux** - terminal multiplexer
- **htop/btop** - system monitoring
- **jq** - JSON processor
- **httpie** - human-friendly HTTP client
- **lazygit** - simple terminal UI for git

---

## 📊 Installation Options

```bash
./install.sh --all # Install everything (default)
./install.sh --cli-tools # Modern CLI utilities only
./install.sh --dev-env # Development environments only
./install.sh --editors # Text editors only
./install.sh --dry-run # Preview installation without changes
./install.sh --help # Show all options
```

---

## 🎯 Compatibility

- ✅ **Debian 11+** (Bullseye)
- ✅ **Ubuntu 20.04+** (Focal)
- ✅ **Pop!_OS 20.04+**
- ✅ **Linux Mint 20+**

---

## ⚙️ Configuration

After installation, reload your shell:

```bash
source ~/.bashrc
```

The installer automatically adds modern aliases:
```bash
ls → exa # Modern ls with colors
cat → bat # cat with syntax highlighting
grep → ripgrep # Ultra-fast search
find → fd # Simple and fast find
```

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md).

### Quick Contribution Guide
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: Add amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 Documentation

- [Tools List](docs/TOOLS-LIST.md) - Complete list of included tools
- [Troubleshooting](docs/TROUBLESHOOTING.md) - Common issues and solutions
- [Customization](docs/CUSTOMIZATION.md) - How to customize your setup
- [FAQ](docs/FAQ.md) - Frequently asked questions
- [Useful Links](docs/USEFUL-LINKS.md) - Curated list of helpful resources

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Thanks to all the amazing open-source projects and their maintainers
- Inspired by the need for a modern, efficient development environment
- Built with ❤️ for the Linux development community

---

## ⭐ Show Your Support

Give a ⭐ if this project helped you set up your development environment!

---

**Made with ❤️ for developers who love the command line**