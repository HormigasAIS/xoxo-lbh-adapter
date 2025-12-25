#!/usr/bin/env python3
"""
Cooling Governor Ant (LBH)
Gobernanza térmica suave por feromonas
"""

import time
from pheromone_bus import read_pheromones

print("🐜 Cooling Governor Ant creada y lista (LBH)")

def cooling_governor_loop(interval=5):
    while True:
        pheromones = read_pheromones()

        if pheromones:
            print(f"🌡️ Feromonas detectadas: {len(pheromones)}")
        else:
            print("🌡️ Observando feromonas... (modo pasivo)")

        time.sleep(interval)

if __name__ == "__main__":
    cooling_governor_loop()
