import subprocess
import time
import os
import socket

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0

def start_colony():
    PORT = 37335
    LOG_FILE = "gateway.log"
    
    print(f"🐜 [HormigasAIS] Iniciando orquestación en el borde...")
    
    # 1. Limpieza de procesos previos
    if is_port_in_use(PORT):
        print(f"⚠️ Puerto {PORT} ocupado. Limpiando...")
        subprocess.run(["pkill", "-f", "uvicorn"])
        time.sleep(2)

    # 2. Comando de ejecución
    cmd = [
        "python3", "-m", "uvicorn", 
        "adapter.bots.bot_gateway:app", 
        "--host", "127.0.0.1", 
        "--port", str(PORT)
    ]

    with open(LOG_FILE, "a") as log:
        process = subprocess.Popen(cmd, stdout=log, stderr=log)
        print(f"🚀 Gateway en línea (PID: {process.pid}).")
        print(f"📡 Monitoreando rastro en: {LOG_FILE}")

if __name__ == "__main__":
    start_colony()
