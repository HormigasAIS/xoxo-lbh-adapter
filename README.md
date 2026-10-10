# 🐜 HormigasAIS - XOXO-LBH Adapter (v1.2.1)
### Ingeniería de Protocolos Inteligentes | Soberanía Digital

Este repositorio constituye la pieza clave de integración entre el bus de datos **XOXO** y el protocolo **LBH (Lenguaje Binario HormigasAIS)**. Diseñado para entornos de **Edge Computing, Robótica (ROS2) e IoT Industrial**, garantiza que la comunicación máquina-a-máquina (M2M) sea resiliente, eficiente y, sobre todo, soberana.

---

## 👨‍💻 Autoría y Gobernanza
* **Titular de Propiedad Intelectual:** Ingeniero Cristhiam Leonardo Hernández Quiñonez (**CLHQ**).
* **Cargo:** Ingeniero de Protocolos HormigasAIS.
* **Copyright:** Consecutivo © 2024-2026 (Protección Inalienable).
* **Origen:** San Miguel, El Salvador.

---

## 🛡️ Capas de Seguridad Integrada
El adaptador no solo transporta datos; los protege mediante un ecosistema de defensa activa:

1. **Firma HMAC-2025:** Cada frame LBH es validado mediante firmas criptográficas para asegurar que el mensaje no ha sido alterado por agentes externos ("Mosquitos").
2. **Validación Centinela:** Auditoría constante de integridad de archivos críticos (`security.py`, `json_lbh.py`).
3. **Soberanía LBH:** Traducción de JSON a binario compacto para optimizar la energía y el ancho de banda en nodos remotos.

---

## ⚖️ Licencia y Uso
Este software se distribuye bajo la **HormigasAIS Source-Available License v1.0** (licencia propietaria; texto completo en [LICENSE](LICENSE)).
* **Permitido sin autorización adicional:** leer, estudiar y auditar el código; hacer un fork privado solo para revisión personal.
* **Requiere autorización de CLHQ:** uso en producción, redistribución, obras derivadas para distribución o uso público, y cualquier uso comercial.
* **Autoría:** conserva el aviso de autoría **CLHQ** en cualquier copia autorizada.

---

> "La colonia no reside en la plataforma, reside en el protocolo."
> — *Ing. Cristhiam Leonardo Hernández Quiñonez*

---
*Visualizando la resiliencia desde el borde del mundo.*
