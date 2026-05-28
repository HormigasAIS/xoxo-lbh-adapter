import sys
import os
import time

def enviar_pulso_vibracion(duracion_ms):
    """Dispara un pulso físico usando la API nativa de Termux"""
    if duracion_ms > 0:
        os.system(f"termux-vibrate -d {duracion_ms}")
    # Tiempo de espera para que el hardware procese el pulso o el silencio
    time.sleep((duracion_ms + 50) / 1000.0)

def modular_byte_a_vibracion(byte_val, celda_char):
    print(f"  Procesando: {bin(byte_val)[2:]:>08s} -> {celda_char}")
    
    # Analizar los 8 bits (desde el bit más significativo al menos significativo)
    for i in range(7, -1, -1):
        bit = (byte_val >> i) & 1
        if bit == 1:
            # Bit en 1: Pulso táctil corto e intenso (50ms)
            enviar_pulso_vibracion(50)
        else:
            # Bit en 0: Micro-silencio (espacio vacío en la celda Braille)
            time.sleep(0.05)
            
    # Pequeña pausa de seguridad entre celdas Braille completas
    time.sleep(0.2)

def transmitir_paquete_lbh(payload_hex):
    print("📡 [LBH-ACTUADOR] Transmitiendo feromona al motor táctil...")
    try:
        byte_stream = bytes.fromhex(payload_hex)
        print(f"🆔 Secuencia de {len(byte_stream)} Bytes lista para transducción.")
        print("⚡ Sintiendo el pulso en el borde (Sostén el teléfono)...")
        
        for i, b in enumerate(byte_stream):
            celda = chr(0x2800 + b)
            modular_byte_a_vibracion(b, celda)
            
        print("🏁 [ÉXITO] Transmisión del paquete LBH completada.")
    except Exception as e:
        print(f"❌ [ERROR] Fuga en la transducción: {str(e)}")

if __name__ == "__main__":
    # Usamos tu identificador maestro por defecto (16 bytes puros)
    test_packet = "ca71aa0c79764c0a962f766330dbe2a1"
    
    if len(sys.argv) > 1:
        test_packet = sys.argv[1]
        
    transmitir_paquete_lbh(test_packet)
