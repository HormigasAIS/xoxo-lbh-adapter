import os
import sys

# Añadimos la ruta para encontrar el adapter
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from adapter.core import XOXOAdapter

def on_data_received(topic, data):
    """
    Este callback solo se ejecuta si el CORE ya validó:
    1. El Contrato Humano (LBH_ASSIST = true)
    2. La firma HMAC (Mensaje auténtico)
    """
    print(f"\n✅ [MANAGER] MENSAJE VALIDADO Y RECIBIDO")
    print(f"📡 Origen: {topic}")
    print(f"📊 Datos del Enjambre: {data}")
    print("-" * 40)

def main():
    # Inicializamos el Manager
    # Nota: Usamos XOXOAdapter que es el nombre de la clase en tu core.py
    manager = XOXOAdapter(robot_id="manager_alpha")
    
    # Configuramos el manejador de datos validados
    manager.on_data_handler = on_data_received
    
    print("🚀 Manager Alpha esperando reportes legitimados...")
    
    # Mantenemos el proceso vivo usando el nuevo método del Core
    manager.loop_forever()

if __name__ == "__main__":
    main()

