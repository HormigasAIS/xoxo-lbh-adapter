#!/bin/bash
# ------------------------------------------------------------------
# Script de Rotación Interactiva y Sanitización Local (HormigasAIS)
# ------------------------------------------------------------------

clear
echo "======================================================"
echo " 🐜 ROTACIÓN INTERACTIVA DE SECRETOS - HormigasAIS "
echo "======================================================"
echo ""

# 1. Captura interactiva de Tokens
read -sp "🔑 Ingresa el TOKEN ANTERIOR (a revocar): " TOKEN_OLD
echo ""
read -sp "✨ Ingresa el NUEVO TOKEN (para configurar): " TOKEN_NEW
echo ""
echo "------------------------------------------------------"

# 2. Captura interactiva de HMAC / API Keys
read -sp "🔐 Ingresa la CLAVE HMAC/API ANTERIOR: " HMAC_OLD
echo ""
read -sp "✨ Ingresa la NUEVA CLAVE HMAC/API: " HMAC_NEW
echo ""
echo "------------------------------------------------------"

# 3. Limpieza de credenciales en el remoto Git (Gitea)
echo "🔄 Sanitizando URL del remoto local 'origin'..."
git remote set-url origin "http://127.0.0.1:3001/HormigasAIS-Colonia-Soberana/xoxo-lbh-adapter.git"
echo "✅ Remoto origin actualizado (credenciales eliminadas de la URL)."

echo ""
echo "======================================================"
echo " RESUMEN Y VARIABLES CONFIGURADAS:"
echo "======================================================"
echo "1. Revoca inmediatamente en la plataforma el TOKEN ANTERIOR."
echo "2. Revoca la CLAVE HMAC/API ANTERIOR en tus nodos."
echo ""
echo "Variables capturadas para tu sesión actual:"
export LBH_BOT_TOKEN="$TOKEN_NEW"
export LBH_HMAC_SECRET="$HMAC_NEW"
echo " - LBH_BOT_TOKEN configurado correctamente [OK]"
echo " - LBH_HMAC_SECRET configurado correctamente [OK]"
echo "======================================================"
