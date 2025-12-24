#!/usr/bin/env python3
import pandas as pd
import ast
import time
import os

LOG_FILE = "auditor.log"
CSV_FILE = "AUDITORIA_HORMIGAS_2025.csv"

def actualizar_csv():
    rows = []
    if not os.path.exists(LOG_FILE):
        print(f"Archivo de log no encontrado: {LOG_FILE}")
        return

    with open(LOG_FILE, "r") as f:
        for line in f:
            if "Datos del Enjambre:" in line:
                data_str = line.split("Datos del Enjambre:")[1].strip()
                try:
                    data = ast.literal_eval(data_str)
                    rows.append(data)
                except Exception as e:
                    print(f"Error al parsear línea: {line}\n{e}")

    if rows:
        df = pd.DataFrame(rows)
        df.to_csv(CSV_FILE, index=False)
        print(f"CSV actualizado: {CSV_FILE} | Registros: {len(df)}")
    else:
        print("No se encontraron datos nuevos para actualizar.")

if __name__ == "__main__":
    # Ejecutar continuamente cada 10 segundos
    while True:
        actualizar_csv()
        time.sleep(10)
