#!/bin/bash
# --- PROTOCOLO LBH: AUTO-CURACIÓN CON LIMPIEZA DE PRE-VUELO ---
# Fundador: Cristhiam Hernández | San Miguel

echo "🐜 Limpiando sectores previos..."
pkill -f python3 2>/dev/null

echo "🐜 Sincronizando Ecosistema HormigasAIS con Ciclo de Retorno..."

# 1. SEGURIDAD PRE-VUELO
mkdir -p ./boveda_seguridad
[ -f "lbh.human" ] && cp lbh.human ./boveda_seguridad/lbh_$(date +%Y%m%d_%H%M%S).human

# 2. ACTIVACIÓN DEL SISTEMA NERVIOSO (XOXO)
pgrep -x mosquitto > /dev/null || mosquitto -d 2>/dev/null

# 3. LANZAMIENTO DE NODOS
nohup python3 -m http.server 8081 > /dev/null 2>&1 &
nohup python3 server_arquitectura.py > /dev/null 2>&1 &
nohup python3 -m http.server 8080 > /dev/null 2>&1 &

# 4. LÓGICA DE COMUNICACIÓN DE VUELTA (Stanford <-> Enfermera)
(
while true; do
  for puerto in 8080 8081 8082; do
    if ! lsof -Pi :$puerto -sTCP:LISTEN -t >/dev/null; then
      mosquitto_pub -h localhost -t "xoxo/interno/stanford" -m "{\"alerta\":\"daño\", \"coord\":\"$puerto\"}"
      mosquitto_pub -h localhost -t "xoxo/interno/enfermera" -m "{\"status\":\"reparando\", \"msg\":\"Trabajando en $puerto\"}"
      
      if [ $puerto -eq 8081 ]; then nohup python3 -m http.server 8081 > /dev/null 2>&1 & fi
      if [ $puerto -eq 8082 ]; then nohup python3 server_arquitectura.py > /dev/null 2>&1 & fi
      if [ $puerto -eq 8080 ]; then nohup python3 -m http.server 8080 > /dev/null 2>&1 & fi
      
      sleep 2
      mosquitto_pub -h localhost -t "hormigas/colonia/status" -m "{\"msg\":\"Seguridad Restablecida\", \"emisor\":\"Stanford\"}"
    fi
  done
  sleep 30
done
) &

echo "-------------------------------------------------------"
echo "✅ Sectores limpios y agentes reasignados."
echo "🚀 Ecosistema LBH Blindado en San Miguel."
