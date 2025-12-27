#!/usr/bin/env bash
[ -f .env ] && export $(grep -v '^#' .env | xargs)
URL="${HORMIGAS_NODE_URL}/v1/event"

echo "🧠 Generando reporte de inteligencia de video..."
echo "📡 Enviando a: $URL"

curl -s -X POST "$URL" \
     -H "Content-Type: application/json" \
     -d '{
           "agent_id": "video-checker-sm-01",
           "event_type": "MOTION_DETECTED",
           "payload": {
             "confidence": 0.98,
             "zone": "Sector San Miguel",
             "objects": ["human"]
           }
         }'
echo -e "\n\n✅ Reporte enviado."
