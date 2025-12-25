#!/usr/bin/env python3
"""
Cooling Governor Ant (LBH)
Gobernanza térmica suave por feromonas
Obediente al contrato humano (STOP_H_PROT)
"""

import time
from pheromone_bus import read_pheromones

CONFIG_PATH = "./config.human"

def read_stop_flag():
    """
    Lee STOP_H_PROT desde config.human
    true  -> pausa segura
    false -> operación normal
    """
    try:
        with open(CONFIG_PATH, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("STOP_H_PROT"):
                    return line.split("=")[1].strip().lower() == "true"
    except Exception as e:
        print(f"⚠️ Error leyendo contrato humano: {e}")
    return False


print("❄️🐜 Cooling Governor Ant activa (LBH)")

def cooling_governor_loop(interval=5):
    while True:
        # --- Control contractual ---
        if read_stop_flag():
            print("🛑 STOP_H_PROT activo → Gobernador térmico en pausa segura")
            time.sleep(2)
            continue  # no actúa, no muere

        # --- Lectura de feromonas ---
        pheromones = read_pheromones()

        if pheromones:
            print(f"🌡️ Feromonas detectadas: {len(pheromones)}")
            # aquí luego puedes filtrar cooling_hint, confidence, etc.
        else:
            print("🌡️ Observando feromonas... (sin señales)")

        time.sleep(interval)

if __name__ == "__main__":
    cooling_governor_loop()
