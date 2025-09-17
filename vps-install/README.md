# Instalação da Dev Stack Completa em VPS

Este diretório contém os scripts e configurações para configurar sua Dev Stack completa em um servidor VPS (Virtual Private Server).

Para uma instalação guiada e inteligente, utilize o `installer.py` na raiz do repositório.

Se você preferir uma instalação não interativa específica para o ambiente VPS, pode executar o script `install_vps.sh`:

```bash
cd vps-install
chmod +x install_vps.sh
./install_vps.sh
```

## O que é Instalado

Este script instala uma dev stack completa, incluindo:

- Git
- Python 3 e pip
- Node.js e npm
- Docker e Docker Compose
- GitHub CLI
- Ferramentas CLI modernas (fzf, ripgrep, bat, exa, lazygit, starship)
- tmux e zsh
- Kilo Code (Agente AI avançado)
- Spec Kit (Framework para desenvolvimento orientado por especificações)
- Gemini CLI (Assistente AI para geração e interpretação de scripts e código)
- GithubCloner (Clonagem massiva de repositórios)
- Prometheus e Grafana (Monitoramento)

## Configuração Pós-Instalação

Após a instalação, você precisará configurar tokens e personalizar os serviços conforme necessário (ex: `config.yaml` do Kilo Code, variáveis de ambiente para Gemini CLI).

## Licença

Este projeto está licenciado sob a [Licença MIT](../../LICENSE).