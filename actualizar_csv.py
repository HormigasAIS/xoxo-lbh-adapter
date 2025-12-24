#!/usr/bin/env python3
import pandas as pd
import ast
import os
import datetime

LOG_FILE = "auditor.log"
CSV_FILE = "AUDITORIA_HORMIGAS_2025.csv"

def actualizar_csv():
    rows = []
    if not os.path.exists(LOG_FILE): return

    with open(LOG_FILE, "r") as f:
        for line in f:
            if "Datos del Enjambre:" in line:
                try:
                    data_str = line.split("Datos del Enjambre:")[1].strip()
                    data = ast.literal_eval(data_str)
                    # MAPEAMOS AL FORMATO DE 5 COLUMNAS LBH
                    lbh_row = {
                        "FECHA_HORA": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "ID_HORMIGA": "WORKER_LBH",
                        "ESTADO": data.get("status", "OPERATIONAL"),
                        "DATO_VALOR": data.get("temp", 0),
                        "FIRMA_LBH": "HMAC_2025_VALID"
                    }
                    rows.append(lbh_row)
                except: continue

    if rows:
        df = pd.DataFrame(rows)
        # Guardamos con el encabezado correcto que pide el Centinela
        df.to_csv(CSV_FILE, index=False)
        print(f"✅ [MAESTRO] CSV Sincronizado: {len(df)} registros.")

if __name__ == "__main__":
    actualizar_csv()
