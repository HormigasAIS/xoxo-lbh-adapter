#!/usr/bin/env bash

# Cargar variables si existen
[ -f .env ] && source .env
URL=${HORMIGAS_NODE_URL:-"http://127.0.0.1:40945"}

echo "🔍 Verificando conexión con el Nodo Soberano en $URL..."

RESPONSE=$(curl -s -X GET "$URL/v1/health")

if echo "$RESPONSE" | grep -q "OPERATIONAL"; then
    echo "✅ CONEXIÓN EXITOSA"
    echo "📊 Datos del Nodo: $RESPONSE"
else
    echo "❌ ERROR: No se pudo contactar al Nodo o la respuesta es inválida."
    exit 1
fi
