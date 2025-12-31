#!/bin/bash
# --- PROTOCOLO LBH: EVOLUCIÓN DE AUTO-CURACIÓN BÍODIRECCIONAL ---
# Fundador: Cristhiam Hernández | San Miguel, El Salvador
# Roles: Stanford (Traductora/Analista) & Enfermera (Reparadora/Operativa)

echo "🐜 Sincronizando Ecosistema HormigasAIS con Ciclo de Retorno..."

# 1. SEGURIDAD: Backup del ADN (Propiedad Intelectual)
mkdir -p ./boveda_seguridad
[ -f "lbh.human" ] && cp lbh.human ./boveda_seguridad/lbh_$(date +%Y%m%d_%H%M%S).human
echo "🔐 ADN resguardado en bóveda."

# 2. SISTEMA NERVIOSO: Activación de Bus XOXO
if pgrep "mosquitto" > /dev/null; then
    echo "✅ Bus XOXO ya está operando."
else
    mosquitto -d 2>/dev/null
    echo "📡 Bus XOXO (MQTT) activado."
fi

# 3. LANZAMIENTO DE NODOS (Sectores 8080, 8081, 8082)
nohup python3 -m http.server 8081 > /dev/null 2>&1 & # Nodo Escuela
nohup python3 server_arquitectura.py > /dev/null 2>&1 & # Mapa LBH
nohup python3 -m http.server 8080 > /dev/null 2>&1 & # Nodo Solar

# 4. LÓGICA DE AUTO-CURACIÓN Y RETROALIMENTACIÓN (Stanford <-> Enfermera)
(
while true; do
  for puerto in 8080 8081 8082; do
    if ! lsof -Pi :$puerto -sTCP:LISTEN -t >/dev/null; then
      
      # [PASO A] STANFORD detecta daño y envía coordenadas a la Enfermera
      mosquitto_pub -h localhost -t "xoxo/interno/stanford" -m "{\"alerta\":\"daño\", \"coord\":\"$puerto\"}"
      
      # [PASO B] ENFERMERA responde confirmando recepción y carga de trabajo
      # Informa que se hace cargo sin abandonar sus otras tareas
      mosquitto_pub -h localhost -t "xoxo/interno/enfermera" -m "{\"status\":\"reparando\", \"carga\":\"normal\", \"msg\":\"Trabajando en sector $puerto\"}"
      
      # [PASO C] REPARACIÓN FÍSICA (La Enfermera ejecuta la coordenada)
      if [ $puerto -eq 8081 ]; then nohup python3 -m http.server 8081 > /dev/null 2>&1 & fi
      if [ $puerto -eq 8082 ]; then nohup python3 server_arquitectura.py > /dev/null 2>&1 & fi
      if [ $puerto -eq 8080 ]; then nohup python3 -m http.server 8080 > /dev/null 2>&1 & fi
      
      # [PASO D] STANFORD recibe la seguridad de la Enfermera y calma al enjambre
      # Se emite feromona de estabilidad al flujo principal
      sleep 2
      mosquitto_pub -h localhost -t "hormigas/colonia/status" -m "{\"msg\":\"Seguridad Restablecida\", \"operacion\":\"continua\", \"emisor\":\"Stanford\"}"
    fi
  done
  sleep 30 # Ciclo de atención constante
done
) &

echo "-------------------------------------------------------"
echo "✅ Roles Stanford y Enfermera sincronizados en canal interno."
echo "✅ Canal de retorno activado: La Enfermera ahora reporta su estado."
echo "🚀 Ecosistema LBH Blindado y Autocurativo en San Miguel."
