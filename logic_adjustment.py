# Bloque de Validación HormigasAIS - Nodo San Miguel
# © 2025-2026 HormigasAIS - Proyectado por Cristhiam Leonardo Hernández Quiñonez (CLHQ)
# Propiedad Intelectual Protegida bajo el Protocolo de Soberanía LBH
if etype == "REAL_TIME_MOTION":
    if conf >= 0.85 and (time.time() - last_notify) > 30:
        last_notify = time.time()
        # Emisión de feromona hacia Telegram/XOXO-BUS
        return True, f"🌙 GUARDIA_ACTIVA ({int(conf*100)}%): Movimiento detectado en Sector Sur."
