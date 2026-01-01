#!/usr/bin/env bash
# ============================================
# DIAGNÓSTICO LBH – NODO-ESCUELA (UTC)
# Autor: HormigasAIS / XOXO
# Objetivo: Verificar tiempo, salud y deterioro
# ============================================

TARGET_URL="http://127.0.0.1:8081/presentation.html"
INTENTOS=20
LOG="logs/diagnostico_lbh_utc.log"

mkdir -p logs

echo "============================================" | tee -a "$LOG"
echo "⚖️  DIAGNÓSTICO LBH – NODO-ESCUELA" | tee -a "$LOG"
echo "============================================" | tee -a "$LOG"

# 1. Tiempo del sistema
echo "" | tee -a "$LOG"
echo "🕒 TIEMPO DEL SISTEMA" | tee -a "$LOG"
echo "Local : $(date)" | tee -a "$LOG"
echo "UTC   : $(date -u)" | tee -a "$LOG"

# 2. Zona horaria
echo "" | tee -a "$LOG"
echo "🌍 ZONA HORARIA CONFIGURADA" | tee -a "$LOG"
timedatectl 2>/dev/null | grep "Time zone" | tee -a "$LOG"

# 3. Estado del puerto
echo "" | tee -a "$LOG"
echo "🔌 ESTADO DEL PUERTO 8081" | tee -a "$LOG"
ss -ltnp 2>/dev/null | grep 8081 || echo "⚠️ Puerto 8081 no está escuchando" | tee -a "$LOG"

# 4. Test de deterioro / estrés
echo "" | tee -a "$LOG"
echo "🔥 TEST DE DETERIORO (curl x $INTENTOS)" | tee -a "$LOG"

for i in $(seq 1 $INTENTOS); do
  HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$TARGET_URL")
  UTC_TIME=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

  if [ "$HTTP_CODE" = "200" ]; then
    echo "[$UTC_TIME] Intento $i → ✅ OK (200)" | tee -a "$LOG"
  else
    echo "[$UTC_TIME] Intento $i → ❌ FAIL ($HTTP_CODE)" | tee -a "$LOG"
  fi

  sleep 0.2
done

# 5. Conclusión automática
echo "" | tee -a "$LOG"
echo "🧠 CONCLUSIÓN DEL SISTEMA" | tee -a "$LOG"
if grep -q "FAIL" "$LOG"; then
  echo "⚠️ Se detecta deterioro o rechazo de conexión." | tee -a "$LOG"
  echo "🔒 El Nodo está protegiéndose (comportamiento sano)." | tee -a "$LOG"
  RESULTADO_ESTRES="Protegiéndose"
else
  echo "✅ Nodo estable bajo carga." | tee -a "$LOG"
  RESULTADO_ESTRES="Estable"
fi

# --- VÍNCULO CON LA CUARTA PÁGINA (PRESENTATION.HTML) ---
JSON_OUT="../HormigasAIS-Nodo-Escuela/status_herencia.json"

cat <<JSON > "$JSON_OUT"
{
  "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "protocolo": "PTCC-Hormiga-10",
  "version_lbh": "1.0.0-Solar",
  "principio": "El código no tiene libre albedrío; es voluntad humana.",
  "resultado": "$RESULTADO_ESTRES",
  "log_preview": "Test de Deterioro finalizado con éxito."
}
JSON

echo "" | tee -a "$LOG"
echo "📁 Log generado en: $LOG"
echo "📡 JSON de Herencia actualizado en: $JSON_OUT"
echo "============================================" | tee -a "$LOG"
