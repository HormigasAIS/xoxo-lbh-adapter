import sys

def calcular_byte_braille(puntos_str):
    """Toma una cadena de números (ej. '123') y la transforma en 1 Byte puro"""
    byte_resultado = 0
    
    # Mapeo de puntos estándar de 8 bits
    mapeo_bits = {
        '1': 0,  # Bit 0 (2^0 = 1)
        '2': 1,  # Bit 1 (2^1 = 2)
        '3': 2,  # Bit 2 (2^2 = 4)
        '4': 3,  # Bit 3 (2^3 = 8)
        '5': 4,  # Bit 4 (2^4 = 16)
        '6': 5,  # Bit 5 (2^5 = 32)
        '7': 6,  # Bit 6 (2^6 = 64)
        '8': 7   # Bit 7 (2^7 = 128)
    }
    
    # Encender el bit correspondiente para cada punto presionado
    for punto in puntos_str:
        if punto in mapeo_bits:
            byte_resultado |= (1 << mapeo_bits[punto])
            
    return byte_resultado

def iniciar_teclado_laboratorio():
    print("⌨️  [LBH-INPUT] Teclado de Simulación Braille Activo.")
    print("Instrucciones: Escribe los puntos combinados (ej: '123' o '145') y dale Enter.")
    print("Escribe 'exit' para cerrar la matriz.\n")
    
    paquete_acumulado = []
    
    while True:
        try:
            entrada = input("🐜 Puntos activos > ").strip()
            if entrada.lower() == 'exit':
                break
                
            if not entrada:
                continue
                
            # Validar que solo contenga números del 1 al 8
            if not all(c in '12345678' for c in entrada):
                print("❌ [ERROR] Entrada inválida. Usa solo números del 1 al 8 (puntos Braille).")
                continue
            
            # Generar el byte
            byte_generado = calcular_byte_braille(entrada)
            celda_char = chr(0x2800 + byte_generado)
            hex_val = f"{byte_generado:02x}"
            
            paquete_acumulado.append(hex_val)
            
            print(f"   ↳ Celda: {celda_char} | Binario: {bin(byte_generado)[2:]:>08s} | HEX: 0x{hex_val}")
            print(f"   📦 Cadena LBH Actual: {''.join(paquete_acumulado)}\n")
            
        except KeyboardInterrupt:
            break
            
    print("\n🏁 [LABORATORIO] Ensayo finalizado.")
    print(f"🔮 Carga útil LBH generada: {''.join(paquete_acumulado)}")

if __name__ == "__main__":
    iniciar_teclado_laboratorio()
