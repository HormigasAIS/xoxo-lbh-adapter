#!/usr/bin/env python3
"""
Pheromone Bus (LBH)
Canal suave de comunicación entre hormigas del enjambre HormigasAIS.

Las feromonas no ordenan.
Sugieren, orientan y respetan el contrato humano.
"""

import time

CONFIG_FILE = "config.human"


def is_stop_active():
    """
    Lee el contrato humano y detecta si el enjambre está en pausa segura.
    """
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            contenido = f.read().lower()
            return "stop_h_prot = true" in contenido
    except FileNotFoundError:
        # Si no hay contrato, el bus no asume autoridad
        return False


def emit_pheromone(type_name, source="unknown", intent="soft_signal"):
    """
    Emite una feromona simbólica al enjambre.
    No ejecuta acciones, solo deja rastro.
    """

    if is_stop_active():
        print("🛑🌫️ LBH FREEZE: Emisión de feromonas pausada por contrato humano")
        return False

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

    pheromone = {
        "type": type_name,
        "source": source,
        "intent": intent,
        "timestamp": timestamp,
        "lbh_compliant": True
    }

    # En esta fase, el bus es sensorial (no persistente)
    print(f"🌸 Feromona '{pheromone['type']}' emitida por {pheromone['source']}")

    return True


def emit_stop_pheromone(reason="human_decision"):
    """
    Feromona crítica: indica pausa segura del enjambre.
    """
    print(f"🛑🧪 Feromona STOP percibida — motivo: {reason}")
    return True


# ==========================
# 🌱 Prueba de vida del bus
# ==========================
if __name__ == "__main__":
    print("📡 Bus de Feromonas LBH iniciado")
    emit_pheromone(
        type_name="Sistema_Soberano",
        source="pheromone_bus",
        intent="handshake"
    )
