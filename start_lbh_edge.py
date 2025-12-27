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
    # Sincronización de rutas para el borde
    os.environ["PYTHONPATH"] = os.getcwd()

    print(f"🐜 [HormigasAIS] Iniciando orquestación en el borde...")

    # 1. Limpieza de procesos previos
    if is_port_in_use(PORT):
        print(f"⚠️ Puerto {PORT} ocupado. Limpiando...")
        subprocess.run("pkill -9 -f uvicorn", shell=True)
        time.sleep(2)

    # 2. Comando de ejecución (LBH Gateway)
    cmd = [
        "python3", "-m", "uvicorn",
        "adapter.bots.bot_gateway:app",
        "--host", "127.0.0.1",
        "--port", str(PORT)
    ]

    with open(LOG_FILE, "w") as log:
        process = subprocess.Popen(cmd, stdout=log, stderr=log)
        time.sleep(2) # Espera de estabilización
        if process.poll() is None:
            print(f"🚀 Gateway en línea (PID: {process.pid}).")
            print(f"📡 Monitoreando rastro en: {LOG_FILE}")
        else:
            print("❌ Error al iniciar. Verifique gateway.log")

if __name__ == "__main__":
    start_colony()
