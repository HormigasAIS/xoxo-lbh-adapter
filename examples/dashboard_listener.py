# dashboard_listener.py
# © 2025-2026 HormigasAIS - Proyectado por Cristhiam Leonardo Hernández Quiñonez (CLHQ)
# Propiedad Intelectual Protegida bajo el Protocolo de Soberanía LBH
"""
Ejemplo de Dashboard Listener usando XOXO-LBH Adapter
Autor: Cristhiam Quiñonez
"""

import time
from adapter import XOXOAdapter, lbh_to_json

# Configuración del adapter
adapter = XOXOAdapter(broker="localhost", robot_id="robot_test")

# Función callback para recibir cualquier evento del robot
def on_data(topic, data):
    print("[Dashboard] Evento recibido en tópico:", topic)
    try:
        # Convertir datos LBH a JSON
        event_data = lbh_to_json(data)
        print("[Dashboard] Datos decodificados:", event_data)
    except Exception as e:
        print("[Error] No se pudo decodificar el paquete LBH:", e)

# Asignar el handler
adapter.set_handler(on_data)

# Iniciar el loop en segundo plano
adapter.loop_start()

print("[Dashboard] Escuchando eventos de robot...")

# Mantener script activo durante 15 segundos para recibir datos
time.sleep(15)

# Detener el loop
adapter.loop_stop()
print("[Dashboard] Listener finalizado")
