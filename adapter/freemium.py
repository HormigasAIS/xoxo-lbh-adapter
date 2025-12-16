# freemium.py
"""
XOXO-LBH Adapter - Freemium Module
Autor: Cristhiam Quiñonez
Descripción:
Gestiona funcionalidades Freemium/Premium para usuarios o robots.
Integración con LBH-M2M y XOXOAdapter para limitar o habilitar comandos.
"""

from adapter import XOXOAdapter, json_to_lbh, lbh_to_json

class FreemiumManager:
    def __init__(self, adapter: XOXOAdapter, mode: str = "freemium"):
        """
        Inicializa el manager con el adapter y el modo de uso
        :param adapter: Instancia de XOXOAdapter
        :param mode: "freemium" o "premium"
        """
        self.adapter = adapter
        self.mode = mode.lower()
        self.command_limit = 3 if self.mode == "freemium" else None
        self.sent_commands = 0

    def can_send_command(self) -> bool:
        """
        Verifica si se puede enviar un comando según el plan
        """
        if self.mode == "premium":
            return True
        return self.sent_commands < self.command_limit

    def send_command(self, payload: dict):
        """
        Envía un comando al robot vía LBH-M2M, respetando límites Freemium
        """
        if not self.can_send_command():
            print("[FreemiumManager] Límite de comandos alcanzado para Freemium.")
            return False

        try:
            # Convertimos a LBH y enviamos
            lbh_frame = json_to_lbh(payload)
            self.adapter.publish_act(**payload)
            self.sent_commands += 1
            print(f"[FreemiumManager] Comando enviado: {payload}")
            return True
        except Exception as e:
            print("[FreemiumManager] Error enviando comando:", e)
            return False

    def reset_counter(self):
        """
        Resetea el contador de comandos Freemium (por ejemplo, diario)
        """
        self.sent_commands = 0
        print("[FreemiumManager] Contador de comandos reseteado.")
