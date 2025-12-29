# test_gemini_full.py
from agente_externo_gemini import AgenteExternoGemini

def main():
    # Inicializamos el agente Géminis
    gemini = AgenteExternoGemini()

    # Estados que queremos probar
    estados = ["IDLE", "SYNC_ACTIVE", "GUARDIA_NOCTURNA", "OBSERVATION_ONLY"]

    for estado in estados:
        print(f"\n📡 Probando estado: {estado}")
        payload = gemini.emitir_instruccion_logica(estado)
        if payload:
            print("✅ Payload generado:")
            print(payload)
        else:
            print("ℹ️ No se generó payload. Solo observación.")

if __name__ == "__main__":
    main()
