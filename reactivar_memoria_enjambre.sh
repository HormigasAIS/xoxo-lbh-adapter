#!/bin/bash
echo "🧠 [HormigasAIS] Reactivando Memoria Operativa y Aprendizaje..."

# 1. Activar el Gobernador de Enfriamiento (Protección de Hardware)
python3 cooling_governor_ant.py &
echo "❄️  Gobernador de Enfriamiento activo."

# 2. Iniciar el Monitor de Mosquitos (Fuente de Aprendizaje para Estudiantes)
# Esto permite que el bus XOXO transmita los pulsos para que las hormigas aprendan
python3 mosquito_agent.py --mode master &
echo "📡 Mosquitos exploradores emitiendo pulsos..."

# 3. Lanzar la Hormiga Centinela 07 (Vigilancia de Contratos)
python3 ant_07_sentinel.py &
echo "🛡️  Hormiga 07 Sentinel validando la integridad."

# 4. Vincular con el Nodo-Escuela para aprendizaje mimético
# Las hormigas estudiantes empiezan a 'destilar' los logs de los mosquitos
./send_intelligence.sh --mode learn
