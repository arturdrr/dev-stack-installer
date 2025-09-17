## Plano de Testes para dev-stack-installer e best-practices-tool

Este documento descreve um plano de testes abrangente para garantir a funcionalidade e a robustez dos projetos `dev-stack-installer` e `best-practices-tool`.

---

### 1. Preparar Ambiente

-   **Sistema Operacional**: Ubuntu/Debian limpo (físico, VM ou Docker container com GUI terminal).
-   **Software Básico**: Instalar Python 3.8+ e curl/wget básicos.
-   **Permissões**: Configurar sudo com senha para o usuário de teste.

---

### 2. Clonar e Verificar Inicial

**Para `dev-stack-installer`:**

```bash
git clone https://github.com/arturdrr/dev-stack-installer.git
cd dev-stack-installer
ls -l
```

**Para `best-practices-tool`:**

```bash
git clone https://github.com/arturdrr/best-practices-tool.git
cd best-practices-tool
ls -l
```

-   **Verificação**: Confirme se `README.md` e scripts (`installer.py`, scripts shell, scripts Python) estão presentes.

---

### 3. Testar Instalador Python (Interativo)

**Para `dev-stack-installer`:**

```bash
python3 installer.py
```

-   **Execução**: Siga o menu, execute a instalação local somente, depois a instalação em VPS somente.
-   **Verificação**: Confirme a criação de logs (`devstack_install.log`) e checkpoint (`install_checkpoint.txt`).
-   **Resiliência**: Teste retomar a instalação após abortá-la.

**Para `best-practices-tool`:**

```bash
python3 installer.py
```

-   **Verificação**: Verifique se o instalador cria as práticas, hooks, wrapper e agendamentos cron.
-   **Configuração**: Confirme se `.bashrc` é modificado adequadamente.
-   **Funcionalidade**: Teste a execução de comandos via wrapper e observe os alertas.

---

### 4. Testar Modo Não Interativo (CLI)

**Para `dev-stack-installer`:**

```bash
python3 installer.py --mode local --profile 1
python3 installer.py --mode vps --profile 2 --user seu_usuario --host seu_vps
```

**Para `best-practices-tool`:**

```bash
python3 installer.py --mode local --profile basic
python3 installer.py --mode vps --profile heavy --user seu_usuario --host seu_vps
```

---

### 5. Validar Shell Hooks e Wrapper

-   **Ativação**: Abra um novo terminal para validar que o hook está ativo (verifique avisos para `rm`, `git push`, `sudo`).
-   **Wrapper**: Teste um comando com o wrapper:
    ```bash
    run_validated_command rm -rf /diretorio/teste
    ```

---

### 6. Testar Atualizações Automáticas

-   **Manual**: Rode manualmente o script de atualização:
    ```bash
    python3 update_practices_cron.py
    ```
-   **Logs**: Verifique os logs em `update_practices.log` ou no local configurado.
-   **Agendamento**: Cheque o crontab para confirmar o agendamento:
    ```bash
    crontab -l
    ```
-   **Configuração**: Teste a edição em `config.yaml` para ativar/desativar componentes e validadores.

---

### 7. Testar Limpeza e Desinstalação (se aplicável)

-   **Script de Desinstalação**: Verifique se existe um script para remover as alterações feitas (hooks, alias, pastas).
-   **Remoção Manual**: Caso não haja, teste a remoção manual e garanta que não deixa resíduos.

---

### 8. Analisar Problemas e Ajustar

-   **Diagnóstico**: Caso erros ocorram, use os arquivos de log para diagnóstico e adapte os scripts se necessário.
-   **Verificações**: Cheque versões de Python, permissões, pacotes do sistema operacional e dependências externas.
