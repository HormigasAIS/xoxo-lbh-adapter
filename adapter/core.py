# core.py
"""
XOXO-LBH Adapter - Core
Autor: Cristhiam Quiñonez
Descripción:
Capa central que integra XOXO con LBH-M2M, proporcionando:
- Publicación y suscripción a tópicos MQTT
- Conversión JSON <-> LBH
- Gestión de handlers para dashboard y robots
- Escalabilidad para múltiples robots y entornos B2B
"""

from adapter import XOXOAdapter, json_to_lbh, lbh_to_json

class XOXOCore:
    def __init__(self, broker="localhost", robot_id="robot_default"):
        """
        Inicializa el adapter con broker y robot_id
        """
        self.adapter = XOXOAdapter(broker=broker, robot_id=robot_id)

    def start(self):
        """
        Inicia el loop del adapter
        """
        self.adapter.loop_start()

    def stop(self):
        """
        Detiene el loop del adapter
        """
        self.adapter.loop_stop()

    def send_command(self, payload: dict):
        """
        Envía comando a actuadores
        payload = {"motor_id": 1, "position": 90, "speed": 120}
        """
        lbh_frame = json_to_lbh(payload)
        self.adapter.publish_act(**payload)
        return lbh_frame

    def set_dashboard_handler(self, handler):
        """
        Asigna función para recibir datos del robot
        """
        def wrapped_handler(topic, data):
            try:
                json_data = lbh_to_json(data)
                handler(topic, json_data)
            except Exception as e:
                print("Error al decodificar:", e)

        self.adapter.set_handler(wrapped_handler)
