#!/bin/bash
# PROTOCOLO LBH: Reparación de Firma de Feromona - 24 Dic 2025

# 1. Lanzamos la Emitter Ant corregida (Pasando type y value por separado)
python3 -c "
import time
from pheromone_bus import emit_pheromone
print('🐜 Emitter Ant REPARADA y vinculada...')
def loop():
    for i in range(30):
        # Ahora pasamos los argumentos correctos al bus
        emit_pheromone('cooling_hint', 0.42, origin='emitter_ant')
        time.sleep(3)
loop()
" &

# 2. Ejecutamos las 3 hormigas de carga
./ejecutar_3_hormigas.sh
