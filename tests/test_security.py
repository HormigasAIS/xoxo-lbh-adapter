# test_security.py
# © 2025-2026 HormigasAIS - Proyectado por Cristhiam Leonardo Hernández Quiñonez (CLHQ)
# Propiedad Intelectual Protegida bajo el Protocolo de Soberanía LBH
"""
Pruebas unitarias para security.py del XOXO-LBH Adapter
Autor: Cristhiam Quiñonez
"""

import unittest
from adapter.security import hmac_sign, hmac_verify

class TestSecurity(unittest.TestCase):

    def setUp(self):
        self.secret = "mi_clave_secreta"
        self.message = b"comando de prueba"

    def test_hmac_sign(self):
        signature = hmac_sign(self.message, self.secret)
        self.assertIsNotNone(signature)
        self.assertIsInstance(signature, str)

    def test_hmac_verify_correct(self):
        signature = hmac_sign(self.message, self.secret)
        self.assertTrue(hmac_verify(self.message, signature, self.secret))

    def test_hmac_verify_incorrect(self):
        wrong_signature = "0000000000"
        self.assertFalse(hmac_verify(self.message, wrong_signature, self.secret))

if __name__ == "__main__":
    unittest.main()
