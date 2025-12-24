#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

try:
    df = pd.read_csv("AUDITORIA_HORMIGAS_2025.csv")
    df['FECHA_HORA'] = pd.to_datetime(df['FECHA_HORA'])
    
    # Solo tomamos datos de hoy para eliminar el error del 2026
    hoy = datetime.now().strftime('%Y-%m-%d')
    df = df[df['FECHA_HORA'].dt.strftime('%Y-%m-%d') == hoy]

    if not df.empty:
        plt.figure(figsize=(10, 6))
        plt.plot(df['FECHA_HORA'], df['DATO_VALOR'], 'g-o', markersize=4, label='Temp Real')
        plt.axhline(y=28.5, color='r', linestyle='--', label='Límite Crítico')
        
        # Ajuste de escala: Esto elimina la compresión
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        plt.xlim(df['FECHA_HORA'].min(), df['FECHA_HORA'].max()) 
        
        plt.title(f"Auditoría LBH - Zoom Activo: {hoy}")
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.savefig("REPORTE_RENDIMIENTO_HORMIGAS.png")
        print("✅ Gráfica expandida y saneada.")
except Exception as e:
    print(f"Error: {e}")
