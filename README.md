# Dev Stack Installer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org/)

---

## Visão Geral

O **Dev Stack Installer** é um script abrangente para configurar ambientes de desenvolvimento Dev Stack, tanto localmente quanto em VPS. Ele oferece instalação modular, com perfis básicos e pesados, suportando desde setups mínimos até ambientes completos para desenvolvimento avançado.  

---

## Recursos

- Instalação local, VPS ou ambas (sequencialmente)  
- Perfis personalizáveis:  
  - **Básico**: pacotes essenciais para um ambiente funcional leve  
  - **Pesado**: instalação completa com ferramentas avançadas  
- Interface de linha de comando elegante com menu interativo e colorido (usa [rich](https://github.com/Textualize/rich))  
- Suporte a execução não interativa via argumentos de linha de comando para automação  
- Bootstrap integrado: instala automaticamente dependências essenciais como `rich`  
- Logs detalhados da instalação para análise de erros  

---

## Pré-requisitos

- Python 3.8 ou superior  
- Acesso sudo para instalação de pacotes locais (para instalações locais)  
- Acesso SSH válido com permissões para executar comandos na VPS (para instalações remotas)

---

## Instruções de Uso

### Modo Interativo (padrão)

Basta executar o instalador sem parâmetros para navegar pelos menus:

```text
python devstack_installer.py
```

Você poderá escolher onde instalar (local, VPS, ambos) e o perfil de instalação (básico ou pesado).

---

### Modo Não Interativo (Automatizado)

Permite execução automatizada, útil para scripts, CI/CD, e outras integrações:

```text
python devstack_installer.py --mode <local|vps|both> --profile <1|2> [--user <SSH_USER>] [--host <SSH_HOST>]
```

- `--mode` (obrigatório): Escolha onde instalar  
- `--profile` (obrigatório): 1 para básico, 2 para pesado  
- `--user` e `--host` (opcionais, para `vps` ou `both`): Dados para conexão SSH  

**Exemplos:**

- Instalar local com perfil básico:

```text
python devstack_installer.py --mode local --profile 1
```

- Instalar VPS com perfil pesado:

```text
python devstack_installer.py --mode vps --profile 2 --user usuario --host endereco.vps.com
```

- Instalar ambos com perfil básico:

```text
python devstack_installer.py --mode both --profile 1 --user usuario --host endereco.vps.com
```

---

## Estrutura do Projeto

```text
.
├── devstack_installer.py # Script principal do instalador
├── README.md # Este arquivo de documentação
├── install_local.sh # Script auxiliar para instalação local
├── other-scripts-or-files # Outros arquivos complementares
└── ...
```

---

## Contribuição

Contribuições são bem-vindas! Para sugerir melhorias ou corrigir problemas:

1. Fork este repositório  
2. Crie uma branch para sua feature (`git checkout -b minha-feature`)  
3. Faça commit das suas alterações (`git commit -m 'Minha feature'`)  
4. Faça push para sua branch (`git push origin minha-feature`)  
5. Abra um Pull Request

Por favor, mantenha o padrão de código consistente.

---

## Licença

Este projeto está licenciado sob a licença [MIT](LICENSE).

---

## Contato

Para dúvidas ou suporte, por favor abra uma issue.

---

_Desenvolvido com cuidado para atender equipes técnicas exigentes e ambientes DevOps._