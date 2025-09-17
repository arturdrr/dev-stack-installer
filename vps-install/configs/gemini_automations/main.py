import os
import subprocess
import json
import shutil
import logging
import smtplib
from email.message import EmailMessage

# Configuração do logger
logging.basicConfig(
    filename='automation.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def log_info(message):
    logging.info(message)
    print(message)

def log_error(message):
    logging.error(message)
    print(message)

def enviar_email(subject, body, to_emails, from_email, smtp_server, smtp_port, smtp_user, smtp_password):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_emails
    msg.set_content(body)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
        smtp.login(smtp_user, smtp_password)
        smtp.send_message(msg)
    log_info(f"Email enviado para {to_emails} com assunto: {subject}")

class GeminiIntegration:
    def __init__(self, repo_path, gemini_cli_command="gemini"):
        self.repo_path = repo_path
        self.gemini_cli_command = gemini_cli_command

    def carregar_arquivos_importantes(self):
        arquivos_alvo = ['README.md', 'install.sh', 'setup.py', 'requirements.txt', 'package.json']
        conteudos = {}
        for arquivo in arquivos_alvo:
            caminho = os.path.join(self.repo_path, arquivo)
            if os.path.isfile(caminho):
                with open(caminho, 'r', encoding='utf-8', errors='ignore') as f:
                    conteudos[arquivo] = f.read()
        return conteudos

    def preparar_prompt(self, conteudos):
        prompt = "Você é um assistente que gera comandos shell para instalar e configurar projetos.\n\n"
        for nome, conteudo in conteudos.items():
            prompt += f"Conteúdo do arquivo {nome}:\n{conteudo}\n\n"
        prompt += "Com base nestes arquivos, gere uma sequência de comandos shell para instalar e configurar este projeto, com explicações sucintas."
        return prompt

    def executar_gemini(self, prompt):
        # Executa o Gemini CLI passando o prompt e captura a saída
        try:
            processo = subprocess.run(
                [self.gemini_cli_command, "generate", "--prompt", prompt],
                capture_output=True, text=True, check=True
            )
            return processo.stdout
        except subprocess.CalledProcessError as e:
            return f"Erro ao executar Gemini CLI: {e}"

    def gerar_script_instalacao(self):
        conteudos = self.carregar_arquivos_importantes()
        if not conteudos:
            return "Nenhum arquivo relevante encontrado no repositório."
        prompt = self.preparar_prompt(conteudos)
        resultado = self.executar_gemini(prompt)
        return resultado

class ScriptExecutor:
    def __init__(self, repo_path, backup_dir="./backup"):
        self.repo_path = repo_path
        self.backup_dir = backup_dir
        os.makedirs(self.backup_dir, exist_ok=True)

    def criar_backup(self):
        backup_path = os.path.join(self.backup_dir, os.path.basename(self.repo_path))
        if os.path.exists(backup_path):
            shutil.rmtree(backup_path)
        shutil.copytree(self.repo_path, backup_path)
        log_info(f"Backup criado em {backup_path}")

    def executar_script(self, script_text):
        script_file = os.path.join(self.repo_path, "temp_install.sh")
        with open(script_file, "w") as f:
            f.write(script_text)
        os.chmod(script_file, 0o755)

        self.criar_backup()

        log_info(f"Executando script: {script_file}")
        try:
            resultado = subprocess.run([script_file], cwd=self.repo_path, capture_output=True, text=True, check=True)
            log_info("Execução concluída com sucesso.")
            log_info(f"Saída do script:\n{resultado.stdout}")
        except subprocess.CalledProcessError as e:
            log_error(f"Erro na execução do script:")
            log_error(e.stderr)
            log_info("Restaurando backup...")
            self.restaurar_backup()
            return False
        finally:
            os.remove(script_file)
        return True

    def restaurar_backup(self):
        backup_path = os.path.join(self.backup_dir, os.path.basename(self.repo_path))
        if os.path.exists(self.repo_path):
            shutil.rmtree(self.repo_path)
        shutil.copytree(backup_path, self.repo_path)
        log_info("Backup restaurado com sucesso.")

def executar_comando(cmd, cwd=None):
    try:
        resultado = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, check=True)
        log_info(f"Comando executado com sucesso: {cmd}\nSaída: {resultado.stdout}")
        return True, resultado.stdout
    except subprocess.CalledProcessError as e:
        log_error(f"Erro ao executar comando: {cmd}\nErro: {e.stderr}")
        return False, e.stderr

def processar_repositorios():
    repo_base_path = "./repos"
    if not os.path.isdir(repo_base_path):
        log_info(f"Diretório de repositórios '{repo_base_path}' não encontrado. Criando...")
        os.makedirs(repo_base_path)

    repos = os.listdir(repo_base_path)
    for repo in repos:
        repo_path = os.path.join(repo_base_path, repo)
        
        log_info(f"Iniciando execução para o repositório {repo}")
        
        # Exemplo: gerar script com Gemini (simulado aqui)
        # script_gerado = gerar_script_gemini(repo_path)

        # Para exemplo, assumimos conteúdo do script
        script_gerado = """
        #!/bin/bash
        echo 'Rodando etapas de instalação para o repo'
        """
        
        script_path = os.path.join(repo_path, "temp_install.sh")
        with open(script_path, "w") as f:
            f.write(script_gerado)
        os.chmod(script_path, 0o755)
        
        sucesso, output = executar_comando(f"./temp_install.sh", cwd=repo_path)
        os.remove(script_path)
        
        if not sucesso:
            # Exemplo de envio de email. Substitua com suas credenciais.
            # enviar_email(
            #     subject=f"Falha na execução do script no repositório {repo}",
            #     body=output,
            #     to_emails="seu-email@exemplo.com",
            #     from_email="automatizador@exemplo.com",
            #     smtp_server="smtp.exemplo.com",
            #     smtp_port=465,
            #     smtp_user="usuariomail",
            #     smtp_password="senha"
            # )
            log_error(f"Execução falhou no repositório {repo}, email de alerta enviado.")
        else:
            log_info(f"Execução concluída com sucesso no repositório {repo}.")

if __name__ == "__main__":
    processar_repositorios()
