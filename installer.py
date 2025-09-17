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

def detect_local_system():
    logging.info("Detectando sistema local...")
    distro = run_command("grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"'")
    cpu = run_command("lscpu | grep 'Model name' | cut -d: -f2 | xargs")
    ram = run_command("free -m | grep Mem | awk '{print $2}'")
    gpu_info = run_command("lspci | grep -i 'vga\|3d\|2d'")
    return {"distro": distro, "cpu": cpu, "ram_mb": ram, "gpu": gpu_info}

def detect_vps_system(ssh_command):
    logging.info(f"Detectando sistema VPS usando: {ssh_command}...")
    def ssh_run(cmd):
        return run_command(f"{ssh_command} '{cmd}'")
    
    distro = ssh_run("grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"'")
    cpu = ssh_run("lscpu | grep 'Model name' | cut -d: -f2 | xargs")
    ram = ssh_run("free -m | grep Mem | awk '{print $2}'")
    gpu_info = ssh_run("lspci | grep -i 'vga\|3d\|2d'")

    return {"distro": distro, "cpu": cpu, "ram_mb": ram, "gpu": gpu_info}

def decide_installation(system_info):
    ram = int(system_info.get("ram_mb") or 0)
    gpu = system_info.get("gpu") or ""
    logging.info(f"RAM detectada (MB): {ram}")
    logging.info(f"GPU detectada: {gpu}")

    # Lógica de exemplo para decisão de instalação
    if ram >= 16000 and gpu:
        logging.info("Decisão: Instalar pacotes pesados de AI/ML e drivers de GPU.")
        return "heavy"
    elif ram >= 8000:
        logging.info("Decisão: Instalar pacotes de desenvolvimento padrão.")
        return "standard"
    else:
        logging.info("Decisão: Instalar pacotes básicos.")
        return "basic"

def choose_profile():
    while True:
        print("\nEscolha o perfil de instalação:")
        print("1 - Básico")
        print("2 - Padrão (Desenvolvimento)")
        print("3 - Pesado (AI/ML)")
        choice = input("Perfil: ").strip()
        if choice == "1":
            return "basic"
        elif choice == "2":
            return "standard"
        elif choice == "3":
            return "heavy"
        else:
            print("Opção inválida, tente novamente.")

def add_custom_apt_repository(repo_url: str, repo_name: str, gpg_key_url: str):
    # Adicionar chave GPG
    cmd_key = f"curl -fsSL {gpg_key_url} | sudo gpg --dearmor -o /usr/share/keyrings/{repo_name}-archive-keyring.gpg"
    if not run_command(cmd_key):
        logging.error(f"Falha ao adicionar chave GPG do repositório {repo_name}")
        return False

    # Adicionar repositório na lista APT
    repo_entry = f"deb [signed-by=/usr/share/keyrings/{repo_name}-archive-keyring.gpg] {repo_url} main"
    repo_path = f"/etc/apt/sources.list.d/{repo_name}.list"
    
    if not os.path.exists(repo_path):
        with open(repo_path, "w") as repo_file:
            repo_file.write(repo_entry + "\n")
        logging.info(f"Repositório {repo_name} adicionado com sucesso.")
    else:
        logging.info(f"Repositório {repo_name} já existe.")
    
    # Atualizar índices do APT
    update_cmd = "sudo apt update"
    if not run_command(update_cmd):
        logging.error(f"Falha ao atualizar repositórios após adicionar {repo_name}")
        return False

    return True

def interactive_add_apt_repository():
    print("=== Adicionar Repositório APT Customizado ===")
    repo_url = input("URL do repositório (ex: http://ppa.launchpad.net/some/ppa/ubuntu): ").strip()
    repo_name = input("Nome do repositório (ex: some-ppa): ").strip()
    gpg_key_url = input("URL da chave GPG (ex: https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x<KEYID>): ").strip()
    
    if add_custom_apt_repository(repo_url, repo_name, gpg_key_url):
        logging.info("Repositório APT customizado adicionado com sucesso!")
    else:
        logging.error("Falha ao adicionar repositório APT customizado.")

# Funções de instalação adaptativas
def install_base(profile):
    logging.info(f"Instalando base do sistema com perfil: {profile}")
    cmds = [
        "sudo apt update && sudo apt upgrade -y"
    ]
    if profile == "heavy":
        cmds.append("sudo apt install -y curl git python3 python3-pip nodejs npm tmux zsh fzf ripgrep bat exa lazygit starship docker.io docker-compose jq htop build-essential")
        # Adicionar pacotes específicos para perfil heavy
    elif profile == "standard":
        cmds.append("sudo apt install -y curl git python3 python3-pip nodejs npm tmux zsh fzf ripgrep bat exa lazygit starship docker.io docker-compose jq htop")
        # Adicionar pacotes específicos para perfil standard
    else: # basic
        cmds.append("sudo apt install -y curl git python3 python3-pip tmux zsh fzf ripgrep bat exa lazygit starship")
        # Adicionar pacotes específicos para perfil basic
    return all(run_command(c) for c in cmds)

def install_github_cli(profile):
    logging.info(f"Instalando GitHub CLI com perfil: {profile}")
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

def install_kilocode(profile):
    logging.info(f"Instalando Kilo Code com perfil: {profile}")
    path = os.path.expanduser("~/kilocode")
    if os.path.isdir(path):
        logging.info("Kilo Code já instalado, pulando.")
        return True
    cmds = [
        f"git clone https://github.com/Kilo-Org/kilocode.git {path}",
        f"cd {path} && ./install.sh"
    ]
    return all(run_command(c) for c in cmds)

def install_spec_kit(profile):
    logging.info(f"Instalando Spec Kit com perfil: {profile}")
    path = os.path.expanduser("~/spec-kit")
    if os.path.isdir(path):
        logging.info("Spec Kit já instalado, pulando.")
        return True
    cmds = [
        f"git clone https://github.com/github/spec-kit.git {path}",
        f"cd {path} && pip3 install -r requirements.txt"
    ]
    return all(run_command(c) for c in cmds)

def install_gemini_cli(profile):
    logging.info(f"Instalando Gemini CLI com perfil: {profile}")
    if os.system("command -v gemini > /dev/null") == 0:
        logging.info("Gemini CLI já instalado, pulando.")
        return True
    # Ajustar link oficial
    cmds = [
        "curl -fsSL https://someurl.com/install_gemini.sh | bash"
    ]
    return all(run_command(c) for c in cmds)

def install_githubcloner(profile):
    logging.info(f"Instalando GithubCloner com perfil: {profile}")
    path = os.path.expanduser("~/githubcloner")
    if os.path.isdir(path):
        logging.info("GithubCloner já instalado, pulando.")
        return True
    cmds = [
        f"git clone https://github.com/mazen160/GithubCloner.git {path}",
        f"cd {path} && pip3 install -r requirements.txt"
    ]
    return all(run_command(c) for c in cmds)

def install_monitoring(profile):
    logging.info(f"Instalando Monitoramento com perfil: {profile}")
    cmds = [
        "sudo apt install -y prometheus grafana",
        "sudo systemctl enable --now prometheus grafana-server"
    ]
    return all(run_command(c) for c in cmds)

def run_adaptive_local_install():
    logging.info("=== Iniciando instalação adaptativa LOCAL ===")
    local_info = detect_local_system()
    logging.info(f"Informações do sistema local: {local_info}")
    
    profile = decide_installation(local_info) # Decisão automática
    print(f"Perfil de instalação local (automático): {profile}")
    
    # Ou permitir escolha manual:
    # profile = choose_profile()
    # print(f"Perfil de instalação local (manual): {profile}")

    # Executar etapas de instalação com base no perfil
    steps_to_run = [
        ("base", install_base),
        ("github_cli", install_github_cli),
        ("kilocode", install_kilocode),
        ("spec_kit", install_spec_kit),
        ("gemini_cli", install_gemini_cli),
        ("githubcloner", install_githubcloner),
        ("monitoring", install_monitoring)
    ]

    for name, func in steps_to_run:
        logging.info(f"Iniciando etapa {name} com perfil {profile}")
        if not func(profile):
            logging.error(f"Falha na etapa {name}. Abortando instalação local.")
            return False
        save_checkpoint(name) # Salva checkpoint para cada etapa
    logging.info("=== Instalação adaptativa LOCAL concluída ===")
    return True

def run_adaptive_vps_install():
    logging.info("=== Iniciando instalação adaptativa VPS ===")
    ssh_cmd = load_ssh_command()
    if not ssh_cmd:
        logging.error("Comando SSH para VPS não configurado. Por favor, configure-o primeiro (Opção 8).")
        return False

    if not test_ssh_connection(ssh_cmd):
        logging.error("Não foi possível conectar à VPS para detecção de sistema.")
        return False

    vps_info = detect_vps_system(ssh_cmd)
    logging.info(f"Informações do sistema VPS: {vps_info}")
    
    profile = decide_installation(vps_info) # Decisão automática
    print(f"Perfil de instalação VPS (automático): {profile}")

    # Ou permitir escolha manual:
    # profile = choose_profile()
    # print(f"Perfil de instalação VPS (manual): {profile}")

    # Aqui, você precisaria adaptar as funções de instalação para serem executadas remotamente via SSH
    # Por exemplo, para install_base:
    # remote_base_cmd = f"{ssh_cmd} 'sudo apt update && sudo apt upgrade -y && sudo apt install -y curl git python3 python3-pip nodejs npm tmux zsh fzf ripgrep bat exa lazygit starship docker.io docker-compose jq htop'"
    # if not run_command(remote_base_cmd):
    #     logging.error("Falha na instalação base remota.")
    #     return False

    logging.warning("A instalação adaptativa VPS ainda requer adaptação das funções de instalação para execução remota.")
    logging.info("=== Instalação adaptativa VPS concluída (requer implementação remota) ===")
    return True

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
    print("10. Adicionar Repositório APT Customizado")
    print("11. Instalação Adaptativa (Local)")
    print("12. Instalação Adaptativa (VPS)")
    print("13. Executar todas as etapas sequencialmente")
    print("14. Sair")

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
            success = install_base(choose_profile())
            if success: save_checkpoint("base")
        elif choice == "2":
            success = install_github_cli(choose_profile())
            if success: save_checkpoint("github_cli")
        elif choice == "3":
            success = install_kilocode(choose_profile())
            if success: save_checkpoint("kilocode")
        elif choice == "4":
            success = install_spec_kit(choose_profile())
            if success: save_checkpoint("spec_kit")
        elif choice == "5":
            success = install_gemini_cli(choose_profile())
            if success: save_checkpoint("gemini_cli")
        elif choice == "6":
            success = install_githubcloner(choose_profile())
            if success: save_checkpoint("githubcloner")
        elif choice == "7":
            success = install_monitoring(choose_profile())
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
            interactive_add_apt_repository()
        elif choice == "11":
            run_adaptive_local_install()
        elif choice == "12":
            run_adaptive_vps_install()
        elif choice == "13":
            last = load_checkpoint()
            start_index = 0
            for i, (name, _) in enumerate(steps):
                if name == last:
                    start_index = i + 1
            for name, func in steps[start_index:]:
                if not func(choose_profile()): # Pass profile to sequential steps
                    logging.error(f"Falha na etapa {name}. Abortando.")
                    break
                save_checkpoint(name)
        elif choice == "14":
            print("Saindo.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()