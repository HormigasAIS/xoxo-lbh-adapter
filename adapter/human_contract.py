# adapter/human_contract.py
# © 2025-2026 HormigasAIS - Proyectado por Cristhiam Leonardo Hernández Quiñonez (CLHQ)
# Propiedad Intelectual Protegida bajo el Protocolo de Soberanía LBH
# Lector del Contrato Humano – LBH Protocol v1.2
# Fuente: config.human
# Autoridad máxima: HUMANO

import os
import json

class HumanContract:
    def __init__(self, path="config.human"):
        self.path = os.path.abspath(path)
        self.loaded = False
        self.roles = {}           # Diccionario con permisos por rol
        self.global_permissions = {}
        self.current_role = "GLOBAL"

    def load(self) -> bool:
        if not os.path.exists(self.path):
            print(f"❌ [LBH] Contrato humano no encontrado en: {self.path}")
            return False

        try:
            with open(self.path) as f:
                data = json.load(f)

            # Cargar permisos desde la sección dedicada del JSON
            perms = data.get("PERMISSIONS", {})
            self.global_permissions = { k.upper(): bool(v) for k, v in perms.items() }

            # Mapear roles dinámicos del enjambre para que hereden los permisos
            for r in data.get("ROLES_REGISTRADOS", ["CLHQ", "GLOBAL", "ALPHA", "BETA", "GAMMA"]):
                self.roles[r.upper()] = self.global_permissions.copy()

            self.data = data
            self.loaded = True
            print(f"📖 [LBH] Contrato cargado | Fundador: {data.get('fundador','?')} | Protocolo: {data.get('protocolo','?')}")
            return True

        except Exception as e:
            print(f"❌ [LBH] Error leyendo contrato humano: {e}")
            return False
    def allows(self, permission_name: str) -> bool:
        if not self.loaded:
            self.load()

        permission_name = permission_name.upper()
        # Primero verificamos el rol actual
        role_perms = self.roles.get(self.current_role, {})
        if permission_name in role_perms:
            return role_perms[permission_name]
        # Si no está definido, usamos permisos globales
        return self.global_permissions.get(permission_name, False)

    def set_role(self, role_name: str):
        role_name = role_name.upper()
        if role_name in self.roles:
            self.current_role = role_name
            print(f"🔹 Rol activo cambiado a: {self.current_role}")
        else:
            print(f"⚠️ Rol {role_name} no definido, usando GLOBAL")
            self.current_role = "GLOBAL"
