Documentação: Instalação Modular do Dev-Stack Local + VPS
Visão Geral
Este guia explica como instalar e manter um ambiente de desenvolvimento completo usando o dev-stack-installer, com configurações separadas e controladas para VPS e computador local, garantindo flexibilidade e produtividade máxima.

Requisitos
Acesso SSH configurado da máquina local para VPS, com chaves SSH (sem senha) preferencialmente

Repositório dev-stack clonado em ambas máquinas nas pastas desejadas

Permissão para executar scripts shell

Passos de Instalação
1. Instalação no VPS
Conecte-se via SSH e execute o instalador:

bash
ssh user@vps "cd /caminho/para/dev-stack-installer && ./install.sh --all"
Isso instala o dev-stack completo na VPS.

2. Instalação no Computador Local
No seu computador, execute a instalação local:

bash
cd /caminho/para/dev-stack-installer
./install.sh --all
Instala o dev-stack completo localmente.

3. Script automatizado (opcional)
Use o script abaixo para fazer instalação sequencial VPS + local com opções ajustadas:

bash
#!/bin/bash

VPS_USER="user"
VPS_HOST="vps.exemplo.com"
DEVSTACK_PATH="/caminho/para/dev-stack-installer"

echo "Instalando na VPS..."
ssh ${VPS_USER}@${VPS_HOST} << EOF
cd ${DEVSTACK_PATH} || exit
./install.sh --all || exit
EOF

if [ $? -ne 0 ]; then
  echo "Erro na instalação da VPS."
  exit 1
fi

echo "Instalando localmente..."
cd ${DEVSTACK_PATH} || exit
./install.sh --all || exit

echo "Instalação no local e VPS concluída!"
Salve como install_both.sh, torne executável (chmod +x install_both.sh) e execute.

Personalização
Use flags para instalar somente módulos específicos:

--cli-tools

--dev-env

--editors

Ajuste caminhos e usuário SSH conforme necessário.

Recomendações
Mantenha o repositório atualizado em ambos ambientes com git pull regularmente.

Utilize ferramentas como rsync para sincronizar arquivos fora do git quando necessário.
