#!/usr/bin/env python3
import json
import os
import sys
import hashlib

# Parámetros de la arquitectura de la Colonia
CAPA_1_CONTRATO = os.path.expanduser("~/HormigasAIS--LBH-Protocol-/ANT_PORTAVOZ_01_REBORN.lbh")
CAPA_2_FIRMA = os.path.expanduser("~/HormigasAIS-Org-Identity/cert_portavoz_reborn.sig")

def verificar_adn_biologico():
    print("[ACOPLAMIENTO] Iniciando validación cruzada de la Hormiga Portavoz...")
    
    # 1. Comprobar existencia física
    if not os.path.exists(CAPA_1_CONTRATO) or not os.path.exists(CAPA_2_FIRMA):
        print("[CRÍTICO] Enlace biológico roto. Falta contrato o firma raíz.")
        sys.exit(1)
        
    # 2. Leer firma registrada en Capa 2
    with open(CAPA_2_FIRMA, "r") as f:
        firma_registrada = f.read().strip()
        
    # 3. Calcular hash en tiempo real del contrato en Capa 1
    with open(CAPA_1_CONTRATO, "rb") as f:
        bytes_contrato = f.read()
        hash_calculado = hashlib.sha256(bytes_contrato).hexdigest()
        
    # 4. Auditoría de Identidad Soberana
    if hash_calculado != firma_registrada:
        print("[ALERTA] INTEGRIDAD VIOLADA. El genoma no coincide con la firma oficial.")
        print(f"  Calculado: {hash_calculado}")
        print(f"  Registrado: {firma_registrada}")
        sys.exit(1)
        
    print("[OK] ADN Verificado de forma cruzada.")
    print(f"  Firma Autorizada LBH: {firma_registrada[:10]}...[VÁLIDA]")
    
    # 5. Cargar la matriz doctrinal para el adaptador
    with open(CAPA_1_CONTRATO, "r", encoding="utf-8") as f:
        contrato = json.load(f)
    
    print(f"  Agente Acoplado     : {contrato['agent_profile']['identity_id']}")
    print(f"  Casta Biológica     : {contrato['agent_profile']['biological_caste']}")
    print(f"  Umbral de Relevo    : I >= {contrato['biological_rules']['criterio_relevo_asincrono']['threshold_i']} -> {contrato['biological_rules']['criterio_relevo_asincrono']['bus_action']}")
    print("="*60)
    print("  HORMIGA PORTAVOZ VINCULADA CORRECTAMENTE AL SUPERORGANISMO")
    print("="*60)

if __name__ == "__main__":
    verificar_adn_biologico()
