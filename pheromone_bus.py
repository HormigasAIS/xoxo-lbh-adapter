import time

def is_stop_active():
    try:
        with open("config.human", "r") as f:
            contenido = f.read().lower()
            return "stop_h_prot = true" in contenido
    except FileNotFoundError:
        return False

def emit_pheromone(type_name):
    if is_stop_active():
        print("🛑 LBH FREEZE: Emisión bloqueada por Contrato Humano.")
        return False
    print(f"🌸 Feromona '{type_name}' aceptada.")
    return True

if __name__ == "__main__":
    # Prueba de vida del bus
    print("📡 Bus de Feromonas LBH Iniciado...")
    emit_pheromone("Sistema_Soberano")
