import time
from pheromone_bus import emit_pheromone

def cooling_governor_loop():
    print("❄️🐜 Gobernador Solar activo (LBH - Protegiendo Hardware)")
    while True:
        emit_pheromone("cooling_status", 1.0)
        time.sleep(20)

if __name__ == "__main__":
    try:
        cooling_governor_loop()
    except KeyboardInterrupt:
        pass
