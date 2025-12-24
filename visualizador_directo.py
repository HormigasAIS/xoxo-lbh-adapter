#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

try:
    df = pd.read_csv("AUDITORIA_HORMIGAS_2025.csv")
    df['FECHA_HORA'] = pd.to_datetime(df['FECHA_HORA'])
    
    # Filtro estricto para hoy (Diciembre 2025)
    hoy = datetime.now().strftime('%Y-%m-%d')
    df = df[df['FECHA_HORA'].dt.strftime('%Y-%m-%d') == hoy]

    if not df.empty:
        plt.figure(figsize=(12, 6))
        # Solo dibujamos los datos de las hormigas
        plt.plot(df['FECHA_HORA'], df['DATO_VALOR'], color='#00ff00', marker='o', linewidth=1.5, label='Latido Enjambre')
        
        # ZOOM DINÁMICO
        plt.xlim(df['FECHA_HORA'].min(), df['FECHA_HORA'].max())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        
        plt.title(f"📊 Auditoría LBH Saneada - {hoy}")
        plt.xlabel("Tiempo (HH:MM:SS)")
        plt.ylabel("Temperatura °C")
        plt.grid(True, alpha=0.15)
        plt.legend()
        
        plt.savefig("REPORTE_RENDIMIENTO_HORMIGAS.png")
        print("✅ Gráfica actualizada: Línea roja eliminada.")
except Exception as e:
    print(f"Error: {e}")
