# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-09-06
### Added
- Initial release of the `dev-stack-installer`.
- Modular installation script (`install.sh`) with options for `--all`, `--cli-tools`, `--dev-env`, `--editors`, and `--config-only`.
- Base system setup (`build-essential`, `git`, `python`).
- Modern CLI tools module (`eza`, `bat`, `fzf`, `ripgrep`, etc.).
- Development environment module (Node.js, npm global packages).
- Editors module (VS Code).
- Configuration module (`.bashrc` aliases).
- Professional repository structure with documentation, issue templates, and CI/CD workflow.
- Basic test suite to verify tool installation.