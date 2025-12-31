#!/bin/bash
echo "🐜 [HormigasAIS] Iniciando Despertar Normal..."
pkill -9 -f python
pkill -9 mosquitto
sleep 1
mosquitto -p 1883 -d
python3 start_lbh_edge.py &
sleep 2
python3 mosquito_agent.py --mode master &
echo "📡 Bus y Mosquitos activos."
