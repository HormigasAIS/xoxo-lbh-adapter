# adapter/__init__.py
# © 2025-2026 HormigasAIS - Proyectado por Cristhiam Leonardo Hernández Quiñonez (CLHQ)
# Propiedad Intelectual Protegida bajo el Protocolo de Soberanía LBH
# Este archivo sincroniza el Core y la Seguridad HMAC
from .core import XOXOAdapter
from .json_lbh import json_to_lbh, lbh_to_json

__all__ = [
    "XOXOAdapter",
    "json_to_lbh",
    "lbh_to_json"
]
