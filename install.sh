#!/bin/bash
# Dev Stack Installer - Complete Developer Environment Setup
# Repository: https://github.com/arturdrr/dev-stack-installer

# Exit on any error, undefined variable, or pipe failure
set -euo pipefail

# --- Configuration ---
SCRIPTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/scripts"

# --- Logging and Colors ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
log_warning() { echo -e "${YELLOW}[WARNING]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# --- Usage Information ---
show_usage() {
    cat << EOF
Dev Stack Installer - Complete Developer Environment Setup for Debian/Ubuntu

Usage: $0 [OPTIONS]

Options:
    --all              Install everything (base, cli tools, dev env, editors, configs)
    --base             Install base system tools (build-essential, curl, etc.)
    --cli-tools        Install only modern CLI tools (eza, bat, fzf, etc.)
    --dev-env          Install only development environments (Node, Python)
    --editors          Install only editors (VS Code)
    --config-only      Apply configurations only (aliases, shell configs)
    --dry-run          Show what would be done without executing
    -h, --help         Show this help message

Example:
    $0 --all           # Install everything
    $0 --cli-tools --dev-env # Install CLI tools and Dev environments

EOF
}

# --- Main Logic ---
main() {
    # Default to --all if no arguments are given
    if [ $# -eq 0 ]; then
        set -- "--all"
    fi

    # Parse arguments
    while [[ "$#" -gt 0 ]]; do
        case "$1" in
            --all)
                log_info "Running full installation..."
                source "${SCRIPTS_DIR}/base-system.sh"
                source "${SCRIPTS_DIR}/cli-tools.sh"
                source "${SCRIPTS_DIR}/dev-environments.sh"
                source "${SCRIPTS_DIR}/editors.sh"
                source "${SCRIPTS_DIR}/configurations.sh"
                shift
                ;;
            --base)
                source "${SCRIPTS_DIR}/base-system.sh"
                shift
                ;;
            --cli-tools)
                source "${SCRIPTS_DIR}/cli-tools.sh"
                shift
                ;;
            --dev-env)
                source "${SCRIPTS_DIR}/dev-environments.sh"
                shift
                ;;
            --editors)
                source "${SCRIPTS_DIR}/editors.sh"
                shift
                ;;
            --config-only)
                source "${SCRIPTS_DIR}/configurations.sh"
                shift
                ;;
            --dry-run)
                log_warning "DRY RUN: Showing what would be done."
                export DRY_RUN=true
                # Re-run with --all in dry-run mode
                $0 --all
                exit 0
                ;;
            -h|--help)
                show_usage
                exit 0
                ;;
            *)
                log_error "Unknown option: $1"
                show_usage
                exit 1
                ;;
        esac
    done

    log_success "Installation process finished!"
    log_info "Please restart your terminal or run 'source ~/.bashrc' to apply all changes."
}

main "$@"
