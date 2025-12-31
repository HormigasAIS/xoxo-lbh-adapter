#!/bin/bash
# 1. Limpieza de procesos previos
echo "🧹 Limpiando el hormiguero..."
pkill -9 python3
pkill -9 mosquitto
sleep 1

# 2. Configuración del Bus XOXO (Soberanía y Red Abierta)
echo "📡 Configurando el Bus XOXO para IP 192.168.1.3..."
cat << 'CONF_EOF' > mosquitto.conf
allow_anonymous true
listener 1883 0.0.0.0
protocol mqtt
listener 9001 0.0.0.0
protocol websockets
CONF_EOF

# 3. Lanzamiento del Corazón del Sistema
mosquitto -c mosquitto.conf -d
python3 start_lbh_edge.py &
sleep 2

# 4. Lanzamiento de Agentes (Mosquito y Gobernador)
python3 mosquito_agent.py --mode master &
python3 cooling_governor_ant.py &
python3 ant_07_sentinel.py &

# 5. Lanzamiento del Interfaz Visual (Dashboard)
echo "🌐 Levantando Interfaz Visual en http://192.168.1.3:8080"
python3 -m http.server 8080 &

echo "-------------------------------------------------------"
echo "✅ NODO HORMIGASAIS TOTALMENTE OPERATIVO (Nivel 1)"
echo "🚀 El enjambre está activo y visible en la red local."
echo "-------------------------------------------------------"

# Monitoreo final
tail -f auditor.log
