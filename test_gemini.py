from agente_externo_gemini import AgenteExternoGemini

if __name__ == "__main__":
    gemini = AgenteExternoGemini()
    
    # Forzar estado de prueba
    estado = "GUARDIA_NOCTURNA"
    
    payload = gemini.emitir_instruccion_logica(estado)
    print(payload)
