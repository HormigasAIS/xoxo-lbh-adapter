#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

try:
    df = pd.read_csv("AUDITORIA_HORMIGAS_2025.csv")
    df['FECHA_HORA'] = pd.to_datetime(df['FECHA_HORA'])
    
    ahora = datetime.now()
    df = df[df['FECHA_HORA'] > (ahora - pd.Timedelta(hours=1))]

    if not df.empty:
        df = df.sort_values('FECHA_HORA')
        
        plt.figure(figsize=(12, 6))
        # Color verde neón para resaltar en el fondo oscuro de GitHub
        plt.plot(df['FECHA_HORA'], df['DATO_VALOR'], color='#00ff00', marker='o', 
                 linestyle='-', linewidth=2, markersize=5, label='Latido Enjambre (LBH)')
        
        plt.xlim(df['FECHA_HORA'].min(), df['FECHA_HORA'].max())
        
        ax = plt.gca()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        
        plt.xticks(rotation=45)
        plt.title(f"📊 Auditoría LBH - Zoom de Precisión ({ahora.strftime('%Y-%m-%d')})")
        plt.xlabel("Tiempo Real (HH:MM:SS)")
        plt.ylabel("Temperatura °C")
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.legend()
        
        plt.tight_layout()
        plt.savefig("REPORTE_RENDIMIENTO_HORMIGAS.png")
        print("✅ Configuración ajustada: Zoom de precisión activado.")
except Exception as e:
    print(f"Error: {e}")
