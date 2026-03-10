#!/bin/bash
# © 2025-2026 HormigasAIS - Proyectado por Cristhiam Leonardo Hernández Quiñonez (CLHQ)
# Propiedad Intelectual Protegida bajo el Protocolo de Soberanía LBH
pkill -f python3 > /dev/null 2>&1
echo "🐜 Despertando al Enjambre MAESTRO (3 Hormigas)..."
python3 swarm/manager_alpha/manager.py > auditor.log 2>&1 &
sleep 2
python3 swarm/worker_beta/worker.py --id ALPHA > /dev/null 2>&1 &
python3 swarm/worker_beta/worker.py --id BETA > /dev/null 2>&1 &
python3 swarm/worker_beta/worker.py --id GAMMA > /dev/null 2>&1 &
echo "🚀 3 HORMIGAS OPERANDO: ALPHA, BETA y GAMMA."
