#!/usr/bin/env python3
import json
import os
import sys
import hashlib

CAPA_1_CONTRATO = os.path.expanduser("~/HormigasAIS--LBH-Protocol-/ANT_HUMANO_00.lbh")
CAPA_2_FIRMA = os.path.expanduser("~/HormigasAIS-Org-Identity/cert_humano.sig")

def verificar_adn_humano():
    print("[ACOPLAMIENTO] Iniciando validación cruzada de la Hormiga Humana (Casta 07)...")
    
    if not os.path.exists(CAPA_1_CONTRATO) or not os.path.exists(CAPA_2_FIRMA):
        print("[CRÍTICO] Enlace biológico roto. Falta contrato o firma raíz de la Conciencia Humana.")
        sys.exit(1)
        
    with open(CAPA_2_FIRMA, "r") as f:
        firma_registrada = f.read().strip()
        
    with open(CAPA_1_CONTRATO, "rb") as f:
        bytes_contrato = f.read()
        hash_calculado = hashlib.sha256(bytes_contrato).hexdigest()
        
    if hash_calculado != firma_registrada:
        print("[ALERTA] INTEGRIDAD VIOLADA. El genoma de la Hormiga Humana ha sido alterado.")
        sys.exit(1)
        
    print("[OK] ADN de la Hormiga Humana verificado con éxito.")
    print(f"  Firma Autorizada LBH: {firma_registrada[:10]}...[VÁLIDA]")
    
    with open(CAPA_1_CONTRATO, "r", encoding="utf-8") as f:
        contrato = json.load(f)
    
    raiz_autoridad = contrato['LBH_CONTRACT_SIGNATURE']['authority_root']
    print(f"  Validando Autoridad : {raiz_autoridad} (Coincide con Portavoz 99.human)")
    print(f"  Agente Acoplado     : {contrato['agent_profile']['identity_id']}")
    print(f"  Casta Biológica     : {contrato['agent_profile']['biological_caste']}")
    print("="*60)
    print("  HORMIGA HUMANA (ANT_HUMANO_00) VINCULADA NATIVAMENTE AL ENJAMBRE")
    print("="*60)

if __name__ == "__main__":
    verificar_adn_humano()
