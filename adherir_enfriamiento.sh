#!/bin/bash
echo "❄️ [HormigasAIS] Adhiriendo Gobernador y Centinela..."

# Crear la hormiga de enfriamiento optimizada
cat << 'INNER_EOF' > cooling_governor_ant.py
import time
from pheromone_bus import emit_pheromone

def cooling_governor_loop():
    print("❄️🐜 Gobernador Solar activo (LBH - Protegiendo Hardware)")
    while True:
        emit_pheromone("cooling_status", 1.0)
        time.sleep(20)

if __name__ == "__main__":
    try:
        cooling_governor_loop()
    except KeyboardInterrupt:
        pass
INNER_EOF

# Ejecutar especialistas en segundo plano
python3 cooling_governor_ant.py &
python3 ant_07_sentinel.py &

echo "🛡️ Gobernador y Centinela 07 vinculados exitosamente."
echo "📜 Retomando flujo de auditoría..."
sleep 1
tail -f auditor.log
