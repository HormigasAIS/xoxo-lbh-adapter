# COPYRIGHT CONSECUTIVO (C) 2024-2026 ING. CRISTHIAM LEONARDO HERNÁNDEZ QUIÑONEZ (CLHQ)
# SOBERANÍA HORMIGASAIS - PROTOCOLO HMAC PROTEGIDO
"""
XOXO-LBH Adapter - Security Protocol
Autor: Ing. Cristhiam Leonardo Hernández Quiñonez (CLHQ)
Descripción: Gestión de integridad M2M mediante firmas HMAC-SHA256.
"""

import hmac
import hashlib

class Security:
    def __init__(self, secret_key: str):
        """Inicializa la clase con la Llave Maestra del Ingeniero."""
        self.secret_key = secret_key.encode('utf-8')

    def generate_hmac(self, message: str) -> str:
        """Genera firma digital para un mensaje LBH."""
        return hmac.new(self.secret_key, message.encode('utf-8'), hashlib.sha256).hexdigest()

    def validate_hmac(self, message: str, received_hmac: str) -> bool:
        """Valida la soberanía del mensaje recibido."""
        expected_hmac = self.generate_hmac(message)
        return hmac.compare_digest(expected_hmac, received_hmac)
