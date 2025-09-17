from prometheus_client import start_http_server, Counter, Gauge
import time
import random

# Métricas personalizadas
kilo_code_runs = Counter('kilo_code_run_total', 'Total de execuções do Kilo Code')
gemini_latency = Gauge('gemini_cli_latency_seconds', 'Latency atual do Gemini CLI')

def simulate_metrics():
    while True:
        kilo_code_runs.inc(random.randint(0, 3))  # Incrementa aleatoriamente execuções
        gemini_latency.set(random.uniform(0.1, 1.5))  # Simula latência em segundos
        time.sleep(15)

if __name__ == '__main__':
    start_http_server(8000)  # Porta para Prometheus coletar métricas
    print("Servidor de métricas iniciado na porta 8000")
    simulate_metrics()
