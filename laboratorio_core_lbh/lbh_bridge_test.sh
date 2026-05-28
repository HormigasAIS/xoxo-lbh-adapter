#!/bin/bash

FILE="pulso_braille_gaad.lbh"

echo "📡 [LBH-BUS] Leyendo pulso táctil del laboratorio..."

if [ -f "$FILE" ]; then
    # Leer los bytes del archivo y pasarlos a formato Hexadecimal plano
    PAYLOAD_HEX=$(xxd -p "$FILE" | tr -d '\n')
    
    echo "🆔 PAYLOAD EXTRAÍDO: $PAYLOAD_HEX"
    echo "⚡ TIPO DE FEROMONA: LBH_BRAILLE_CORE"
    
    # Simulación del empaquetado final para el Bus de la colonia
    TIMESTAMP=$(date +%s)
    EVENT_ID=$(openssl rand -hex 8)
    
    echo -e "\n📝 Generando paquete de transmisión..."
    echo "------------------------------------------------"
    echo "▶️ [FEROMONA_EMITIDA]: {\"timestamp\": $TIMESTAMP, \"origin\": \"A16_Soberano\", \"event_id\": \"$EVENT_ID\", \"type\": \"lbh_braille_core\", \"payload\": \"$PAYLOAD_HEX\", \"status\": \"active\"}"
    echo "------------------------------------------------"
    echo "🚀 [ÉXITO] Estructura acoplada al búfer de salida local."
else
    echo "❌ [ERROR] Archivo binario $FILE no encontrado."
fi
