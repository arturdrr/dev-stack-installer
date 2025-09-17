#!/bin/bash

LOGFILE="local_install.log"
CHECKPOINTFILE="local_install_checkpoint.log"

log() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOGFILE"
}

save_checkpoint() {
  echo "$1" > "$CHECKPOINTFILE"
}

load_checkpoint() {
  if [ -f "$CHECKPOINTFILE" ]; then
    cat "$CHECKPOINTFILE"
  else
    echo ""
  fi
}

install_base_local() {
  log "Iniciando instalação base LOCAL..."
  sudo apt update && sudo apt upgrade -y
  sudo apt install -y git python3 python3-pip nodejs npm curl tmux zsh fzf ripgrep bat exa lazygit starship
  log "Base LOCAL instalada com sucesso."
  save_checkpoint "base_local"
}

install_github_cli_local() {
  if command -v gh &> /dev/null; then
    log "GitHub CLI já instalado LOCAL, pulando."
  else
    log "Instalando GitHub CLI LOCAL..."
    curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
    sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list
    sudo apt update
    sudo apt install -y gh
  fi
  save_checkpoint "github_cli_local"
}

install_gemini_cli_local() {
  # Ajuste conforme documentação oficial da Gemini CLI
  if command -v gemini &> /dev/null; then
    log "Gemini CLI já instalado LOCAL, pulando."
  else
    log "Instalando Gemini CLI LOCAL..."
    curl -fsSL https://someurl.com/install_gemini.sh | bash
  fi
  save_checkpoint "gemini_cli_local"
}

# Fluxo principal local

last_step=$(load_checkpoint)

case "$last_step" in
  ""|"base_local")
    install_base_local
    ;;&
  "github_cli_local")
    install_github_cli_local
    ;;&
  "gemini_cli_local")
    install_gemini_cli_local
    ;;
  *)
    log "Instalação LOCAL concluída ou checkpoint desconhecido: $last_step"
    ;;
esac

log "Instalação LOCAL da dev stack finalizada."