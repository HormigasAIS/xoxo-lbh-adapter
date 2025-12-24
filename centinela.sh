#!/bin/bash

# --- Configuración ---
SCRIPT_GRAFICA="swarm/manager_alpha/generador_reporte.py"

echo "🚀 [$(date)] Iniciando ciclo de actualización del Centinela..."

# 1. Generar la nueva gráfica
python3 $SCRIPT_GRAFICA

# 2. Verificar si la gráfica se creó
if [ -f "REPORTE_RENDIMIENTO_HORMIGAS.png" ]; then
    echo "📊 Gráfica actualizada localmente."
    
    # 3. Sincronizar TODO el ecosistema (Reportes + Scripts nuevos)
    git add .
    git commit -m "🤖 Centinela: Sincronización completa del ecosistema [$(date +'%Y-%m-%d %H:%M')]"
    git push origin main
    
    echo "✅ [$(date)] Dashboard y Scripts sincronizados globalmente."
else
    echo "❌ Error: No se pudo generar el reporte gráfico."
fi
