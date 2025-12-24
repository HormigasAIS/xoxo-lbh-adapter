# adapter/human_contract.py
# Lector del Contrato Humano – LBH Protocol v1.2
# Fuente: config.human
# Autoridad máxima: HUMANO

import os
import configparser

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
            parser = configparser.ConfigParser()
            parser.read(self.path)

            # Cargar permisos globales
            if "PERMISSIONS" in parser:
                self.global_permissions = {k.upper(): parser.getboolean("PERMISSIONS", k)
                                           for k in parser["PERMISSIONS"]}

            # Cargar roles
            for section in parser.sections():
                if section.startswith("ROLE:"):
                    role_name = section.split(":")[1].upper()
                    perms = {k.upper(): parser.getboolean(section, k)
                             for k in parser[section] if parser[section][k].lower() in ["true", "false"]}
                    self.roles[role_name] = perms

            self.loaded = True
            print(f"📖 [LBH] Contrato cargado | Roles: {list(self.roles.keys())}")
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
