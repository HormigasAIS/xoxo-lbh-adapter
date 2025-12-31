#!/bin/bash
echo "🛡️ [XOXO-LBH] Iniciando Despertar de la Colonia con Protocolo EOF..."

# 1. Limpieza de procesos huérfanos
pkill -f "python3"
pkill mosquitto

# 2. Reinicio del Bus de Feromonas (Broker)
mosquitto -p 1883 -d

# 3. Lanzamiento del Adaptador Maestro (Gateway)
python3 start_lbh_edge.py &
sleep 2

# 4. Inyección del Enjambre Solar (ALPHA, BETA, GAMMA)
# Usamos el orquestador que ya conoce los argumentos de origen
python3 xoxo_init.py &

echo "🚀 Enjambre despierto. Monitoreando Auditoría LBH..."
tail -f auditor.log
