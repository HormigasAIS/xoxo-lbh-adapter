# 🐜 BITÁCORA DE COMANDOS: PROYECTO HORMIGASAIS 🤖
**Misión:** Construcción del Adaptador XOXO-LBH Seguro
**Ingeniero en Jefe:** Cristhiam Quiñonez

---

## 🛠 FASE 1: EL ENTORNO DE OPERACIONES (Termux)
Antes de lanzar cohetes, preparamos la base de lanzamiento.

* **`cd ~/HormigasAIS-video-intelligence-checker/xoxo-lbh-adapter`**
  * *Traducción:* "¡Llevame al cuartel general!" – Entras a la carpeta donde vive todo tu código.
* **`source venv_xoxo/bin/activate`**
  * *Traducción:* "¡Traje de combate puesto!" – Activa tu Entorno Virtual para usar las librerías aisladas.
* **`pip list`**
  * *Traducción:* "Inventario de armas." – Revisa librerías instaladas (paho-mqtt, fastapi, etc.).
* **`chmod +x lanzar.sh`**
  * *Traducción:* "Permiso para despegar." – Da permisos de ejecución al script de inicio rápido.
* **`./lanzar.sh`**
  * *Traducción:* "Botón de encendido." – Ejecuta el script que automatiza la entrada al proyecto y al venv.

---

## 🔐 FASE 2: EL ESCUDO DE SEGURIDAD (HMAC & LBH)
Aquí es donde pusimos "llave" a los mensajes para que nadie hackee tus hormigas.

* **HMAC (Hash-based Message Authentication Code):**
  * El "sello de cera" digital. Si alguien cambia un bit del mensaje, el sello se rompe y el robot ignora la orden.
* **LBH (Lenguaje-Binario-HormigasAIS):**
  * Idioma nativo hexadecimal. Convierte JSON pesado en paquetes ligeros y veloces para el hardware.
* **`python test_adapter.py`**
  * *Traducción:* "¡Simulación de vuelo!" – Ejecuta la prueba de integridad del core.py y el protocolo.

---

## 📡 FASE 3: LA TORRE DE CONTROL (Broker MQTT)
Hicimos que los mensajes no solo se impriman, sino que viajen por el aire.

* **`pkg install mosquitto mosquitto-clients`**
  * *Traducción:* "Instalando la antena." – Instala el servidor (Broker) que reparte los mensajes.
* **`mosquitto -v`**
  * *Traducción:* "Torre de control encendida." – Inicia el servidor en modo detallado para ver cada conexión.
* **`mosquitto_sub -h localhost -t "hormigasais/robot_test/commands" -v`**
  * *Traducción:* "El espía." – Escucha un canal específico para verificar los frames LBH enviados.
* **`mosquitto_pub -h localhost -t "hormigasais/robot_test/reports" -m "DATA|FIRMA"`**
  * *Traducción:* "Simulador de Robot." – Envía un mensaje desde la terminal hacia el adaptador para probar la recepción.

---

## 📂 FASE 4: ANATOMÍA DEL CÓDIGO (Los Archivos)

* **`json_lbh.py`**: El **Traductor**. Convierte JSON a Binario, genera firmas HMAC y ahora también las VALIDA al recibir.
* **`core.py`**: El **Corazón**. Maneja la conexión MQTT, suscripción a reportes y lógica de publicación.
* **`__init__.py`**: El **Conserje**. Organiza las importaciones para que el sistema reconozca el paquete `adapter`.
* **`lanzar.sh`**: El **Piloto Automático**. Script Bash que configura todo el entorno con un solo comando.

---

## 💡 NOTAS DE SEGURIDAD FINAL:
> "Un frame LBH sin firma es un robot a la deriva. Un frame LBH con HMAC es una hormiga con armadura."
> **Estado Actual:** Comunicación Full-Duplex (Doble vía) con validación de identidad activa.

[2026-01-18 01:13:38] SOBERANÍA M2M VALIDADA: Sello CLHQ operativo en v1.2.1
