#!/bin/bash
# Este script clona e instala o repositório dev-stack-installer.

# Termina o script se algum comando falhar.
set -e

# --- CONFIGURAÇÃO ---
# ATENÇÃO: Substitua esta URL pela URL correta do repositório.
REPO_URL="https://github.com/exemplo-org/dev-stack-installer.git"
CLONE_DIR="dev-stack-installer"


echo "A clonar o repositório de $REPO_URL..."

# Clona o repositório. Se o diretório já existir, atualiza com as últimas alterações.
if [ -d "$CLONE_DIR" ]; then
    echo "O diretório $CLONE_DIR já existe. A buscar as últimas alterações..."
    cd "$CLONE_DIR"
    git pull
    cd ..
else
    git clone "$REPO_URL" "$CLONE_DIR"
fi

echo "A aceder ao diretório do repositório..."
cd "$CLONE_DIR"

echo "O clone/pull foi concluído."
echo "Verifique a documentação do repositório para os passos de instalação específicos."
echo "Os exemplos de comandos de instalação estão comentados abaixo neste script."

# --- PASSOS DE INSTALAÇÃO ESPECÍFICOS ---
# Descomente e ajuste as seções relevantes abaixo, conforme necessário.

# Exemplo para projetos Python com um ficheiro de requisitos:
# if [ -f "requirements.txt" ]; then
#     echo "Encontrado requirements.txt, a instalar dependências..."
#     pip install -r requirements.txt
# fi

# Exemplo para projetos com um Makefile:
# if [ -f "Makefile" ]; then
#     echo "Encontrado Makefile, a executar 'make install'..."
#     # ou 'make', dependendo do projeto
#     make install
# fi

# Exemplo para projetos com um script de instalação específico:
# if [ -f "install.sh" ]; then
#     echo "Encontrado install.sh, a executá-lo..."
#     chmod +x install.sh
#     ./install.sh
# fi

# Exemplo para projetos Node.js:
# if [ -f "package.json" ]; then
#     echo "Encontrado package.json, a instalar dependências..."
#     npm install
# fi

echo "Script finalizado."
