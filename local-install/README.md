# Instalação Local da Dev Stack

Este diretório contém os scripts e configurações para configurar sua Dev Stack em um ambiente de desenvolvimento local.

Para uma instalação guiada e inteligente, utilize o `installer.py` na raiz do repositório.

Se você preferir uma instalação não interativa específica para o ambiente local, pode executar o script `install_local.sh`:

```bash
cd local-install
chmod +x install_local.sh
./install_local.sh
```

## O que é Instalado

Este script instala as ferramentas essenciais para um ambiente de desenvolvimento local, incluindo:

- Git
- Python 3 e pip
- Node.js e npm
- GitHub CLI
- Ferramentas CLI modernas (fzf, ripgrep, bat, exa, lazygit, starship)
- tmux e zsh

## Configuração Pós-Instalação

Após a instalação, você precisará configurar manualmente o Gemini CLI, o terminal Warp e seu editor de código preferido.

## Licença

Este projeto está licenciado sob a [Licença MIT](../../LICENSE).