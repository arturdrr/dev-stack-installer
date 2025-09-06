# Contributing to dev-stack-installer

🎉 **Thank you for considering contributing!** Every contribution helps make this project better.

## 🚀 Getting Started

### Prerequisites
- Debian/Ubuntu system for testing
- Basic knowledge of Bash scripting
- Git installed

### Development Setup
```bash
git clone https://github.com/arturdrr/dev-stack-installer.git
cd dev-stack-installer
chmod +x install.sh
./install.sh --dry-run # Test without installing
```

## 🛠️ How to Contribute

### 1. Fork the Repository
Click the "Fork" button at the top of this repository.

### 2. Create a Feature Branch
```bash
git checkout -b feature/your-amazing-feature
```

### 3. Make Your Changes
- Follow existing code style
- Test your changes thoroughly
- Update documentation if needed

### 4. Commit Your Changes
Use conventional commit messages:
```bash
git commit -m "feat: add support for new tool"
git commit -m "fix: resolve installation issue"
git commit -m "docs: update README with new features"
```

### 5. Push and Create PR
```bash
git push origin feature/your-amazing-feature
```
Then create a Pull Request on GitHub.

## 📝 Commit Convention

- `feat:` - New features
- `fix:` - Bug fixes  
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

## 🐛 Bug Reports

Use our [bug report template](.github/ISSUE_TEMPLATE/bug_report.md) and include:
- OS version and distribution
- Steps to reproduce
- Expected vs actual behavior
- Error messages (if any)

## ✨ Feature Requests

Use our [feature request template](.github/ISSUE_TEMPLATE/feature_request.md) and:
- Describe the problem you're trying to solve
- Explain your proposed solution
- Consider the impact on existing users

## 🧪 Testing

Before submitting:

Run local tests:
```bash
./tests/verify-tools.sh
```

Run in different modes:
```bash
./install.sh --dry-run
./install.sh --cli-tools
```

## 📚 Documentation

- Update README.md for new features
- Add entries to CHANGELOG.md
- Update relevant docs/ files
- Include examples where helpful

## 💡 Questions?

- Open an issue for questions
- Check existing issues first
- Be respectful and constructive

## 🏆 Recognition

Contributors are recognized in our release notes and README acknowledgments.

---

**Thank you for making dev-stack-installer better!** 🙌
