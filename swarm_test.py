import time
import sys
import os

# 1. Configuración de entorno
sys.path.append(os.getcwd())
from adapter.core import XOXOAdapter

# Tópico único para evitar ruidos de otros canales
TOPIC_TELEMETRY = "hormigasais/swarm/telemetry"

print("🐜 [SISTEMA ENJAMBRE] Iniciando Protocolo LBH-Secure...")

# 2. Inicialización de Agentes
manager = XOXOAdapter(robot_id="manager_alpha")
worker = XOXOAdapter(robot_id="worker_beta")

# 3. Lógica del Manager (IA)
def procesar_datos(data):
    if not data: return
    # Si logramos llegar aquí, es que la firma LBH fue validada por el bridge
    bateria = data.get("battery", 100)
    print(f"\n✅ [MANAGER] Firma verificada. Batería de compañera: {bateria}%")
    if bateria < 20:
        print("🚨 [IA] Enviando comando de emergencia...")

# 4. Configurar el receptor
manager.set_handler(procesar_datos)

# 5. Iniciar conexiones
manager.start()
worker.start()

# 6. Espera de Estabilización (EVITA EL CICLO DE RECONEXIÓN)
print("⏳ Estabilizando red MQTT...")
time.sleep(5) 

# El Manager se sintoniza al canal de la Worker
manager.adapter.client.subscribe(TOPIC_TELEMETRY)

print("\n--- 🏁 INICIO DE TRANSMISIÓN SEGURA ---")

# 7. La Worker genera y envía el reporte
payload = {"battery": 15, "status": "critical"}
# Generamos el frame LBH con HMAC
frame = worker.send_command(payload)

print(f"📦 Frame LBH: {frame[:20]}...")
worker.adapter.client.publish(TOPIC_TELEMETRY, frame)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n🛑 Apagando...")
    manager.stop()
    worker.stop()

