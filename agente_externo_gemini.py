# agente_externo_gemini.py
import os

HANDSHAKE_PATH = "contracts/external/GEMINI_HANDSHAKE.lbh"

class AgenteExternoGemini:
    def __init__(self, fundacion_id="Cristhiam_LBH_2025"):
        self.soberania = fundacion_id
        self.permiso_ejecucion = False
        self.handshake_hash = None

    def cargar_contrato(self):
        if not os.path.exists(HANDSHAKE_PATH):
            return False
        with open(HANDSHAKE_PATH, "r") as f:
            for line in f:
                if line.startswith("HASH="):
                    self.handshake_hash = line.split("=")[1].strip()
        return True

    def validar_entorno(self, log_recibido):
        if "Centinela validando contrato LBH" in log_recibido:
            return "SYNC_ACTIVE"
        if "GUARDIA_NOCTURNA" in log_recibido:
            return "GUARDIA_NOCTURNA"
        return "OBSERVATION_ONLY"

    def emitir_instruccion_logica(self, estado):
        if estado == "GUARDIA_NOCTURNA":
            return self.generar_payload_lbh()
        return None

    def generar_payload_lbh(self):
        return {
            "type": "LBH_PAYLOAD_SUGGESTION",
            "origin": "Gemini_Interface",
            "hash": self.handshake_hash,
            "instruction": "LOG_VAL_CENTINELA: Guard Mode Stable",
            "execution": "HUMAN_ONLY"
        }

# Ejemplo de prueba
if __name__ == "__main__":
    gemini = AgenteExternoGemini()
    gemini.cargar_contrato()
    estado = gemini.validar_entorno("Centinela validando contrato LBH — GUARDIA_NOCTURNA")
    payload = gemini.emitir_instruccion_logica(estado)
    print(payload)
