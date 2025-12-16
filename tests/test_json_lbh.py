# test_json_lbh.py
"""
Pruebas unitarias para json_lbh.py del XOXO-LBH Adapter
Autor: Cristhiam Quiñonez
"""

import unittest
from adapter.json_lbh import json_to_lbh, lbh_to_json

class TestJsonLBH(unittest.TestCase):

    def setUp(self):
        self.sample_json = {"motor_id": 1, "position": 45, "speed": 100}
        self.lbh_frame = json_to_lbh(self.sample_json)

    def test_conversion_to_lbh(self):
        self.assertIsInstance(self.lbh_frame, bytes)
        self.assertGreater(len(self.lbh_frame), 0)

    def test_conversion_back_to_json(self):
        decoded = lbh_to_json(self.lbh_frame)
        self.assertEqual(decoded, self.sample_json)

if __name__ == "__main__":
    unittest.main()
