#!/bin/bash
# © 2025-2026 HormigasAIS - Proyectado por Cristhiam Leonardo Hernández Quiñonez (CLHQ)
# Propiedad Intelectual Protegida bajo el Protocolo de Soberanía LBH
# --------------------------------------------------
# Ritual de Integración de Señal Externa (NO ejecución)
# Sistema: XOXO LBH Adapter
# Origen: Nodo-Escuela
# Tipo: Huella de soberanía humana
# --------------------------------------------------

BASE_DIR="$HOME/xoxo-lbh-adapter"
SOURCE_REGLAMENTO="$HOME/HormigasAIS--LBH-Protocol-/config/REGLAMENTOS_externo.yaml"
TARGET_DIR="$BASE_DIR/signals/external"

echo "🧬 Preparando canal sensorial externo para XOXO..."

# 1. Crear directorio de señales externas si no existe
mkdir -p "$TARGET_DIR"

# 2. Enlazar reglamento como huella (no copia, no ejecución)
if [ ! -L "$TARGET_DIR/REGLAMENTOS_externo.yaml" ]; then
  ln -s "$SOURCE_REGLAMENTO" "$TARGET_DIR/REGLAMENTOS_externo.yaml"
  echo "✅ Huella externa enlazada correctamente."
else
  echo "ℹ️ Huella externa ya existe. No se realizaron cambios."
fi

# 3. Nota explícita (no acción)
echo "🛑 Nota: Este enlace es SOLO para observación biológica."
echo "🛑 No se ejecuta, no se interpreta, no se propaga automáticamente."

