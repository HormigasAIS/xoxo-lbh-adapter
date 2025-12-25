#!/usr/bin/env python3
"""
pheromone_bus.py - Evolución XOXO-LBH
Transporta señales y las inyecta en el adaptador para monitoreo global.
"""

import time
import json
from collections import deque

# Buffer circular de 64 feromonas (Memoria volátil)
_PHEROMONE_BUFFER = deque(maxlen=64)

def emit_pheromone(type_p, value, origin="hormiga_maestra"):
    """
    Emite una feromona y la prepara para el adaptador XOXO.
    """
    pheromone = {
        "timestamp": time.time(),
        "type": type_p,
        "value": value,
        "origin": origin,
        "protocol": "LBH-2025"
    }
    _PHEROMONE_BUFFER.append(pheromone)
    
    # Inyección inmediata al adaptador (simulación de pipe o log)
    with open("auditor.log", "a") as f:
        f.write(f"📡 [XOXO-BUS] FEROMONA_EMITIDA: {json.dumps(pheromone)}\n")
    
    # Si es de tipo CALOR, disparamos el protocolo de enfriamiento
    if type_p == "CALOR" and value >= 32:
        print(f"🚨 ALERT: {value}°C detectados. Notificando a xoxo-lbh-adapter...")

def read_pheromones():
    """ Lee el estado actual del enjambre """
    return list(_PHEROMONE_BUFFER)

if __name__ == "__main__":
    # Prueba de integración
    emit_pheromone("ESTADO", "INICIO_ENSAYO", "maestro")
    print("✅ Bus de Feromonas vinculado al adaptador XOXO.")
