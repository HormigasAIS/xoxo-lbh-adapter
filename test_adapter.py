# test_adapter.py
import time
from adapter import XOXOAdapter, json_to_lbh, lbh_to_json

# Configuración del adapter
adapter = XOXOAdapter(broker="localhost", robot_id="robot_test")

# Función para recibir datos
def on_data(topic, data):
    print("[Dashboard] Tópico:", topic)
    print("[Dashboard] Datos:", data)
    # Convertimos LBH a JSON
    try:
        json_data = lbh_to_json(data)
        print("[Dashboard] Decodificado a JSON:", json_data)
    except Exception as e:
        print("Error al decodificar:", e)

# Asignamos el handler
adapter.set_handler(on_data)

# Arrancamos el loop en segundo plano
adapter.loop_start()

# Enviamos un comando de prueba
test_payload = {"motor_id": 1, "position": 90, "speed": 120}
lbh_frame = json_to_lbh(test_payload)
adapter.publish_act(**test_payload)

print("Enviando comando de prueba...")
time.sleep(5)

# Detener el loop después de prueba
adapter.loop_stop()
print("Test finalizado")
