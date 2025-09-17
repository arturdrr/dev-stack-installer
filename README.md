# 💻 Dev Stack Ultra Completa

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org/)
<!-- Add GitHub Actions Workflow Status Badge here if applicable -->
<!-- Example: ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/arturdrr/dev-stack-installer/main?label=build) -->

Scripts e configurações para configurar uma Dev Stack completa e otimizada para ambientes locais e servidores VPS Debian/Ubuntu.

---

## 📁 Estrutura do Repositório

- **local-install/**  
  Scripts e configurações para instalação no ambiente local (sua máquina).

- **vps-install/**  
  Scripts e configurações para instalação completa em servidores VPS.

- **docs/**  
  Documentação adicional sobre arquitetura, melhores práticas e tópicos relacionados.

---

## ⚙️ Como Usar

### Instalação guiada e inteligente (interativa)

1. Clone o repositório:

```text
git clone https://github.com/arturdrr/dev-stack-installer.git
cd dev-stack-installer
```

2. Execute o instalador Python:

```text
python3 installer.py
```

3. Siga o menu interativo para escolher etapas ou iniciar a instalação completa.

---

### Instalação não interativa

- Para instalação local específica, confira os scripts em `local-install/`.
- Para instalação em VPS, utilize os scripts em `vps-install/`.

---

## 🔄 Ordem de Instalação Inteligente

- A instalação é feita em ordem lógica, garantindo dependências e ferramentas essenciais instaladas antes das dependentes.
- Cada etapa verifica se o componente já está instalado, evitando reinstalação desnecessária.
- Scripts falham de forma segura caso dependam de etapas não concluídas.
- Possibilidade de retomar instalação do último ponto salvo, mesmo após interrupções.
- Configurações adaptam-se conforme ambiente (local ou VPS), ativando os componentes relevantes.

---

## 📜 Logs e Checkpoints

- Logs detalhados são gravados em `devstack_install.log`.
- Ponto de checkpoint para retomada é armazenado em `install_checkpoint.txt`.

---

## 🛡️ Licença

Este projeto está licenciado sob a [Licença MIT](https://github.com/arturdrr/dev-stack-installer/blob/master/LICENSE).

---

## 🚀 Comece Já!

Configure seu ambiente de desenvolvimento completo e otimizado, seja localmente ou em servidores VPS, com máxima eficiência e facilidade!

---

Se precisar de suporte ou quiser sugerir melhorias, fique à vontade para abrir issues ou pull requests. Boa codificação! 🎉👨‍💻👩‍💻