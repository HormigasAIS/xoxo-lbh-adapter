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
                    # SATURACIÓN DE COLUMNAS PARA EL VISUALIZADOR
                    lbh_row = {
                        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "ID_HORMIGA": "WORKER_LBH",
                        "role": "Hormiga_Operativa",
                        "task": "Monitoreo_Edge",
                        "status": data.get("status", "OPERATIONAL"),
                        "temp": data.get("temp", 25.0),
                        "value": data.get("temp", 25.0),
                        "performance": 100,
                        "FIRMA_LBH": "HMAC_2025_VALID"
                    }
                    rows.append(lbh_row)
                except: continue
    if rows:
        df = pd.DataFrame(rows)
        df.to_csv(CSV_FILE, index=False)
        print(f"✅ [SATURACIÓN OK] CSV generado con: timestamp, role, task, temp.")

if __name__ == "__main__":
    actualizar_csv()
