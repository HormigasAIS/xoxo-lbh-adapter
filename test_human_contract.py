from adapter.human_contract import HumanContract

# ---- TEST GLOBAL (sin rol) ----
print("=== GLOBAL (fallback) ===")
hc = HumanContract()
hc.load()

print("LBH_ASSIST:", hc.allows("LBH_ASSIST"))
print("M2M_COMMUNICATION:", hc.allows("M2M_COMMUNICATION"))
print("SANDBOX_MODE:", hc.allows("SANDBOX_MODE"))
print("GOVERNANCE:", hc.allows("GOVERNANCE"))

# ---- TEST POR ROLES ----
for role in ["ALPHA", "BETA", "GAMMA"]:
    print(f"\n=== ROLE {role} ===")
    hc = HumanContract(role=role)
    hc.load()

    print("LBH_ASSIST:", hc.allows("LBH_ASSIST"))
    print("M2M_COMMUNICATION:", hc.allows("M2M_COMMUNICATION"))
    print("SANDBOX_MODE:", hc.allows("SANDBOX_MODE"))
    print("GOVERNANCE:", hc.allows("GOVERNANCE"))
