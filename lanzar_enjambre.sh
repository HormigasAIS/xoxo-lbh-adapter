#!/bin/bash

# Limpiar procesos previos para evitar conflictos
pkill -f python3 > /dev/null 2>&1

echo "🐜 Despertando al Enjambre HormigasAIS..."
echo "------------------------------------------"

# 1. Iniciar el Manager (Auditor)
# Redirigimos la salida a un log para que no ensucie tu terminal principal
python3 swarm/manager_alpha/manager.py > auditor.log 2>&1 &
PID_MANAGER=$!
echo "✅ Auditor activo (PID: $PID_MANAGER)"

sleep 2

# 2. Iniciar Worker ALPHA
python3 swarm/worker_beta/worker.py --id ALPHA > /dev/null 2>&1 &
PID_ALPHA=$!
echo "✅ Worker ALPHA en línea (PID: $PID_ALPHA)"

# 3. Iniciar Worker BETA
python3 swarm/worker_beta/worker.py --id BETA > /dev/null 2>&1 &
PID_BETA=$!
echo "✅ Worker BETA en línea (PID: $PID_BETA)"

echo "------------------------------------------"
echo "🚀 ENJAMBRE OPERANDO EN SEGUNDO PLANO."
echo "Los datos se están guardando en 'AUDITORIA_HORMIGAS_2025.csv'."
echo "Usa './centinela.sh' para actualizar tu GitHub."
echo "Para detener todo, usa: pkill -f python3"
echo "------------------------------------------"
