#!/bin/bash
echo "🐜 Despertando al Enjambre HormigasAIS..."
python3 swarm/manager_alpha/manager.py > /dev/null 2>&1 &
PID_MANAGER=$!
echo "✅ Auditor activo (PID: $PID_MANAGER)"
sleep 2
python3 swarm/worker_beta/worker.py --id ALPHA > /dev/null 2>&1 &
PID_ALPHA=$!
echo "✅ Worker ALPHA en línea (PID: $PID_ALPHA)"
python3 swarm/worker_beta/worker.py --id BETA > /dev/null 2>&1 &
PID_BETA=$!
echo "✅ Worker BETA en línea (PID: $PID_BETA)"
echo "------------------------------------------"
echo "🚀 ENJAMBRE OPERANDO."
echo "Usa './centinela.sh' para subir a GitHub."
echo "------------------------------------------"
