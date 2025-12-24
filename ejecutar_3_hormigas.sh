#!/bin/bash
# ROL: MAESTRO - Sincronización Total 2025-12-24
pkill -f python3
sleep 1
> auditor.log

echo "⚖️ Iniciando Enjambre LBH (ALPHA, BETA, GAMMA)..."

# Lanzamos Manager y Workers
python3 -u swarm/manager_alpha/manager.py --limite 28.5 >> auditor.log 2>&1 &
python3 -u swarm/worker_beta/worker.py --id ALPHA --interval 5 >> auditor.log 2>&1 &
python3 -u swarm/worker_beta/worker.py --id BETA --interval 5 >> auditor.log 2>&1 &
python3 -u swarm/worker_beta/worker.py --id GAMMA --interval 5 >> auditor.log 2>&1 &

while true; do
    python3 actualizar_csv.py
    python3 visualizador_directo.py
    echo "📈 Latido registrado a las $(date +'%H:%M:%S')"
    sleep 10
done
