import os
import sys
import time
import json
import threading

# Añadimos la ruta para encontrar el adapter
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from adapter.core import XOXOAdapter

def heartbeat():
    """Bucle secundario que registra el rastro de vida en el estado local"""
    state_dir = "/data/data/com.termux/files/home/hormigasais-state"
    state_file = os.path.join(state_dir, "alpha.json")
    
    # Asegurar que el directorio de persistencia exista
    os.makedirs(state_dir, exist_ok=True)
    
    while True:
        try:
            state = {
                "node": "alpha",
                "status": "alive",
                "timestamp": time.time()
            }
            with open(state_file, "w") as f:
                json.dump(state, f, indent=4)
        except Exception as e:
            print(f"⚠️ [HEARTBEAT ERROR] No se pudo escribir estado: {e}")
        
        time.sleep(5)  # Emite feromonas cada 5 segundos

def on_data_received(topic, data):
    """Este callback solo se ejecuta si el CORE ya validó el contrato y la firma"""
    print(f"\n✅ [MANAGER] MENSAJE VALIDADO Y RECIBIDO")
    print(f"📡 Origen: {topic}")
    print(f"📊 Datos del Enjambre: {data}")
    print("-" * 40)

def main():
    # Inicializamos el Manager Alpha ligado a LBH-Secure
    manager = XOXOAdapter(robot_id="manager_alpha")
    manager.on_data_handler = on_data_received
    
    # FASE 4: Lanzar el hilo del Heartbeat para persistencia de estado local
    heartbeat_thread = threading.Thread(target=heartbeat, daemon=True)
    heartbeat_thread.start()
    
    print("🚀 Manager Alpha esperando reportes legitimados...")
    print("💓 Heartbeat activo | Escribiendo persistencia en ~/hormigasais-state/alpha.json")
    print("-" * 40)
    
    # Mantenemos el proceso vivo escuchando de forma segura al broker
    manager.loop_forever()

if __name__ == "__main__":
    main()
