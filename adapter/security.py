# COPYRIGHT CONSECUTIVO (C) 2024-2026 ING. CRISTHIAM LEONARDO HERNÁNDEZ QUIÑONEZ (CLHQ)
# SOBERANÍA HORMIGASAIS - PROTOCOLO HMAC PROTEGIDO
# security.py
"""
XOXO-LBH Adapter - Security
Autor: Cristhiam Quiñonez
Descripción:
Proporciona funciones de seguridad para:
- Generación de HMAC para autenticidad de mensajes
- Validación de paquetes LBH recibidos
- Base para futuras capas de cifrado y firma
"""

import hmac
import hashlib

class Security:
    def __init__(self, secret_key: str):
        """
        Inicializa la clase con una clave secreta
        """
        self.secret_key = secret_key.encode('utf-8')

    def generate_hmac(self, message: str) -> str:
        """
        Genera HMAC-SHA256 para un mensaje dado
        """
        return hmac.new(self.secret_key, message.encode('utf-8'), hashlib.sha256).hexdigest()

    def validate_hmac(self, message: str, received_hmac: str) -> bool:
        """
        Valida que el HMAC recibido coincida con el mensaje
        """
        expected_hmac = self.generate_hmac(message)
        return hmac.compare_digest(expected_hmac, received_hmac)
