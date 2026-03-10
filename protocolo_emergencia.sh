#!/bin/bash
# © 2025-2026 HormigasAIS - Proyectado por Cristhiam Leonardo Hernández Quiñonez (CLHQ)
# Propiedad Intelectual Protegida bajo el Protocolo de Soberanía LBH

# Protocolo de Resiliencia HormigasAIS - Fase 1
BACKUP_DIR=".backups/fase1_v1.0.0"

case "$1" in
    "snapshot")
        echo "📡 Iniciando Snapshot de Seguridad (v1.0.0-LBH)..."
        mkdir -p $BACKUP_DIR
        cp actualizar_csv.py visualizador_rendimiento.py AUDITORIA_HORMIGAS_2025.csv rendimiento.png README.md $BACKUP_DIR/
        echo "✅ Snapshot guardado en $BACKUP_DIR"
        ;;
    "recovery")
        echo "⚠️  Iniciando Restauración de Emergencia..."
        if [ -d "$BACKUP_DIR" ]; then
            cp $BACKUP_DIR/* .
            echo "🛠️  Estado v1.0.0-LBH restablecido con éxito. Gráficos y lógica sincronizados."
        else
            echo "❌ Error: No se encontró el respaldo de la Fase 1."
        fi
        ;;
    *)
        echo "Uso: ./protocolo_emergencia.sh {snapshot|recovery}"
        ;;
esac
