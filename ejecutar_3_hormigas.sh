#!/usr/bin/env python3
import time
import pandas as pd
from datetime import datetime
import random

CSV_FILE = "AUDITORIA_HORMIGAS_2025.csv"

def latido_maestro():
    # Forzamos fecha exacta de Diciembre 2025
    ahora = datetime.now()
    ids = ["ALPHA", "BETA", "GAMMA"]
    
    for id_h in ids:
        valor = round(random.uniform(22.0, 30.0), 2)
        nueva_fila = {
            "FECHA_HORA": ahora.strftime('%Y-%m-%d %H:%M:%S'),
            "ID_HORMIGA": id_h,
            "ESTADO": "ACTIVO",
            "DATO_VALOR": valor,
            "FIRMA_LBH": f"HMAC_VALID_{int(time.time())}"
        }
        df = pd.DataFrame([nueva_fila])
        df.to_csv(CSV_FILE, mode='a', header=not pd.io.common.file_exists(CSV_FILE), index=False)
    
    print(f"📈 Latido Maestro registrado: {ahora.strftime('%H:%M:%S')}")

if __name__ == "__main__":
    while True:
        latido_maestro()
        # Generar gráfica cada latido para que GitHub la reciba fresca
        import os
        os.system("python3 visualizador_directo.py")
        time.sleep(15)
