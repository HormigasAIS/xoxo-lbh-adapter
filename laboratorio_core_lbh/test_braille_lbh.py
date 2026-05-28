import sys

# 🐜 Mapeo de un Byte puro a Carácter Unicode Braille (Eje binario de 8 puntos)
def byte_a_celda_braille(byte_val):
    # El bloque Unicode Braille inicia en 0x2800 (Celda vacía)
    # Modificar el orden de los bits según la disposición estándar si es necesario
    return chr(0x2800 + byte_val)

def procesar_pulso_lbh(payload_hex):
    print("📡 [LBH-BRAILLE] Decodificando pulso en el borde...")
    try:
        # Convertir la cadena hex en bytes puros
        byte_stream = bytes.fromhex(payload_hex)
        
        print(f"🆔 Tamaño del paquete LBH: {len(byte_stream)} Bytes")
        print("⚡ Representación Táctil/Visual Braille:")
        
        # Traducir cada byte del paquete LBH a una celda Braille de 8 puntos
        celdas = [byte_a_celda_braille(b) for b in byte_stream]
        
        print("\n   " + " ".join(celdas) + "\n")
        print("📝 Volcado Binario:");
        for i, b in enumerate(byte_stream):
            print(f"   Byte [{i:02d}]: {bin(b)[2:]:>08s} -> {celdas[i]}")
            
    except Exception as e:
        print(f"❌ [ERROR] Fallo en el análisis binario: {str(e)}")

if __name__ == "__main__":
    # Simulación de un paquete LBH de prueba (Falsa feromona o token de 16 bytes)
    # Ejemplo: Origen (1 byte), Tipo (1 byte), Hash/Firma (6 bytes), Payload (8 bytes) = 16 Bytes
    test_packet = "ca71aa0c79764c0a962f766330dbe2a1" 
    
    if len(sys.argv) > 1:
        test_packet = sys.argv[1]
        
    procesar_pulso_lbh(test_packet)
