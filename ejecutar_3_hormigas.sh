#!/bin/bash
# ROL: MAESTRO - Sincronización de 5 Columnas (Ajuste Final)
pkill -f python3
sleep 1
echo "FECHA_HORA,ID_HORMIGA,ESTADO,DATO_VALOR,FIRMA_LBH" > AUDITORIA_HORMIGAS_2025.csv
> auditor.log

echo "⚖️ Iniciando Enjambre LBH..."

# 1. Manager y Hormigas
python3 -u swarm/manager_alpha/manager.py --limite 28.5 >> auditor.log 2>&1 &
python3 -u swarm/worker_beta/worker.py --id ALPHA --interval 5 >> auditor.log 2>&1 &
python3 -u swarm/worker_beta/worker.py --id BETA --interval 5 >> auditor.log 2>&1 &
python3 -u swarm/worker_beta/worker.py --id GAMMA --interval 5 >> auditor.log 2>&1 &

while true; do
    # Transformación: Mueve el primer número (temp) a la 4ta columna
    # De: TEMP,ESTADO,TIME -> A: FECHA,ID,ESTADO,TEMP,LBH_OK
    sed -i 's/^\([0-9.]*\),\(OPERATIONAL\),.*/2025-12-24,WORKER,\2,\1,LBH_OK/' AUDITORIA_HORMIGAS_2025.csv
    
    python3 actualizar_csv.py --once
    python3 visualizador_directo.py
    
    TOTAL=$(wc -l < AUDITORIA_HORMIGAS_2025.csv)
    echo "📈 Registros Estructurados: $TOTAL | $(date +'%H:%M:%S')"
    sleep 10
done
