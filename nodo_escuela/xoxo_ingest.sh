#!/data/data/com.termux/files/usr/bin/bash
# ================================================================
# 🐜 HormigasAIS — XOXO INGEST v1.0 (Soberano Edge)
# Nodo: A16-SanMiguel-SV | Protocolo: LBH-v2.0
# Función: Ingestión externa → Sincronización XOXO-BUS M2M
# ================================================================

set -e

# ─────────────────────────────────────────
GITHUB_TOKEN="${GITHUB_TOKEN:-}"
AUDIT_KEY="PCLHQ-Q5PTRLA0091086"
# ─────────────────────────────────────────

API="https://api.hormigasais.com"
NODE_NAME="Nodo-Soberano-A16"
GITHUB_USER="Thrumanshow"
GITHUB_ORG="HormigasAIS"

# 📁 INFRAESTRUCTURA DE RESILIENCIA LOCAL (CACHE)
BASE="$HOME/hormigasais-ingest"
QUEUE="$BASE/queue"
LOGS="$BASE/logs"
FAILED="$BASE/failed"

mkdir -p "$QUEUE" "$LOGS" "$FAILED"

# ─────────────────────────────────────────
# 🧬 CRIPTOGRAFÍA LOCAL
# ─────────────────────────────────────────
generate_hash() {
    local INPUT="$1"
    echo -n "$INPUT" | sha256sum | awk '{print $1}'
}

# ─────────────────────────────────────────
# 📡 PROPAGACIÓN DE FEROMONAS (ENVIAR AL WORKER)
# ─────────────────────────────────────────
enviar_evento() {
    local ENDPOINT="$1"
    local PAYLOAD="$2"
    local USAR_KEY="$3"
    
    local TS
    TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    
    local EVENT_ID
    EVENT_ID=$(generate_hash "$ENDPOINT-$PAYLOAD-$TS" | cut -c1-16)

    echo "$PAYLOAD" > "$QUEUE/$EVENT_ID.json"

    echo ""
    echo "📡 [LBH-BUS] Propagando feromona digital..."
    echo "🆔 EVENT_ID: $EVENT_ID"
    echo "⚡ ENDPOINT: $ENDPOINT"

    local URL="$API$ENDPOINT"
    if [ "$USAR_KEY" = "true" ]; then
        URL="$API$ENDPOINT?key=$AUDIT_KEY"
    fi

    local RESPONSE
    RESPONSE=$(curl -s -X POST "$URL" \
        -H "Content-Type: application/json" \
        -d "$PAYLOAD")

    echo "$RESPONSE" > "$LOGS/$EVENT_ID.log"

    if echo "$RESPONSE" | grep -q "error"; then
        mv "$QUEUE/$EVENT_ID.json" "$FAILED/$EVENT_ID.json"
        echo "❌ [ERROR] Fallo en la red central o contrato rechazado."
        echo "📝 Detalles: $RESPONSE"
    else
        rm -f "$QUEUE/$EVENT_ID.json"
        echo "✅ [ÉXITO] Contrato asimilado y propagado al XOXO-BUS."
        echo "📝 Servidor: $RESPONSE"
    fi
}

# ─────────────────────────────────────────
# 📬 INGESTIÓN CLÁUSULA: EMAIL → EVENTO LBH
# ─────────────────────────────────────────
ingest_email() {
    local FROM="$1"
    local SUBJECT="$2"

    FROM=$(echo -n "$FROM" | sed 's/"/\\"/g')
    SUBJECT=$(echo -n "$SUBJECT" | sed 's/"/\\"/g')

    # Alineado con /xoxo/gift para registrar intenciones automáticas de regalo vía Master
    local PAYLOAD
    PAYLOAD=$(cat <<EOF
{
  "plan": "free",
  "destinatario": "$FROM",
  "email": "$FROM",
  "mensaje": "🎁 Auto-Ingest Email: $SUBJECT"
}
EOF
)
    enviar_evento "/xoxo/gift" "$PAYLOAD" "true"
}

# ─────────────────────────────────────────
# 🌐 INGESTIÓN CLÁUSULA: WEBHOOK → EVENTO LBH
# ─────────────────────────────────────────
ingest_webhook() {
    local SOURCE="$1"
    local DATA="$2"

    if ! echo "$DATA" | grep -q "^{"; then
        DATA="\"$(echo -n "$DATA" | sed 's/"/\\"/g')\""
    fi

    # Webhooks entrantes de la colonia mapeados directamente a la emisión legítima
    local PAYLOAD
    PAYLOAD=$(cat <<EOF
{
  "plan": "premium",
  "destinatario": "$SOURCE",
  "email": "",
  "mensaje": "🎁 Webhook Ingest: $DATA"
}
EOF
)
    enviar_evento "/xoxo/gift" "$PAYLOAD" "true"
}

