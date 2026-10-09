#!/bin/bash
# --- PROTOCOLO LBH: DESPLIEGUE CIEGO SOBERANO ---
# Fundador: Cristhiam Hernández | San Miguel, El Salvador

TIMESTAMP_UTC=$(date -u +"%Y%m%dT%H%M%SZ")

echo "📡 EMISOR: HORMIGA_10_SOBERANA"
echo "🧹 Limpieza de seguridad: Eliminando bloqueos de puerto..."

# 1. Fuerza Bruta: Terminamos cualquier proceso que use Python o Mosquitto
pkill -9 python3 2>/dev/null
pkill -9 mosquitto 2>/dev/null
sleep 3

# 2. Reconstrucción Directa: La Enfermera levanta los sectores sin preguntar
echo "🏗️ La Enfermera está reconstruyendo los sectores 8080, 8081, 8082..."

nohup python3 -m http.server 8080 > /dev/null 2>&1 &
nohup python3 -m http.server 8081 > /dev/null 2>&1 &
nohup python3 server_arquitectura.py > /dev/null 2>&1 &

sleep 2

# 3. Activación del Bus XOXO
mosquitto -d 2>/dev/null

echo "-------------------------------------------------------"
echo "🚀 Ecosistema LBH Normalizado."
echo "🌐 Status Page forzada en: http://localhost:8081"
echo "📅 Timestamp LBH: $TIMESTAMP_UTC"
