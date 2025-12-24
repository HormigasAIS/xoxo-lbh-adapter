#!/bin/bash
# MODO MAESTRO: Estabilización Térmica Validada
pkill -f python3
sleep 1
> auditor.log

echo "⚖️ Iniciando Enjambre LBH: ALPHA, BETA, GAMMA..."

# 1. El Manager (Cerebro) con un-buffered output (-u)
python3 -u swarm/manager_alpha/manager.py --limite 28.5 >> auditor.log 2>&1 &
sleep 5

# 2. Las 3 Hormigas (Músculo) - Inyección directa
python3 -u swarm/worker_beta/worker.py --id ALPHA --interval 5 >> auditor.log 2>&1 &
python3 -u swarm/worker_beta/worker.py --id BETA --interval 5 >> auditor.log 2>&1 &
python3 -u swarm/worker_beta/worker.py --id GAMMA --interval 5 >> auditor.log 2>&1 &

echo "📊 Puente de datos activado desde EOF..."

while true; do
    # Forzamos la actualización manual al CSV para saltar el error de "no hay datos"
    python3 actualizar_csv.py --once
    python3 visualizador_directo.py
    
    # Verificamos si el log tiene peso real
    TAMANO=$(stat -c%s auditor.log)
    echo "📈 Tamaño del Log: $TAMANO bytes | Registros CSV: $(wc -l < AUDITORIA_HORMIGAS_2025.csv)"
    
    sleep 10
done