# ─────────────────────────────────────────
# 🎁 INGESTIÓN CLÁUSULA: XOXO CLAIM (TARJETAS)
# ─────────────────────────────────────────
ingest_claim() {
    local CODE="$1"
    local OWNER="$2"
    local EMAIL="$3"

    # Redirección exacta a la estructura de canje de /xoxo/redeem
    local PAYLOAD
    PAYLOAD=$(cat <<EOF
{
  "codigo": "$CODE",
  "owner": "$OWNER",
  "email": "$EMAIL"
}
EOF
)
    enviar_evento "/xoxo/redeem" "$PAYLOAD" "false"
}

# ─────────────────────────────────────────
# 🔄 REPLAY: REINTENTO DE EVENTOS FALLIDOS
# ─────────────────────────────────────────
retry_failed() {
    echo ""
    echo "🔄 [Replay] Sincronizando transacciones diferidas..."
    echo "----------------------------------------------------------------"

    if [ ! -n "$(ls -A "$FAILED" 2>/dev/null | grep '\.json$')" ]; then
        echo "✨ Excelente: No hay eventos pendientes en FAILED."
        return
    fi

    for file in "$FAILED"/*.json; do
        [ -e "$file" ] || continue
        local FILENAME
        FILENAME=$(basename "$file")
        echo -n "📡 Retransmitiendo $FILENAME... "

        # Determina endpoint según las llaves internas para recuperar el flujo exacto
        local ENDPOINT="/xoxo/redeem"
        local URL="$API$ENDPOINT"
        if grep -q "plan" "$file"; then
            ENDPOINT="/xoxo/gift"
            URL="$API$ENDPOINT?key=$AUDIT_KEY"
        fi

        local RESPONSE
        RESPONSE=$(curl -s -X POST "$URL" \
            -H "Content-Type: application/json" \
            -d @"$file")

        if ! echo "$RESPONSE" | grep -q "error"; then
            rm -f "$file"
            echo "✅ RECUPERADO."
        else
            echo "❌ SIGUE FALLANDO."
        fi
    done
}

# ─────────────────────────────────────────
# 🧪 TEST DE PROTOCOLO DE CANJE LOCAL
# ─────────────────────────────────────────
test_event() {
    # El test emula un intento de canje estructurado idéntico al del front final del sitio
    local PAYLOAD
    PAYLOAD=$(cat <<EOF
{
  "codigo": "TEST-CODE-CLHQ",
  "owner": "$GITHUB_USER",
  "email": "clhq@hormigasais.com"
}
EOF
)
    enviar_evento "/xoxo/redeem" "$PAYLOAD" "false"
}

# ─────────────────────────────────────────
# 🐜 INTERFAZ DE COMANDOS DEL ADAPTADOR
# ─────────────────────────────────────────
case "$1" in
    email)
        if [ -z "$2" ] || [ -z "$3" ]; then
            echo "⚠️ Uso: bash xoxo_ingest.sh email [remitente] [asunto]"
            exit 1
        fi
        ingest_email "$2" "$3"
        ;;
    webhook)
        if [ -z "$2" ] || [ -z "$3" ]; then
            echo "⚠️ Uso: bash xoxo_ingest.sh webhook [origen] [datos_json_o_string]"
            exit 1
        fi
        ingest_webhook "$2" "$3"
        ;;
    claim)
        if [ -z "$2" ] || [ -z "$3" ] || [ -z "$4" ]; then
            echo "⚠️ Uso: bash xoxo_ingest.sh claim [codigo] [usuario] [email]"
            exit 1
        fi
        ingest_claim "$2" "$3" "$4"
        ;;
    retry)
        retry_failed
        ;;
    test)
        test_event
        ;;
    *)
        echo ""
        echo "🐜 ======================================================="
        echo "   HormigasAIS — XOXO INGEST INTERFACES (LBH-v2.0)"
        echo "=========================================================="
        echo "Comandos disponibles:"
        echo "  bash xoxo_ingest.sh email \"<remitente>\" \"<asunto>\""
        echo "  bash xoxo_ingest.sh webhook \"<fuente>\" \"<datos>\""
        echo "  bash xoxo_ingest.sh claim \"<codigo>\" \"<usuario>\" \"<email>\""
        echo "  bash xoxo_ingest.sh retry"
        echo "  bash xoxo_ingest.sh test"
        echo "=========================================================="
        echo ""
        ;;
esac

