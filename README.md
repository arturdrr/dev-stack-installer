# 💻 Dev Stack Ultra Completa

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org/)
<!-- Add GitHub Actions Workflow Status Badge here if applicable -->
<!-- Example: ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/arturdrr/dev-stack-installer/main?label=build) -->

Scripts e configurações para configurar uma Dev Stack completa e otimizada para ambientes locais e servidores VPS Debian/Ubuntu.

---

## 💡 Visão Geral

O **Dev Stack Ultra Completa** é um conjunto robusto de scripts e configurações projetado para automatizar a configuração de ambientes de desenvolvimento completos e otimizados. Seja para sua máquina local ou para servidores VPS baseados em Debian/Ubuntu, este projeto garante uma instalação eficiente, inteligente e personalizável, permitindo que você comece a codificar rapidamente.

---

## ✨ Recursos Principais

-   **Instalação Guiada e Inteligente**: Um instalador Python interativo que guia você através do processo, oferecendo opções claras para cada etapa.
-   **Modos de Instalação Flexíveis**: Suporte para instalação local, em VPS, ou ambos sequencialmente, com perfis "Básico" e "Pesado" para atender às suas necessidades.
-   **Ordem de Instalação Otimizada**: Garante que as dependências e ferramentas essenciais sejam instaladas na ordem correta, minimizando erros.
-   **Resiliência e Retomada**: Capacidade de retomar a instalação do último ponto salvo, mesmo após interrupções, graças a um sistema de logs e checkpoints.
-   **Configurações Adaptáveis**: As configurações se ajustam automaticamente ao ambiente (local ou VPS), ativando apenas os componentes relevantes.
-   **Logs Detalhados**: Todos os passos da instalação são registrados em logs para fácil depuração e auditoria.
-   **Personalização Fácil**: Permite adaptar a instalação às suas preferências e necessidades específicas.

---

## 🛠️ Pré-requisitos

-   **Sistema Operacional**: Debian/Ubuntu (ou distribuições baseadas).
-   **Python**: Python 3.8 ou superior.
-   **Acesso Sudo**: Necessário para a instalação de pacotes no sistema local.
-   **Acesso SSH**: Para instalações em VPS, é necessário acesso SSH válido com permissões adequadas.

---

## ⚙️ Como Usar

### Instalação Guiada e Inteligente (Interativa)

Esta é a forma recomendada para a maioria dos usuários. O instalador Python irá guiá-lo através das opções de instalação.

1.  **Clone o repositório**:
    ```bash
    git clone https://github.com/arturdrr/dev-stack-installer.git
    cd dev-stack-installer
    ```

2.  **Execute o instalador Python**:
    ```bash
    python3 installer.py
    ```

3.  **Siga o menu interativo**: Escolha entre instalar localmente, em uma VPS, ou ambos, e selecione o perfil de instalação (Básico ou Pesado) conforme suas necessidades.

### Instalação Não Interativa (Automatizada)

Para automação ou integração em scripts, você pode usar o modo não interativo, passando os parâmetros diretamente na linha de comando.

```bash
python3 installer.py --mode <local|vps|both> --profile <1|2> [--user <SSH_USER>] [--host <SSH_HOST>]
```

-   `--mode` (obrigatório): Define onde instalar (`local`, `vps`, ou `both`).
-   `--profile` (obrigatório): `1` para perfil Básico, `2` para perfil Pesado.
-   `--user` e `--host` (opcionais): Necessários para instalações em VPS, especificam o usuário e o endereço do servidor.

**Exemplos**:

-   Instalar localmente com perfil básico:
    ```bash
    python3 installer.py --mode local --profile 1
    ```
-   Instalar em VPS com perfil pesado:
    ```bash
    python3 installer.py --mode vps --profile 2 --user seu_usuario --host seu_vps.com
    ```

---

## 🔄 Ordem de Instalação Inteligente

O instalador segue uma sequência lógica para garantir que todas as ferramentas e dependências sejam configuradas corretamente.

-   **Verificação de Dependências**: Ferramentas essenciais são instaladas antes de seus dependentes.
-   **Idempotência**: Cada etapa verifica se o componente já está presente, evitando reinstalações desnecessárias e garantindo que o script possa ser executado múltiplas vezes sem efeitos colaterais indesejados.
-   **Tratamento de Falhas**: Scripts são projetados para falhar de forma segura, com mensagens claras caso uma etapa não possa ser concluída.
-   **Retomada Automática**: Em caso de interrupção, o sistema de checkpoints permite que a instalação seja retomada do último ponto de sucesso.
-   **Adaptação de Ambiente**: As configurações são dinamicamente ajustadas para otimizar o desempenho e a compatibilidade, seja em um ambiente local de desenvolvimento ou em um servidor de produção.

---

## 📜 Logs e Checkpoints

Para garantir transparência e facilitar a depuração:

-   **Logs Detalhados**: Todas as ações e resultados da instalação são registrados em `devstack_install.log`, fornecendo um histórico completo do processo.
-   **Ponto de Checkpoint**: Um arquivo `install_checkpoint.txt` é mantido para registrar o progresso, permitindo que a instalação seja retomada de onde parou em caso de interrupções.

---

## 🎨 Personalização

O instalador é projetado para ser flexível. Você pode:

-   **Editar Perfis**: Modificar os scripts dentro de `local-install/` e `vps-install/` para adicionar ou remover pacotes e configurações.
-   **Adicionar Ferramentas**: Estender os scripts para incluir a instalação de suas ferramentas e frameworks favoritos.

---

## ❓ Solução de Problemas (Troubleshooting)

-   **"Comando não encontrado"**: Verifique se o Python 3 está instalado e no seu PATH.
-   **Erros de Permissão**: Certifique-se de que você tem permissões `sudo` para instalar pacotes.
-   **Problemas de Conexão SSH**: Verifique suas credenciais SSH e a conectividade com a VPS.
-   **Logs**: Consulte `devstack_install.log` para mensagens de erro detalhadas.

---

## 🛡️ Licença

Este projeto está licenciado sob a [Licença MIT](https://github.com/arturdrr/dev-stack-installer/blob/master/LICENSE).

---

## 🚀 Comece Já!

Configure seu ambiente de desenvolvimento completo e otimizado, seja localmente ou em servidores VPS, com máxima eficiência e facilidade!

---

Se precisar de suporte ou quiser sugerir melhorias, fique à vontade para abrir issues ou pull requests. Boa codificação! 🎉👨‍💻👩‍💻