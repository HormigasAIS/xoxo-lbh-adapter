# COPYRIGHT CONSECUTIVO (C) 2024-2026 ING. CRISTHIAM LEONARDO HERNÁNDEZ QUIÑONEZ (CLHQ)
from adapter.security import Security
import json

# Llave que solo el Ingeniero y la Colonia conocen
LLAVE_MAESTRA = "CLHQ_SECRET_PROTOCOL_2026"
agente_seguridad = Security(LLAVE_MAESTRA)

print("--- [🐜 VALIDACIÓN DE PODER M2M - ADAPTER V1.2.1] ---")

# CASO 1: ATAQUE EXTERNO (Firma incorrecta)
msg_falso = json.dumps({"sensor": "edge_node", "status": "compromised"})
print("\n[🚨] Intruso intentando inyectar comando...")
if not agente_seguridad.validate_hmac(msg_falso, "hash_falso_123"):
    print("[❌ RECHAZADO] Firma inválida. Piquete de seguridad activo.")

# CASO 2: AUTORIDAD CLHQ (Firma correcta)
msg_real = json.dumps({"sensor": "edge_node", "status": "operativo"})
firma_clhq = agente_seguridad.generate_hmac(msg_real)
print(f"\n[✅] Ingeniero enviando comando con firma: {firma_clhq[:32]}...")

if agente_seguridad.validate_hmac(msg_real, firma_clhq):
    print("[🐜 ACCESO CONCEDIDO] Sello de Cristhiam Leonardo Hernández Quiñonez validado.")

print("\n--- [PRUEBA FINALIZADA] ---")
