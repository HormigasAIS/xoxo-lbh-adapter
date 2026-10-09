#!/usr/bin/env python3
# © 2025-2026 HormigasAIS - Proyectado por Cristhiam Leonardo Hernández Quiñonez (CLHQ)
# Propiedad Intelectual Protegida bajo el Protocolo de Soberanía LBH
import time
from pheromone_bus import emit_pheromone

# Coordenadas de Operación: San Miguel, El Salvador
GEO_LOC = {"lat": 13.4833, "lon": -88.1833, "city": "San Miguel", "country": "SV"}

def emitter_loop():
    print(f"🌍 Emitter Ant Localizada en: {GEO_LOC['city']}, {GEO_LOC['country']}")
    for i in range(10):
        # Inyectamos la ubicación en la feromona de asistencia
        emit_pheromone('cooling_hint', 0.42, origin='emitter_ant_geo')
        # Emitimos pulso de ubicación para el mapa del Dashboard
        emit_pheromone('geo_pulse', GEO_LOC, origin='satelital')
        
        print(f"🛰️ Pulso geográfico #{i+1} emitido desde el Nodo SV")
        time.sleep(5)

if __name__ == "__main__":
    emitter_loop()
