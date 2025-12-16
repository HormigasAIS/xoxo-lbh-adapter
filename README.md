# XOXO-LBH Adapter

![License](https://img.shields.io/badge/License-BSL%201.1%20(HormigasAIS)-blue?style=flat-square&logo=github)

Autor: Cristhiam Quiñonez — HormigasAIS  
Licencia: BSL 1.1 Adaptada  
Objetivo: Integración de XOXO con LBH-M2M para robots, IoT y comunicación distribuida.

---

## 🔹 Descripción

`XOXO-LBH Adapter` es un paquete Python que permite a **XOXO** integrarse directamente con **LBH-M2M**, habilitando:

- Comunicación **Machine-to-Machine (M2M)** segura y ligera.  
- Conversión entre **JSON ↔ LBH binario** para intercambio de datos con robots y sensores.  
- Soporte para el ecosistema HormigasAIS, incluyendo **Freemium/Premium** y herramientas B2B.

Este adapter funciona como **puente inteligente** entre la capa de automatización XOXO y el protocolo LBH-M2M, permitiendo:

- Publicación de comandos a actuadores.  
- Lectura de datos de sensores en tiempo real.  
- Validación de integridad mediante **HMAC**.  
- Preparación para integraciones **JSON-LBH** para clientes B2B.

---

## 🔹 Instalación

### Requisitos

- Python 3.8+  
- pip  
- Broker MQTT (ej. Mosquitto)

### Pasos

```bash
# Clonar el repositorio
git clone https://github.com/Thrumanshow/xoxo-lbh-adapter.git
cd xoxo-lbh-adapter

# Instalar en modo editable
pip install -e .


---

🔹 Uso Básico

Inicializar Adapter

from adapter import XOXOAdapter

adapter = XOXOAdapter(broker="localhost", robot_id="robot_test")

Enviar comandos a actuadores

test_payload = {"motor_id": 1, "position": 90, "speed": 120}
adapter.publish_act(**test_payload)

Leer sensores y convertir a JSON

from adapter import lbh_to_json

def on_data(topic, data):
    json_data = lbh_to_json(data)
    print("[Dashboard] Datos decodificados:", json_data)

adapter.set_handler(on_data)
adapter.loop_start()


---

🔹 Estructura del Proyecto

xoxo-lbh-adapter/
 ├── adapter/
 │     ├── __init__.py
 │     ├── core.py
 │     ├── freemium.py
 │     ├── json_lbh.py
 │     └── security.py
 ├── examples/
 │     ├── send_command.py
 │     ├── read_sensor.py
 │     └── dashboard_listener.py
 ├── tests/
 │     ├── test_core.py
 │     ├── test_json_lbh.py
 ├── requirements.txt
 ├── pyproject.toml
 ├── test_adapter.py
 └── README.md


---

🔹 Objetivo Cumplido

Protocolo Binario LBH-M2M: Encoder y decoder robustos.

Capa de Seguridad HMAC: Integridad y autenticidad de datos M2M.

Integración JSON-LBH: Herramienta lista para clientes B2B.

Soporte Robótica & IoT: Comandos y lectura de sensores vía MQTT.

Preparación para Freemium/Premium: Compatible con botones interactivos LBH.


---

🔹 Roadmap Futuro

Extensión LBH-SPEC v2.0 completo.

Integración con ROS2 para robótica modular.

Validación avanzada y autogeneración de paquetes LBH desde JSON.

Expansión del soporte Freemium/Premium y mercado B2B.


---

🔹 Licencia

Este proyecto está bajo la licencia MIT.
"Inteligencia colaborativa para un futuro automatizado y humano"
 ├── requirements.txt
 ├── pyproject.toml
 ├── test_adapter.py
 └── README.md


---

🔹 Objetivo Cumplido

1. Protocolo Binario LBH-M2M: Encoder y decoder robustos.


2. Capa de Seguridad HMAC: Integridad y autenticidad de datos M2M.


3. Integración JSON-LBH: Herramienta lista para clientes B2B.


4. Soporte Robótica & IoT: Comandos y lectura de sensores via MQTT.


5. Preparación para Freemium/Premium: Compatible con botones interactivos LBH.


---

🔹 Roadmap Futuro

Extensión LBH-SPEC v2.0 completo.

Integración con ROS2 para robótica modular.

Validación avanzada y autogeneración de paquetes LBH desde JSON.

Expansión del soporte Freemium/Premium y mercado B2B.


---

🔹 Licencia

Este proyecto está bajo la Business Source License 1.1 (BSL 1.1) Adaptada para HormigasAIS.
"Inteligencia colaborativa para un futuro automatizado y centrado en el ser humano"
