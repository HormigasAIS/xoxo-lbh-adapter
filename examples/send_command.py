# send_command.py
"""
Ejemplo de envío de comandos a un robot usando XOXO-LBH Adapter
Autor: Cristhiam Quiñonez
"""

import time
from adapter import XOXOAdapter, json_to_lbh

# Configuración del adapter
adapter = XOXOAdapter(broker="localhost", robot_id="robot_test")

# Función de callback para recibir datos del robot
def on_data(topic, data):
    print("[Dashboard] Tópico:", topic)
    print("[Dashboard] Datos recibidos:", data)

# Asignamos el handler de recepción
adapter.set_handler(on_data)

# Arrancamos el loop de recepción en segundo plano
adapter.loop_start()

# Comando de prueba para el robot
command_payload = {
    "motor_id": 1,
    "position": 45,   # Grados
    "speed": 100      # RPM
}

# Convertimos JSON a LBH
lbh_frame = json_to_lbh(command_payload)

# Enviamos comando al robot
adapter.publish_act(**command_payload)

print("[Ejemplo] Comando enviado:", command_payload)

# Esperamos 5 segundos para recibir respuesta
time.sleep(5)

# Detenemos el loop
adapter.loop_stop()
print("[Ejemplo] Test de envío finalizado")
