# core.py
"""
XOXO-LBH Adapter - Core con Seguridad HMAC y Gobernanza LBH
Autor: Cristhiam Quiñonez
"""

import json
import paho.mqtt.client as mqtt
# Importamos las herramientas de seguridad y el contrato
from .json_lbh import json_to_lbh, lbh_to_json
from adapter.human_contract import HumanContract 

class XOXOAdapter:
    def __init__(self, broker="localhost", port=1883, **kwargs):
        self.broker = broker
        self.port = port
        self.robot_id = kwargs.get('robot_id', 'unknown_robot')
        self.on_data_handler = None

        # 🔐 PASO 3: Inicialización del Contrato Humano (LBH)
        # El "Sacerdote" se integra al motor para vigilar las acciones
        self.human_contract = HumanContract()
        self.human_contract.load()

        # Tópicos siguiendo el estándar HormigasAIS
        self.cmd_topic = f"hormigasais/{self.robot_id}/commands"
        self.rpt_topic = f"hormigasais/{self.robot_id}/reports"

        # Cliente MQTT
        self.client = mqtt.Client(client_id=self.robot_id)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message

        print(f"📡 Sistema LBH-Secure Activo | Robot: {self.robot_id}")

    # 🛡️ PASO 4: El Método Barrera (Gatekeeper)
    def check_permission(self, permission: str) -> bool:
        """Verifica si la Ley Humana permite la ejecución"""
        allowed = self.human_contract.allows(permission)
        if not allowed:
            print(f"⛔ [LBH BLOCK] Acción denegada por contrato | permiso: {permission}")
        return allowed

    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print(f"✅ Conectado al Broker: {self.broker}")
            # El Manager se suscribe para escuchar a los Workers
            self.client.subscribe("hormigasais/+/reports")
            print(f"📥 Escuchando reportes del enjambre...")
        else:
            print(f"❌ Error de conexión al Broker. Código: {rc}")

    # 🛡️ PASO 5: Protección de la Acción Real (Procesamiento de datos)
    def _on_message(self, client, userdata, msg):
        """Recibe reportes y solo los procesa si hay permiso humano"""
        
        # Primero revisamos si el contrato permite 'LBH_ASSIST'
        if not self.check_permission("LBH_ASSIST"):
            return # Si es 'false', el motor ignora el mensaje y no hace nada

        try:
            payload_hex = msg.payload.decode()
            
            # 🔐 Aquí el Core usa json_lbh para validar la FIRMA HMAC
            # Si la firma es falsa, el método lanzará un error
            data_dict = lbh_to_json(payload_hex) 

            if self.on_data_handler:
                # Si todo es legal, enviamos los datos al Manager
                self.on_data_handler(msg.topic, data_dict)
                
        except Exception as e:
            print(f"⚠️ [SEGURIDAD] Mensaje rechazado o corrupto: {e}")

    def loop_forever(self):
        """Mantiene al Fiscal (Manager) despierto y escuchando"""
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_forever()

