import os
import subprocess

class SpecKitAutomation:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.specify_dir = os.path.join(base_dir, "specify")
        self.plan_dir = os.path.join(base_dir, "plan")
        self.tasks_dir = os.path.join(base_dir, "tasks")
        self.src_dir = os.path.join(base_dir, "src")

    def setup_directories(self):
        """Cria os diretórios necessários para o fluxo do Spec Kit."""
        os.makedirs(self.specify_dir, exist_ok=True)
        os.makedirs(self.plan_dir, exist_ok=True)
        os.makedirs(self.tasks_dir, exist_ok=True)
        os.makedirs(self.src_dir, exist_ok=True)

    def run_cmd(self, cmd, cwd=None):
        """Executa um comando no shell e retorna a saída."""
        print(f"[CMD] {cmd}")
        # Para uma implementação real, o tratamento de erros aqui seria mais robusto
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"[ERROR] {result.stderr}")
            return None
        print(f"[OUTPUT] {result.stdout.strip()}")
        return result.stdout.strip()

    def init_specification(self, project_name, description):
        """Inicializa uma nova especificação."""
        # Este comando é um placeholder. Ajuste conforme a CLI do Spec Kit.
        cmd = f'spec-kit specify init --project "{project_name}" --description "{description}"'
        self.run_cmd(cmd, cwd=self.base_dir)

    def generate_plan(self):
        """Gera um plano técnico a partir das especificações."""
        # Este comando é um placeholder.
        cmd = f"spec-kit plan generate --spec-folder {self.specify_dir}"
        self.run_cmd(cmd, cwd=self.base_dir)

    def create_tasks(self):
        """Cria tarefas de desenvolvimento a partir do plano."""
        # Este comando é um placeholder.
        cmd = f"spec-kit tasks create --plan-folder {self.plan_dir}"
        self.run_cmd(cmd, cwd=self.base_dir)

    def generate_code_from_task(self, task_file):
        """Usa o Gemini para gerar código a partir de uma tarefa."""
        output_file = os.path.join(self.src_dir, os.path.basename(task_file).replace('.spec', '.py'))
        
        # O comando do Gemini aqui é um placeholder. 
        # A implementação real dependerá da API ou CLI do Gemini.
        gemini_cmd = f'gemini generate --input {task_file} --output {output_file}'
        
        print(f"Gerando código para {task_file}...")
        self.run_cmd(gemini_cmd, cwd=self.base_dir)

    def process_all_tasks(self):
        """Itera sobre todas as tarefas e gera o código para cada uma."""
        if not os.path.exists(self.tasks_dir):
            print(f"[WARNING] Diretório de tarefas não encontrado: {self.tasks_dir}")
            return
            
        for task_file in os.listdir(self.tasks_dir):
            if task_file.endswith(".spec"):
                self.generate_code_from_task(os.path.join(self.tasks_dir, task_file))

def main():
    """Orquestra o fluxo completo de automação do Spec Kit."""
    
    # O diretório base deve ser o do projeto onde o Spec Kit será utilizado.
    base_dir = "./meu_projeto_speckit"  
    
    print(f"--- Iniciando automação do Spec Kit para o projeto em '{base_dir}' ---")
    
    automation = SpecKitAutomation(base_dir)
    
    # 1. Prepara a estrutura de diretórios
    automation.setup_directories()
    
    # 2. Inicia a especificação (exemplo)
    automation.init_specification("MeuProjeto", "Funcionalidade de autenticação segura com OAuth2")
    
    # 3. Gera o plano a partir da especificação
    # (Em um cenário real, a especificação seria criada/editada manualmente antes desta etapa)
    automation.generate_plan()
    
    # 4. Cria as tarefas a partir do plano
    automation.create_tasks()
    
    # 5. Processa as tarefas para gerar o código
    automation.process_all_tasks()
    
    print("--- Fluxo Spec Kit + Gemini CLI concluído ---")

if __name__ == "__main__":
    main()