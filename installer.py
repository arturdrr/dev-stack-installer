import subprocess
import os
import sys
import logging

LOGFILE = "devstack_install.log"
CHECKPOINT_FILE = "install_checkpoint.txt"
SSH_CONFIG_FILE = "ssh_command.cfg"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler(LOGFILE),
        logging.StreamHandler(sys.stdout)
    ]
)

def run_command(cmd):
    logging.info(f"Executando: {cmd}")
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info("Comando finalizado com sucesso.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao executar comando: {e}")
        logging.error(e.stderr.decode() if e.stderr else "")
        return False

def save_checkpoint(step):
    with open(CHECKPOINT_FILE, "w") as f:
        f.write(step)

def load_checkpoint():
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, "r") as f:
            return f.read().strip()
    return ""

def save_ssh_command(ssh_cmd):
    with open(SSH_CONFIG_FILE, "w") as f:
        f.write(ssh_cmd)
    os.chmod(SSH_CONFIG_FILE, 0o600)
    logging.info(f"Comando SSH salvo em {SSH_CONFIG_FILE}.")

def load_ssh_command():
    if os.path.exists(SSH_CONFIG_FILE):
        with open(SSH_CONFIG_FILE, "r") as f:
            return f.read().strip()
    return None

def ask_ssh_command_interactive():
    print("=== Configuração simplificada de conexão SSH para a VPS ===")
    ssh_command = input("Digite seu comando SSH completo ou alias para conectar na VPS (ex: ssh user@ip -p 2222): ").strip()
    save_ssh_command(ssh_command)
    return ssh_command

def test_ssh_connection(ssh_command):
    logging.info(f"Testando conexão SSH usando: {ssh_command}")
    try:
        subprocess.run(f"{ssh_command} echo 'Conexão SSH testada com sucesso!'", shell=True, check=True)
        logging.info("Teste de conexão SSH executado com sucesso.")
        return True
    except subprocess.CalledProcessError:
        logging.error("Falha ao testar conexão SSH. Verifique o comando e as configurações SSH locais.")
        return False

def remote_example_task(ssh_command):
    logging.info("Executando tarefa remota de exemplo na VPS.")
    return run_command(f"{ssh_command} 'uptime'")

# Funções de instalação
def install_base():
    cmds = [
        "sudo apt update && sudo apt upgrade -y",
        "sudo apt install -y curl git python3 python3-pip nodejs npm tmux zsh fzf ripgrep bat exa lazygit starship docker.io docker-compose jq htop"
    ]
    return all(run_command(c) for c in cmds)

def install_github_cli():
    if os.system("command -v gh > /dev/null") == 0:
        logging.info("GitHub CLI já instalado, pulando.")
        return True
    cmds = [
        "curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg",
        "sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg",
        "echo 'deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main' | sudo tee /etc/apt/sources.list.d/github-cli.list",
        "sudo apt update",
        "sudo apt install -y gh"
    ]
    return all(run_command(c) for c in cmds)

def install_kilocode():
    path = os.path.expanduser("~/kilocode")
    if os.path.isdir(path):
        logging.info("Kilo Code já instalado, pulando.")
        return True
    cmds = [
        f"git clone https://github.com/Kilo-Org/kilocode.git {path}",
        f"cd {path} && ./install.sh"
    ]
    return all(run_command(c) for c in cmds)

def install_spec_kit():
    path = os.path.expanduser("~/spec-kit")
    if os.path.isdir(path):
        logging.info("Spec Kit já instalado, pulando.")
        return True
    cmds = [
        f"git clone https://github.com/github/spec-kit.git {path}",
        f"cd {path} && pip3 install -r requirements.txt"
    ]
    return all(run_command(c) for c in cmds)

def install_gemini_cli():
    if os.system("command -v gemini > /dev/null") == 0:
        logging.info("Gemini CLI já instalado, pulando.")
        return True
    # Ajustar link oficial
    cmds = [
        "curl -fsSL https://someurl.com/install_gemini.sh | bash"
    ]
    return all(run_command(c) for c in cmds)

def install_githubcloner():
    path = os.path.expanduser("~/githubcloner")
    if os.path.isdir(path):
        logging.info("GithubCloner já instalado, pulando.")
        return True
    cmds = [
        f"git clone https://github.com/mazen160/GithubCloner.git {path}",
        f"cd {path} && pip3 install -r requirements.txt"
    ]
    return all(run_command(c) for c in cmds)

def install_monitoring():
    cmds = [
        "sudo apt install -y prometheus grafana",
        "sudo systemctl enable --now prometheus grafana-server"
    ]
    return all(run_command(c) for c in cmds)

def print_menu():
    print("\n=== Instalador Dev Stack ===")
    print("1. Instalar base do sistema")
    print("2. Instalar GitHub CLI")
    print("3. Instalar Kilo Code")
    print("4. Instalar Spec Kit")
    print("5. Instalar Gemini CLI")
    print("6. Instalar GithubCloner")
    print("7. Instalar Monitoramento (Prometheus e Grafana)")
    print("8. Configurar SSH para VPS")
    print("9. Testar Conexão SSH VPS (Exemplo Remoto)")
    print("10. Executar todas as etapas sequencialmente")
    print("11. Sair")

def main():
    steps = [
        ("base", install_base),
        ("github_cli", install_github_cli),
        ("kilocode", install_kilocode),
        ("spec_kit", install_spec_kit),
        ("gemini_cli", install_gemini_cli),
        ("githubcloner", install_githubcloner),
        ("monitoring", install_monitoring)
    ]

    while True:
        print_menu()
        choice = input("Escolha uma opção: ").strip()
        if choice == "1":
            success = install_base()
            if success: save_checkpoint("base")
        elif choice == "2":
            success = install_github_cli()
            if success: save_checkpoint("github_cli")
        elif choice == "3":
            success = install_kilocode()
            if success: save_checkpoint("kilocode")
        elif choice == "4":
            success = install_spec_kit()
            if success: save_checkpoint("spec_kit")
        elif choice == "5":
            success = install_gemini_cli()
            if success: save_checkpoint("gemini_cli")
        elif choice == "6":
            success = install_githubcloner()
            if success: save_checkpoint("githubcloner")
        elif choice == "7":
            success = install_monitoring()
            if success: save_checkpoint("monitoring")
        elif choice == "8":
            ask_ssh_command_interactive()
        elif choice == "9":
            ssh_cmd = load_ssh_command()
            if ssh_cmd:
                test_ssh_connection(ssh_cmd)
                remote_example_task(ssh_cmd)
            else:
                logging.warning("Comando SSH não configurado. Por favor, configure-o primeiro (Opção 8).")
        elif choice == "10":
            last = load_checkpoint()
            start_index = 0
            for i, (name, _) in enumerate(steps):
                if name == last:
                    start_index = i + 1
            for name, func in steps[start_index:]:
                if not func():
                    logging.error(f"Falha na etapa {name}. Abortando.")
                    break
                save_checkpoint(name)
        elif choice == "11":
            print("Saindo.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
