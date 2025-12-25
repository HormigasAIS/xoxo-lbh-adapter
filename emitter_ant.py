#!/usr/bin/env python3
"""
Emitter Ant (LBH)
Emite feromonas suaves de ayuda al enjambre
(no dicta acciones, solo comunica estado)
"""

import time
import time as _time
from pheromone_bus import emit_pheromone

print("🐜 Emitter Ant activa (LBH)")

def emitter_loop(interval=3, beats=10):
    for i in range(beats):
        pheromone = {
            "type": "HEAT",                 # tipo canónico
            "level": 0.35,                  # intensidad suave (olor, no alarma)
            "source": "emitter_ant",
            "intent": "assist_swarm",
            "confidence": 0.42,
            "ttl": 30,                      # segundos de vida
            "timestamp": int(_time.time()),
            "lbh_compliant": True
        }

        emit_pheromone(pheromone)
        print(f"🧪 Feromona fragante emitida #{i+1}")
        time.sleep(interval)

    print("✅ Emisión completada. Hormiga en reposo.")

if __name__ == "__main__":
    emitter_loop()
