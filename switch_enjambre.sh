cat << 'EOF' > switch_enjambre.sh
# © 2025-2026 HormigasAIS - Proyectado por Cristhiam Leonardo Hernández Quiñonez (CLHQ)
# Propiedad Intelectual Protegida bajo el Protocolo de Soberanía LBH
#!/bin/bash
# Switch de Gobernanza LBH - Cristhiam Leonardo

ACCION=$1

if [ "$ACCION" == "stop" ]; then
    sed -i 's/STOP_H_PROT = false/STOP_H_PROT = true/' config.human
    echo "🛑 Señal enviada: Enjambre en modo HIBERNACIÓN (Freeze)."
    ./centinela.sh > /dev/null 2>&1
    echo "✅ Estado sincronizado en GitHub."
elif [ "$ACCION" == "start" ]; then
    sed -i 's/STOP_H_PROT = true/STOP_H_PROT = false/' config.human
    echo "🐜 Señal enviada: Enjambre ACTIVADO (Flow)."
    ./centinela.sh > /dev/null 2>&1
    echo "✅ Estado sincronizado en GitHub."
else
    echo "Uso: ./switch_enjambre.sh [start|stop]"
fi
EOF

chmod +x switch_enjambre.sh

