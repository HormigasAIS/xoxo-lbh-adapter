#!/bin/bash
# © 2025-2026 HormigasAIS - Proyectado por Cristhiam Leonardo Hernández Quiñonez (CLHQ)
# Propiedad Intelectual Protegida bajo el Protocolo de Soberanía LBH
echo "🐜 Iniciando Entorno HormigasAIS..."
# Activar entorno
source venv_xoxo/bin/activate
# Entrar a la carpeta
cd ~/HormigasAIS-video-intelligence-checker/xoxo-lbh-adapter
echo "✅ Entorno Activo y Directorio Configurado"
echo "🤖 Para ejecutar el test usa: python test_adapter.py"
# Abrir una shell interactiva para que no se cierre
exec bash

