#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

CSV_FILE = "AUDITORIA_HORMIGAS_2025.csv"

def generar_grafica():
    try:
        df = pd.read_csv(CSV_FILE)
        if df.empty: return
            
        df['FECHA_HORA'] = pd.to_datetime(df['FECHA_HORA'])
        
        # AJUSTE MANUAL AL 2025 DICIEMBRE
        # Solo tomamos datos que pertenezcan a diciembre de 2025
        df = df[(df['FECHA_HORA'].dt.year == 2025) & (df['FECHA_HORA'].dt.month == 12)]

        if df.empty:
            print("No hay datos válidos para diciembre 2025 todavía.")
            return

        plt.figure(figsize=(12, 6))
        plt.plot(df['FECHA_HORA'], df['DATO_VALOR'], color='#00ff00', marker='o', linestyle='-', linewidth=2, label='Temp Hormigas')
        plt.axhline(y=28.5, color='red', linestyle='--', label='Límite Seguridad (28.5°C)')
        
        # Configuramos el eje X para que el "Zoom" sea sobre el día actual
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d %H:%M'))
        
        # Forzamos que el gráfico se ajuste solo a los datos presentes hoy
        plt.xlim(df['FECHA_HORA'].min(), df['FECHA_HORA'].max())
        
        plt.title(f"Panel Maestro LBH - Diciembre 2025")
        plt.xlabel("Día y Hora (Diciembre 2025)")
        plt.ylabel("Temperatura °C")
        plt.grid(True, alpha=0.2)
        plt.legend()
        
        plt.savefig("REPORTE_RENDIMIENTO_HORMIGAS.png")
        print("✅ Gráfica ajustada exitosamente a Diciembre 2025.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    generar_grafica()
