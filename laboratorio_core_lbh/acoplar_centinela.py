#!/usr/bin/env python3
import json
import os
import sys
import hashlib

CAPA_1_CONTRATO = os.path.expanduser("~/HormigasAIS--LBH-Protocol-/ANT_CENTINELA_02_REBORN.lbh")
CAPA_2_FIRMA = os.path.expanduser("~/HormigasAIS-Org-Identity/cert_centinela_reborn.sig")

def verificar_adn_centinela():
    print("[ACOPLAMIENTO] Iniciando validación cruzada de la Hormiga Centinela...")
    
    if not os.path.exists(CAPA_1_CONTRATO) or not os.path.exists(CAPA_2_FIRMA):
        print("[CRÍTICO] Enlace biológico roto. Falta contrato o firma raíz del Centinela.")
        sys.exit(1)
        
    with open(CAPA_2_FIRMA, "r") as f:
        firma_registrada = f.read().strip()
        
    with open(CAPA_1_CONTRATO, "rb") as f:
        bytes_contrato = f.read()
        hash_calculado = hashlib.sha256(bytes_contrato).hexdigest()
        
    if hash_calculado != firma_registrada:
        print("[ALERTA] INTEGRIDAD VIOLADA. El genoma del Centinela no coincide.")
        sys.exit(1)
        
    print("[OK] ADN del Centinela verificado con éxito.")
    print(f"  Firma Autorizada LBH: {firma_registrada[:10]}...[VÁLIDA]")
    
    with open(CAPA_1_CONTRATO, "r", encoding="utf-8") as f:
        contrato = json.load(f)
    
    print(f"  Agente Acoplado     : {contrato['agent_profile']['identity_id']}")
    print(f"  Casta Biológica     : {contrato['agent_profile']['biological_caste']}")
    print(f"  Acción de Alerta    : I >= {contrato['biological_rules']['criterio_alerta_coordinada']['threshold_i']} -> {contrato['biological_rules']['criterio_alerta_coordinada']['bus_action']}")
    print("="*60)
    print("  HORMIGA CENTINELA VINCULADA CORRECTAMENTE AL SUPERORGANISMO")
    print("="*60)

if __name__ == "__main__":
    verificar_adn_centinela()
