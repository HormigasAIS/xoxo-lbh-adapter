import subprocess
import time
import os
import sys

def start_colony():
    PORT = 37335
    # Aseguramos que use el Python del venv actual
    python_bin = sys.executable
    os.environ["PYTHONPATH"] = os.getcwd()
    
    print(f"🐜 [HormigasAIS] Orquestando desde Entorno Virtual...")
    
    # Limpieza de seguridad
    subprocess.run("pkill -9 -f uvicorn", shell=True, stderr=subprocess.DEVNULL)
    time.sleep(1)

    cmd = [
        python_bin, "-m", "uvicorn", 
        "adapter.bots.bot_gateway.app", # Nota el cambio a punto si es módulo
        "--host", "127.0.0.1", 
        "--port", str(PORT),
        "--log-level", "info"
    ]

    # Si falla como módulo, intentamos como ruta de archivo (Resiliencia LBH)
    with open("gateway.log", "w") as log:
        process = subprocess.Popen(cmd, stdout=log, stderr=log)
        time.sleep(3)
        
        if process.poll() is not None:
            # Reintento alternativo de ruta
            cmd[3] = "adapter.bots.bot_gateway:app"
            process = subprocess.Popen(cmd, stdout=log, stderr=log)
            time.sleep(2)

        if process.poll() is None:
            print(f"🚀 Gateway SOBERANO activo (PID: {process.pid})")
        else:
            print("❌ Error. Revise 'cat gateway.log' para diagnóstico.")

if __name__ == "__main__":
    start_colony()
