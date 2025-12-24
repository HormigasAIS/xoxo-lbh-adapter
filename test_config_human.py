# test_config_human.py
from adapter.human_contract import HumanContract

# Cargar el contrato desde la raíz
hc = HumanContract(path="config.human")
hc.load()

# Mostrar permisos globales (fallback)
print("=== GLOBAL PERMISSIONS (fallback) ===")
for perm in [
    "LBH_ASSIST", "M2M_COMMUNICATION", "SANDBOX_MODE", "GOVERNANCE",
    "SHUTDOWN_ROBOT", "MODIFY_ROLES", "OVERRIDE_PERMISSIONS",
    "ACCESS_SENSITIVE_DATA", "FORCE_STOP_TASK"
]:
    print(f"{perm}: {hc.allows(perm)}")
print()  # Separador

# Mostrar permisos por rol definido
for role in ["ALPHA", "BETA", "GAMMA"]:
    hc.set_role(role)
    print(f"=== ROLE {role} ===")
    for perm in [
        "LBH_ASSIST", "M2M_COMMUNICATION", "SANDBOX_MODE", "GOVERNANCE",
        "SHUTDOWN_ROBOT", "MODIFY_ROLES", "OVERRIDE_PERMISSIONS",
        "ACCESS_SENSITIVE_DATA", "FORCE_STOP_TASK"
    ]:
        print(f"{perm}: {hc.allows(perm)}")
    print()  # Separador entre roles
