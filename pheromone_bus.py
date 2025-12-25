# pheromone_bus.py

import time

STOP_H_PROT = False  # leído desde config.human (en siguiente paso)

def is_stop_active():
    return STOP_H_PROT

def emit_pheromone(pheromone):
    if is_stop_active():
        print("🛑 LBH FREEZE: emisión bloqueada por contrato humano")
        return False

    # Emisión normal
    print(f"🌸 Feromona aceptada: {pheromone['type']}")
    return True

def listen_pheromones():
    while True:
        if is_stop_active():
            print("🧊 Enjambre congelado (STOP_H_PROT activo)")
            time.sleep(5)
            continue

        # Escucha normal
        time.sleep(2)
