#!/bin/bash

# --- Configuración de rutas soberanas ---
CORTEX_RESULTADO="/data/data/com.termux/files/home/Laboratorio_Adopcion/NodoEscuela_Gemini_Nuevo/cortex_aprendizaje/pensamiento_final.json"
SITE_DATA="/data/data/com.termux/files/home/hormigasais-site/js/estado_hormiga.json"

echo "📡 [puente_feromonas] Iniciando sincronización de feromonas..."

# Verificar si el pensamiento existe antes de intentar copiarlo
if [ -f "$CORTEX_RESULTADO" ]; then
    # Copiar con validación
    cp "$CORTEX_RESULTADO" "$SITE_DATA"
    
    # Asegurar permisos para que el servidor web pueda leer el archivo
    chmod 644 "$SITE_DATA"
    
    echo "✅ [puente_feromonas] Estado de la colonia actualizado en el frontend."
    echo "💾 Archivo destino: $SITE_DATA"
else
    echo "⚠️ [puente_feromonas] Error: No se encontró pensamiento_final.json en el cortex."
fi

