#!/usr/bin/env python3
# test_gemini_pulse.py
# Simulación de lectura de GEMINI_HANDSHAKE.lbh y pulso de Gemini

import os

HANDSHAKE_PATH = "contracts/external/GEMINI_HANDSHAKE.lbh"

def leer_handshake(path):
    if not os.path.exists(path):
        print(f"❌ Handshake no encontrado: {path}")
        return None
    with open(path, "r") as f:
        contenido = f.read()
    return contenido

def extraer_hash(handshake_text):
    for line in handshake_text.splitlines():
        if line.startswith("HASH="):
            return line.split("=")[1].strip()
    return "NO_HASH"

def simular_pulso(hash_value):
    print("📡 [SIMULACIÓN GEMINI]")
    print(f"✅ Handshake detectado: {hash_value}")
    print(f"🔄 Pulso emitido al XOXO-BUS: {{'origin': 'Gemini_Interface', 'status': 'active', 'hash': '{hash_value}'}}")

if __name__ == "__main__":
    handshake = leer_handshake(HANDSHAKE_PATH)
    if handshake:
        hash_val = extraer_hash(handshake)
        simular_pulso(hash_val)
