#!/bin/bash

# --- Configuración ---
SCRIPT_GRAFICA="swarm/manager_alpha/generador_reporte.py"

echo "🚀 [$(date)] Iniciando ciclo de actualización del Centinela..."

# 1. ACTIVAR ENTORNO VIRTUAL (Para asegurar que encuentre pandas)
source venv_xoxo/bin/activate

# 2. Generar la nueva gráfica
python3 $SCRIPT_GRAFICA

# 3. Verificar si la gráfica se creó
if [ -f "REPORTE_RENDIMIENTO_HORMIGAS.png" ]; then
    echo "📊 Gráfica actualizada localmente."
    
    # 4. Sincronizar TODO
    git add .
    git commit -m "🤖 Centinela: Sincronización con entorno validado [$(date +'%Y-%m-%d %H:%M')]"
    git push origin main
    
    echo "✅ [$(date)] Dashboard y Scripts sincronizados globalmente."
else
    echo "❌ Error: No se pudo generar el reporte gráfico."
fi
