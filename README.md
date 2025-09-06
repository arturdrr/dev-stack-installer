# 🚀 Dev Stack Installer

**Complete Developer Environment Setup for Debian/Ubuntu and derivatives.**

This repository contains a modular and customizable script to automate the installation of essential development tools, modern CLI utilities, and their configurations.

![demo](https://user-images.githubusercontent.com/12345/12345678-abcdef.gif) <!-- Placeholder for a future demo gif -->

## ⚡ Quick Start

Get up and running with a single command. This will clone the repository and start the interactive installation.

```bash
git clone https://github.com/arturdrr/dev-stack-installer.git
cd dev-stack-installer
chmod +x install.sh
./install.sh
```

## 🛠️ What Gets Installed

This script can install a wide range of tools, organized into modules.

### Modern CLI Tools
- **`eza`** - A modern replacement for `ls`.
- **`bat`** - A `cat` clone with syntax highlighting and Git integration.
- **`fzf`** - A general-purpose command-line fuzzy finder.
- **`ripgrep` (`rg`)** - A line-oriented search tool that recursively searches your current directory for a regex pattern.
- **`fd`** - A simple, fast and user-friendly alternative to `find`.
- **`zoxide`** - A smarter `cd` command that learns your habits.
- **`starship`** - The minimal, blazing-fast, and infinitely customizable prompt for any shell!

➡️ **[View the complete list of tools in `docs/TOOLS-LIST.md`](docs/TOOLS-LIST.md)**

### Development Environments
- **Node.js** - Installed via NodeSource to ensure the latest versions.
- **Python** - Using the system's Python 3 and `pip`, with `venv` for environment management.
- **Go** - (Optional) Latest stable version.

### Editors & IDEs
- **VS Code** - (Optional) The most popular code editor.
- **Vim/Nano** - Essential terminal editors, usually pre-installed.

## 📊 Installation Options

The installer is modular. You can choose to install everything or only specific parts.

```bash
# Run the full installation (default)
./install.sh

# Install only the modern CLI tools
./install.sh --cli-tools

# Install only development environments (Node, Python)
./install.sh --dev-env

# Apply configurations (aliases, etc.) without installing tools
./install.sh --config-only

# See what would be installed without actually installing anything
./install.sh --dry-run
```

## 🎯 Compatibility

This script is tested and confirmed to work on:

- ✅ Debian 11+ (Bullseye)
- ✅ Ubuntu 20.04+ (Focal)
- ✅ Pop!_OS 20.04+
- ✅ Other Debian/Ubuntu-based distributions

## 📖 Documentation

- **[Complete Tools List](docs/TOOLS-LIST.md)**: A full list of every tool the script can install.
- **[Customization Guide](docs/CUSTOMIZATION.md)**: Learn how to add or remove tools from the installation.
- **[Troubleshooting Guide](docs/TROUBLESHOOTING.md)**: Solutions to common problems.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/arturdrr/dev-stack-installer/issues).

Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
