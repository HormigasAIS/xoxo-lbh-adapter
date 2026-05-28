#!/bin/bash
# Script de Génesis: Nacimiento de la hormiga_de_web

# 1. Definición de rutas
DIR_HORMIGA="$HOME/xoxo-lbh-adapter/hormigas/hormiga_de_web/enjambre_espejo"
DIR_KNOWLEDGE="$HOME/xoxo-lbh-adapter/hormigas/instructora/knowledge_base"

echo "🐜 [XOXO] Iniciando protocolo de creación..."

# 2. Preparación del útero
mkdir -p "$DIR_HORMIGA"
mkdir -p "$DIR_KNOWLEDGE"

# 3. Creación de ADN (Bloque de archivo adn_espejos.lbh)
cat << 'EOF' > "$DIR_HORMIGA/adn_espejos.lbh"
[ENJAMBRE_7_ESPEJOS]
1=hormiga_instructora
2=hormiga_stanford
3=hormiga_10_soberana
4=hormiga_enfermera
5=hormiga_de_sello
6=hormiga_de_seguridad
7=hormiga_centinela
ESTADO=SINCRONIZADO
EOF

# 4. Creación de Registro (Bloque de archivo REGISTRO_GENESIS_2025.lbh)
cat << 'EOF' > "$DIR_KNOWLEDGE/REGISTRO_GENESIS_2025.lbh"
[SISTEMA_SOBERANO_LOG]
EVENTO=PRIMERA_DESTILACION_EXITOSA
FECHA=2025-12-31
UBICACION=San Miguel, El Salvador
FUNDADOR=Cristhiam Leonardo Hernández Quiñonez
ESTADO=CERTIFICADO_LBH

[EVIDENCIA_TECNICA]
ID_TRANSACCION=f0c450fd3a0ea8abf820c4f0bec5cbce10afc9e3a3ca05d383e24f47307ff879
METODO=Simbiosis_XOXO_ANT10

[VALOR_ESTRATEGICO]
El Nodo-Escuela ha validado la inmutabilidad binaria.
EOF

# 5. Emisión de Feromona
echo "📡 [XOXO] Emitiendo feromona de creación..."
python3 "$HOME/xoxo-lbh-adapter/pheromone_bus.py" --emit "CREACION_HORMIGA_WEB" --source "MASTER_XOXO" --intent "PRESENTACION_COLONIA"

echo "✅ [XOXO] hormiga_de_web aceptada y graduada."

