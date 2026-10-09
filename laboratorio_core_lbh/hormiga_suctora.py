import json, sys

def emitir_feromona():
    for linea in sys.stdin:
        try:
            data = json.loads(linea)
            # Succión de contexto: detecta ganchos peligrosos
            peligro = any(k in data.get('gancho_psicologico', '') for k in ['masiva', 'robo', 'clon'])
            feromona = {
                "tipo": "SUCTORA_CONTEXT",
                "peligrosidad": "ALTA" if peligro else "BAJA",
                "saturacion": data.get('origen', 'unknown') == 'api_publica'
            }
            print(json.dumps(feromona))
            sys.stdout.flush()
        except:
            pass

if __name__ == '__main__':
    emitir_feromona()
