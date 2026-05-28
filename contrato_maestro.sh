#!/bin/bash
# © 2025-2026 HormigasAIS - Proyectado por Cristhiam Leonardo Hernández Quiñonez (CLHQ)
# Propiedad Intelectual Protegida bajo el Protocolo de Soberanía LBH
# ROL: SACERDOTE - Custodiando la paz térmica
# ROL: JUEZ - Dictaminando el límite sagrado de 30.0

# 1. El Juez limpia el terreno de forma absoluta (Purga de procesos zombis)
pkill -f python3

# 2. El Juez dicta su sentencia de forma independiente
echo "⚖️ Contrato LBH Activo: El Juez ha dictaminado el límite en 30.0"

# 3. El Manager (Auditor) se levanta con la firma del Sacerdote
python3 swarm/manager_alpha/manager.py --limite 30.0 --strict > auditor.log 2>&1 &
sleep 2

# 4. Las Hormigas (Subordinados) entran en el redil de la rectificación
python3 swarm/worker_beta/worker.py --id ALPHA --contract_limit 30.0 > /dev/null 2>&1 &
python3 swarm/worker_beta/worker.py --id BETA --contract_limit 30.0 > /dev/null 2>&1 &
python3 swarm/worker_beta/worker.py --id GAMMA --contract_limit 30.0 > /dev/null 2>&1 &

echo "🕯️ Sacerdote: El enjambre ha sido bendecido. La paz de los 25°C sea con el sistema."

