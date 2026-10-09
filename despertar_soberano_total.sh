#!/bin/bash
echo "🛡️ [HormigasAIS] Iniciando Protocolo de Unificación LBH-2025..."

# 1. AUTOCURACIÓN DE MEMORIA (Parche de importación)
python3 -c "
with open('cooling_governor_ant.py', 'r') as f:
    lineas = f.readlines()
with open('cooling_governor_ant.py', 'w') as f:
    for l in lineas:
        f.write(l.replace('from pheromone_bus import read_pheromones', 'from pheromone_bus import emit_pheromone'))
"
echo "✅ Memoria de Enfriamiento sincronizada."

# 2. LIMPIEZA Y PREPARACIÓN DEL BUS
pkill -f "python3"
pkill mosquitto
mosquitto -p 1883 -d
sleep 1
echo "📡 Bus de Feromonas XOXO reiniciado."

# 3. LANZAMIENTO DEL ENJAMBRE VINCULADO
echo "🧠 Activando Gobernador, Mosquitos y Centinela..."
python3 cooling_governor_ant.py &
python3 mosquito_agent.py --mode master &
python3 ant_07_sentinel.py &

# 4. VÍNCULO CON NODO-ESCUELA (MODO APRENDIZAJE)
echo "🚀 Sincronizando aprendizaje mimético con la Escuela..."
./send_intelligence.sh --mode learn

echo "📊 Monitoreando flujo de activos LBH..."
tail -f auditor.log
