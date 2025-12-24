#!/usr/bin/env python3
import time
import pandas as pd
from datetime import datetime
import random
import os

CSV_FILE = "AUDITORIA_HORMIGAS_2025.csv"

def generar_latido_dinamico():
    ahora = datetime.now()
    ids = ["ALPHA", "BETA", "GAMMA"]
    
    for id_h in ids:
        # Generamos valores que fluctúen para crear una curva real
        valor_base = 24.0
        fluctuacion = random.uniform(-3.0, 5.0)
        valor_final = round(valor_base + fluctuacion, 2)
        
        nueva_fila = {
            "FECHA_HORA": ahora.strftime('%Y-%m-%d %H:%M:%S'),
            "ID_HORMIGA": id_h,
            "ESTADO": "ACTIVO",
            "DATO_VALOR": valor_final,
            "FIRMA_LBH": f"HMAC_2025_NEW_{int(time.time())}"
        }
        
        df = pd.DataFrame([nueva_fila])
        df.to_csv(CSV_FILE, mode='a', header=not os.path.exists(CSV_FILE), index=False)
    
    print(f"📡 [NUEVO VALOR] {ahora.strftime('%H:%M:%S')} -> {valor_final}°C")

if __name__ == "__main__":
    print("🚀 Iniciando secuencia de nuevos valores para el Tablero LBH...")
    for _ in range(15): # Generamos 15 ciclos para llenar el gráfico
        generar_latido_dinamico()
        os.system("python3 visualizador_directo.py")
        time.sleep(5) # Intervalo corto para ver el progreso rápido
