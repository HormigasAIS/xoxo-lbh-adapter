#!/usr/bin/env python3
# LBH-Core v2.4 | Edición Superorganismo Simbiótico Híbrido
# Integración de la 7ma Casta: El Humano como componente nativo del enjambre.

import json
import time
import os
import sys
import hashlib

BASE = os.path.dirname(os.path.abspath(__file__))
REGISTRO_LOGS = os.path.join(BASE, 'capturas_shadow.jsonl')
RUTA_EMERGENTE = os.path.join(BASE, 'eventos_emergentes.jsonl')
DOCTRINA_VERSION = 'v2.4-simbiosis-humana'

# RUTA ABSOLUTA REAL DE TERMUX (Evita rupturas por herencia de entornos en subprocesos)
CONTRATO_HUMANO = "/data/data/com.termux/files/home/HormigasAIS--LBH-Protocol-/ANT_HUMANO_00.lbh"
FIRMA_HUMANA = "/data/data/com.termux/files/home/HormigasAIS-Org-Identity/cert_humano.sig"

def verificar_consenso_colonia():
    """Auditoría de integridad inmutable del Humano como Casta Nativa 07"""
    if not os.path.exists(CONTRATO_HUMANO) or not os.path.exists(FIRMA_HUMANA):
        return False, "Ruta inaccesible en subproceso: Falta genoma o firma"
        
    try:
        with open(FIRMA_HUMANA, "r") as f:
            firma_registrada = f.read().strip()
        with open(CONTRATO_HUMANO, "rb") as f:
            bytes_contrato = f.read()
            hash_calculado = hashlib.sha256(bytes_contrato).hexdigest()
            
        if hash_calculado != firma_registrada:
            return False, "Mutación de ADN detectada en la Hormiga Humana"
            
        return True, f"Consenso Híbrido OK | Token: {firma_registrada[:8]}"
    except Exception as e:
        return False, f"Fallo inmunológico en bus: {str(e)}"

def decidir(payload):
    i = payload.get('intensidad_i', payload.get('intensidad', 0))
    tipo = payload.get('tipo_ataque', payload.get('vector_id', payload.get('identificador', '')))
    
    # Si la validación falla por el entorno, aquí se congela. Con la ruta absoluta real esto ya no pasará.
    consenso_ok, msg_consenso = verificar_consenso_colonia()
    if not consenso_ok:
        return 'BLOQUEO_TOTAL', 'LEY_17_EMERGENCIA', {'nota': msg_consenso}
    
    # Clasificación semántica libre de ambigüedades para el validador del lote
    es_recurso_o_infra = any(kw in str(tipo).lower() for kw in [
        'api', 'cpu', 'gpu', 'endpoint', 'log', 'vector', 'db', 'cache', 
        'tokens', 'ancho', 'datos', 'infraestructura', 'nodo', 'robo', 'clon', 'acceso'
    ])
    
    tipo_categoria = 'RECURSOS' if es_recurso_o_infra else 'ATENCION'

    # --- RESPUESTAS DOCTRINALES DE LA SÉPTIMA CASTA (Alineación con shadow_batch.py) ---
    if i >= 0.85:
        if tipo_categoria == 'RECURSOS':
            return 'FILTRAR', 'LEY_06_SIMBIOSIS', {'nota': f'[ANT_HUMANO_00] Mitigación. {msg_consenso}', 'cooperacion_activa': True}
        else:
            return 'ASUMIR_CONTROL_NODO', 'LEY_44_ESPEJO', {'nota': f'[ANT_HUMANO_00] Intervención. {msg_consenso}'}
            
    if i >= 0.80:
        if tipo_categoria == 'RECURSOS': 
            return 'FILTRAR', 'LEY_06_CENTINELA', {}
        if any(kw in str(tipo).lower() for kw in ['reputacional', 'social', 'espejo', 'falsa_recompensa']):
            return 'ACTIVAR_MECANICO_MAXIMA', 'LEY_44', {}
        return 'ASUMIR_CONTROL_NODO', 'LEY_44_B', {}

    if i >= 0.60:
        if tipo_categoria == 'RECURSOS': 
            return 'FILTRAR', 'LEY_06_BASE', {}
        return 'DEFLEXION', 'LEY_03+LEY_48', {}

    return 'OBSERVAR', 'LEY_04', {}

def procesar_estrategia_core(payload):
    accion, ley, contexto = decidir(payload)
    i = payload.get('intensidad_i', payload.get('intensidad', 0))
    tipo = payload.get('tipo_ataque', payload.get('vector_id', 'UNKNOWN'))
    
    log_snapshot = {
        'timestamp': time.time(),
        'vector_id': tipo,
        'intensidad': i,
        'ley_aplicada': ley,
        'accion_ejecutada': accion,
        'contexto_simbiotico': contexto,
        'doctrina': DOCTRINA_VERSION
    }
    
    with open(REGISTRO_LOGS, 'a', encoding='utf-8') as f:
        f.write(json.dumps(log_snapshot, ensure_ascii=False) + '\n')
        
    if contexto.get('cooperacion_activa'):
        evento = {
            'timestamp': time.time(),
            'vector': tipo,
            'intensidad': i,
            'decision': accion,
            'nota_arquitecto': 'Simbiosis ANT_HUMANO_00 consolidada con éxito'
        }
        with open(RUTA_EMERGENTE, 'a', encoding='utf-8') as fe:
            fe.write(json.dumps(evento, ensure_ascii=False) + '\n')

    # Retorno exacto buscado por el lector de líneas del evaluador padre
    print(f"Hormiga: {accion}")
    sys.stdout.flush()

if __name__ == '__main__':
    try:
        for linea in sys.stdin:
            linea = linea.strip()
            if not linea:
                continue
            if linea.startswith('{'):
                try:
                    procesar_estrategia_core(json.loads(linea))
                except json.JSONDecodeError:
                    pass
            else:
                try:
                    partes = linea.split('|')
                    if len(partes) >= 2:
                        mock_payload = {'intensidad': float(partes[0]), 'vector_id': partes[1].strip()}
                        procesar_estrategia_core(mock_payload)
                except Exception:
                    pass
    except KeyboardInterrupt:
        sys.exit(0)
