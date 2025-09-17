#!/bin/bash

LOGFILE="vps_install.log"
CHECKPOINTFILE="vps_install_checkpoint.log"

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

install_base_vps() {
  log "Iniciando instalação base VPS..."
  sudo apt update && sudo apt upgrade -y
  sudo apt install -y git python3 python3-pip nodejs npm docker.io docker-compose curl jq htop tmux zsh fzf ripgrep bat exa lazygit starship
  sudo usermod -aG docker $USER
  log "Base VPS instalada com sucesso."
  save_checkpoint "base_vps"
}

install_github_cli_vps() {
  if command -v gh &> /dev/null; then
    log "GitHub CLI já instalado VPS, pulando."
  else
    log "Instalando GitHub CLI VPS..."
    curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
    sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list
    sudo apt update
    sudo apt install -y gh
  fi
  save_checkpoint "github_cli_vps"
}

install_kilocode_vps() {
  path="$HOME/kilocode"
  if [ -d "$path" ]; then
    log "Kilo Code já instalado VPS, pulando."
  else
    log "Clonando e instalando Kilo Code VPS..."
    git clone https://github.com/Kilo-Org/kilocode.git $path
    cd $path && ./install.sh
    cd -
    log "Kilo Code instalado VPS."
  fi
  save_checkpoint "kilocode_vps"
}

install_spec_kit_vps() {
  path="$HOME/spec-kit"
  if [ -d "$path" ]; then
    log "Spec Kit já instalado VPS, pulando."
  else
    log "Clonando e instalando Spec Kit VPS..."
    git clone https://github.com/github/spec-kit.git $path
    cd $path && pip3 install -r requirements.txt
    cd -
    log "Spec Kit instalado VPS."
  fi
  save_checkpoint "spec_kit_vps"
}

install_gemini_cli_vps() {
  if command -v gemini &> /dev/null; then
    log "Gemini CLI já instalado VPS, pulando."
  else
    log "Instalando Gemini CLI VPS..."
    curl -fsSL https://someurl.com/install_gemini.sh | bash
  fi
  save_checkpoint "gemini_cli_vps"
}

install_githubcloner_vps() {
  path="$HOME/githubcloner"
  if [ -d "$path" ]; then
    log "GithubCloner já instalado VPS, pulando."
  else
    log "Clonando e instalando GithubCloner VPS..."
    git clone https://github.com/mazen160/GithubCloner.git $path
    cd $path && pip3 install -r requirements.txt
    cd -
    log "GithubCloner instalado VPS."
  fi
  save_checkpoint "githubcloner_vps"
}

install_monitoring_vps() {
  log "Instalando Prometheus e Grafana no VPS..."
  sudo apt install -y prometheus grafana
  sudo systemctl enable --now prometheus grafana-server
  log "Monitoramento instalado VPS."
  save_checkpoint "monitoring_vps"
}

# Fluxo principal VPS

last_step=$(load_checkpoint)

case "$last_step" in
  ""|"base_vps")
    install_base_vps
    ;;&
  "github_cli_vps")
    install_github_cli_vps
    ;;&
  "kilocode_vps")
    install_kilocode_vps
    ;;&
  "spec_kit_vps")
    install_spec_kit_vps
    ;;&
  "gemini_cli_vps")
    install_gemini_cli_vps
    ;;&
  "githubcloner_vps")
    install_githubcloner_vps
    ;;&
  "monitoring_vps")
    install_monitoring_vps
    ;;
  *)
    log "Instalação VPS concluída ou checkpoint desconhecido: $last_step"
    ;;
esac

log "Instalação VPS da dev stack finalizada."