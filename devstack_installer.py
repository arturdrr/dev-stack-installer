import subprocess
import sys
import argparse
import logging
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

LOGFILE = "devstack_complete.log"
logging.basicConfig(level=logging.INFO, filename=LOGFILE,
                    format="%(asctime)s %(levelname)s:%(message)s")

console = Console()

def runcommand(cmd):
    logging.info(f"Executando: {cmd}")
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info("Comando executado com sucesso")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao executar o comando: {str(e)}")
        return False

def show_menu(title, options, border_color):
    panel = Panel('\n'.join(options), title=title, border_style=border_color, padding=(1, 4))
    console.print(Align.center(panel))

def choose_profile(interactive=True, preset=None):
    if not interactive:
        return preset  # Preset for non interactive mode

    while True:
        options = ["[1] Básico", "[2] Pesado", "[0] Voltar"]
        show_menu("Escolha o Perfil", options, "bright_magenta")
        profile = console.input("\nEscolha um perfil: ").strip()
        if profile in ["0", "1", "2"]:
            return profile
        console.print("[red]Opção inválida! Tente novamente.[/red]")

def install_local(profile):
    console.print(f"\nIniciando instalação local com perfil: {'Básico' if profile == '1' else 'Pesado'}")
    if profile == "2":  # pesado
        cmds = [
            "sudo apt update",
            "sudo apt upgrade -y",
            "sudo apt install -y curl git neovim fzf tmux docker.io python3 python3-pip build-essential"
        ]
    else:  # básico
        cmds = [
            "sudo apt update",
            "sudo apt upgrade -y",
            "sudo apt install -y curl git neovim fzf tmux"
        ]
    for c in cmds:
        if not runcommand(c):
            console.print("[red]Erro na instalação local.[/red]")
            return
    console.print("[green]Instalação local concluída com sucesso.[/green]")

def install_vps(profile, user, host):
    console.print(f"\nIniciando instalação na VPS com perfil: {'Básico' if profile == '1' else 'Pesado'}")
    install_cmd = f"cd ~/dev-stack-installer && ./install.sh --{'basic' if profile == '1' else 'heavy'}"
    ssh_cmd = f"ssh {user}@{host} 
'{install_cmd}'"
    if not runcommand(ssh_cmd):
        console.print("[red]Erro na instalação na VPS.[/red]")
        return
    console.print("[green]Instalação na VPS concluída com sucesso.[/green]")

def main(interactive, mode=None, profile=None, user=None, host=None):
    if interactive:
        while True:
            options = [
                "[1] Instalar localmente",
                "[2] Instalar na VPS",
                "[3] Instalar local e VPS (sequencial)",
                "[0] Sair"
            ]
            show_menu("Menu Principal", options, "bright_blue")
            choice = console.input("\nEscolha uma opção: ").strip()

            if choice == "1":
                profile_choice = choose_profile()
                if profile_choice != "0":
                    install_local(profile_choice)
                console.input("\nPressione Enter para retornar ao menu...")

            elif choice == "2":
                profile_choice = choose_profile()
                if profile_choice != "0":
                    install_vps(profile_choice, user or "user", host or "vps.example.com")
                console.input("\nPressione Enter para retornar ao menu...")

            elif choice == "3":
                profile_choice = choose_profile()
                if profile_choice != "0":
                    install_vps(profile_choice, user or "user", host or "vps.example.com")
                    install_local(profile_choice)
                console.input("\nPressione Enter para retornar ao menu...")

            elif choice == "0":
                console.print("Saindo...")
                break
            else:
                console.print("[red]Opção inválida! Tente novamente.[/red]")
                console.input("Pressione Enter para continuar...")

    else:
        # modo não interativo
        if mode not in ["local", "vps", "both"] or profile not in ["1", "2"]:
            console.print("[red]Modo ou perfil inválido. Use --help para ajuda.[/red]")
            sys.exit(1)
        if mode == "local":
            install_local(profile)
        elif mode == "vps":
            install_vps(profile, user, host)
        elif mode == "both":
            install_vps(profile, user, host)
            install_local(profile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dev Stack Installer")
    parser.add_argument("--mode", choices=["local", "vps", "both"], help="Modo de instalação")
    parser.add_argument("--profile", choices=["1", "2"], help="Perfil: 1=básico, 2=pesado")
    parser.add_argument("--user", default="user", help="Usuário SSH da VPS")
    parser.add_argument("--host", default="vps.example.com", help="Host/IP da VPS")
    args = parser.parse_args()

    interactive_mode = not (args.mode and args.profile)
    # check_and_install = lambda: None  # Ou implemente check/install do rich se quiser
    try:
        import rich
    except ImportError:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
            import rich
        except subprocess.CalledProcessError:
            print("Erro ao instalar a biblioteca 'rich'. Por favor, instale-a manualmente: pip install rich")
            sys.exit(1)

    main(interactive_mode, args.mode, args.profile, args.user, args.host)