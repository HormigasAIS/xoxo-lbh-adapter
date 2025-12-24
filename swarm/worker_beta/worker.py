import time
import random
from adapter.core import XOXOAdapter
from adapter.json_lbh import json_to_lbh

def main():
    # Inicializamos el Worker con el nuevo nombre de clase
    worker = XOXOAdapter(robot_id="worker_beta")
    
    print("🐝 Worker Beta iniciado | Albedrío Controlado Activo")
    
    try:
        worker.client.connect("localhost", 1883, 60)
        worker.client.loop_start()
        
        while True:
            # 📊 Simulación de datos (Libertad condicionada)
            sensor_data = {
                "temp": round(random.uniform(20.0, 30.0), 2),
                "status": "OPERATIONAL",
                "timestamp": time.time()
            }
            
            # 🔐 Cifrado y Firma con la Llave 2025 (vía json_lbh)
            # Esto genera el hexadecimal firmado que el Manager espera
            payload_hex = json_to_lbh(sensor_data)
            
            # Enviamos al tópico de reportes
            worker.client.publish(worker.rpt_topic, payload_hex)
            
            print(f"📡 Reporte enviado (Firmado): {sensor_data}")
            time.sleep(5)  # Latido del enjambre
            
    except KeyboardInterrupt:
        print("\n🛑 Worker detenido por el usuario")
        worker.client.loop_stop()

if __name__ == "__main__":
    main()
