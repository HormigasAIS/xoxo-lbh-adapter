# test_core.py
"""
Pruebas unitarias para core.py de XOXO-LBH Adapter
Autor: Cristhiam Quiñonez
"""

import unittest
from adapter.core import XOXOAdapter, json_to_lbh, lbh_to_json

class TestCore(unittest.TestCase):

    def setUp(self):
        # Crear instancia de adapter simulando un robot de prueba
        self.adapter = XOXOAdapter(broker="localhost", robot_id="robot_test")
        self.test_payload = {"motor_id": 1, "position": 90, "speed": 120}
        self.lbh_frame = json_to_lbh(self.test_payload)

    def test_json_to_lbh(self):
        # Verifica que la conversión de JSON a LBH no esté vacía
        self.assertIsNotNone(self.lbh_frame)
        self.assertIsInstance(self.lbh_frame, bytes)

    def test_lbh_to_json(self):
        # Convierte de nuevo LBH a JSON y verifica integridad
        decoded = lbh_to_json(self.lbh_frame)
        self.assertEqual(decoded, self.test_payload)

    def test_publish_act(self):
        # Publicación simulada de un comando de actuador
        try:
            self.adapter.publish_act(**self.test_payload)
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

    def test_set_handler(self):
        # Verifica que se pueda asignar un handler
        try:
            self.adapter.set_handler(lambda topic, data: print(topic, data))
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
