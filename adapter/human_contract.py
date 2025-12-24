# adapter/human_contract.py
# Lector del Contrato Humano – LBH Protocol
# Fuente: swarm/contracts/config.human

import os


class HumanContract:
    def __init__(self, path="swarm/contracts/config.human"):
        # Ruta absoluta para evitar errores en Termux
        self.path = os.path.abspath(path)
        self.loaded = False
        self.permissions = {}

    def load(self) -> bool:
        if not os.path.exists(self.path):
            print(f"❌ [LBH] Contrato humano no encontrado en: {self.path}")
            return False

        try:
            with open(self.path, "r") as f:
                content = f.read()

            self._parse(content)
            self.loaded = True
            print(f"📖 [LBH] Contrato cargado | Permisos: {self.permissions}")
            return True

        except Exception as e:
            print(f"❌ [LBH] Error leyendo contrato humano: {e}")
            return False

    def _parse(self, content: str):
        # Normalizamos contenido para evitar errores de mayúsculas/minúsculas
        content_lower = content.lower()

        # Permisos reconocidos por el core
        self.permissions["LBH_ASSIST"] = "lbh_assist = true" in content_lower
        self.permissions["M2M_COMMUNICATION"] = "m2m_communication = true" in content_lower
        self.permissions["SANDBOX_MODE"] = "sandbox_mode = true" in content_lower

    def allows(self, permission_name: str) -> bool:
        if not self.loaded:
            self.load()

        return self.permissions.get(permission_name, False)
