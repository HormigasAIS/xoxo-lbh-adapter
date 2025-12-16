# read_sensor.py
"""
Ejemplo de lectura de sensores de un robot usando XOXO-LBH Adapter
Autor: Cristhiam Quiñonez
"""

import time
from adapter import XOXOAdapter, lbh_to_json

# Configuración del adapter
adapter = XOXOAdapter(broker="localhost", robot_id="robot_test")

# Función de callback para procesar datos de sensores
def on_data(topic, data):
    print("[Dashboard] Tópico recibido:", topic)
    try:
        # Convertimos datos LBH a JSON
        sensor_data = lbh_to_json(data)
        print("[Dashboard] Datos de sensor decodificados:", sensor_data)
    except Exception as e:
        print("[Error] Fallo al decodificar LBH:", e)

# Asignamos el handler al adapter
adapter.set_handler(on_data)

# Arrancamos el loop de recepción en segundo plano
adapter.loop_start()

print("[Ejemplo] Escuchando datos de sensores...")

# Mantener el script activo por 10 segundos para recibir datos
time.sleep(10)

# Detenemos el loop
adapter.loop_stop()
print("[Ejemplo] Lectura de sensores finalizada")
