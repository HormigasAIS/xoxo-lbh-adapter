#!/usr/bin/env bash

# =========================================================
# 🐜 XOXO-LBH-ADAPTER → HormigasAIS Sovereign Bridge
# =========================================================

echo "🐜 Inicializando XOXO Bridge..."

# ─────────────────────────────────────────
# Rutas soberanas
# ─────────────────────────────────────────

CORE_BASE="$HOME/hormigasais-core"

WORKER="$CORE_BASE/video_checker/lbh_video_analyzer.py"

CORTEX="$CORE_BASE/hormiga_de_web.py"

SITE_BASE="$HOME/hormigasais-site"

OUTPUT_DIR="$SITE_BASE/lbh_output"

LOG_DIR="$SITE_BASE/lbh_logs"

MEMORY_DIR="$HOME/xoxo-lbh-adapter/memoria_biologica"

mkdir -p "$OUTPUT_DIR"
mkdir -p "$LOG_DIR"
mkdir -p "$MEMORY_DIR"

# ─────────────────────────────────────────
# Dataset biológico soberano
# ─────────────────────────────────────────

AI_DATASET="$MEMORY_DIR/videos_ai.txt"

HUMAN_DATASET="$MEMORY_DIR/videos_humanos.txt"

# =========================================================
# 🧠 MEMORIA AI
# =========================================================

cat > "$AI_DATASET" << 'DATAAI'
https://vt.tiktok.com/ZSxX534YP/
https://www.facebook.com/share/r/1J5ujpkusv/
https://www.instagram.com/reel/DYajsjJxne1/?igsh=MWpuMnRpOHo3MWptbg==
https://youtube.com/shorts/E4sxmoEYhqg?si=pui_bpesRcBmzGQa
DATAAI

# =========================================================
# 🧠 MEMORIA HUMANA
# =========================================================

cat > "$HUMAN_DATASET" << 'DATAHUMAN'
https://vt.tiktok.com/ZSxXmPfYy/
https://www.facebook.com/share/r/18imRhsPqf/
https://www.instagram.com/reel/DYajsjJxne1/?igsh=MWpuMnRpOHo3MWptbg==
https://youtube.com/live/6yfGF2IBUfI?si=eJjtO4w3VaoAS8PG
DATAHUMAN

# ─────────────────────────────────────────
# Validaciones soberanas
# ─────────────────────────────────────────

if [ ! -f "$WORKER" ]; then
    echo "❌ Worker no encontrado:"
    echo "$WORKER"
    exit 1
fi

# ─────────────────────────────────────────
# URL recibida
# ─────────────────────────────────────────

URL="${1:-https://youtube.com/test}"

TS=$(date +%s)

OUTPUT_JSON="$OUTPUT_DIR/evento_${TS}.json"

LOG_FILE="$LOG_DIR/xoxo_bridge.log"

# ─────────────────────────────────────────
# Clasificación memoria biológica
# ─────────────────────────────────────────

CLASIFICACION="DESCONOCIDO"

if grep -Fxq "$URL" "$AI_DATASET"; then
    CLASIFICACION="AI_DETECTADO"
fi

if grep -Fxq "$URL" "$HUMAN_DATASET"; then
    CLASIFICACION="HUMANO_CONFIRMADO"
fi

# ─────────────────────────────────────────
# Cortex independiente
# Espacio amarillo soberano
# ─────────────────────────────────────────

CORTEX_STATUS="NO_ACTIVO"

if [ -f "$CORTEX" ]; then
    CORTEX_STATUS="ACTIVO"
fi

# ─────────────────────────────────────────
# Ejecutar worker soberano
# ─────────────────────────────────────────

echo "🧪 Ejecutando worker biológico..."

JSON_RESULT=$(
LBH_CLASS="$CLASIFICACION" \
python3 "$WORKER" "$URL"
)

# ─────────────────────────────────────────
# Persistencia soberana
# ─────────────────────────────────────────

cat > "$OUTPUT_JSON" << JSONEOF
{
  "bridge_node": "XOXO-LBH-ADAPTER",

  "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",

  "clasificacion_memoria": "$CLASIFICACION",

  "cortex_hormiga_web": {
    "estado": "$CORTEX_STATUS",
    "ruta": "$CORTEX"
  },

  "worker_core": {
    "estado": "ACTIVO",
    "ruta": "$WORKER"
  },

  "site_delivery": {
    "estado": "ACTIVO",
    "ruta": "$OUTPUT_DIR"
  },

  "url": "$URL",

  "worker_stdout": $JSON_RESULT
}
JSONEOF

# ─────────────────────────────────────────
# Log soberano
# ─────────────────────────────────────────

echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] $CLASIFICACION -> $URL" >> "$LOG_FILE"

# ─────────────────────────────────────────
# Estado final
# ─────────────────────────────────────────

echo ""
echo "✅ Evento procesado."
echo "🧠 Memoria biológica: $CLASIFICACION"
echo "🟡 Cortex: $CORTEX_STATUS"
echo "📦 JSON:"
echo "$OUTPUT_JSON"
echo ""

cat "$OUTPUT_JSON"

