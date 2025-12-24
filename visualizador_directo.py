#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

CSV_FILE = "AUDITORIA_HORMIGAS_2025.csv"

def generar_grafica():
    try:
        df = pd.read_csv(CSV_FILE)
        df['FECHA_HORA'] = pd.to_datetime(df['FECHA_HORA'])
        
        # Filtramos solo las últimas 2 horas para que la gráfica respire
        ahora = datetime.now()
        hace_2_horas = ahora - timedelta(hours=2)
        df = df[df['FECHA_HORA'] > hace_2_horas]

        plt.figure(figsize=(10, 6))
        plt.plot(df['FECHA_HORA'], df['DATO_VALOR'], 'g-o', label='Temp Enjambre (LBH)')
        plt.axhline(y=28.5, color='r', linestyle='--', label='Límite Seguridad (28.5°C)')
        
        # Formateo del eje X para ver minutos y segundos
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        plt.gcf().autofmt_xdate()
        
        plt.title(f"Reporte de Rendimiento en Tiempo Real - {ahora.strftime('%Y-%m-%d')}")
        plt.xlabel("Hora del Sistema (CST)")
        plt.ylabel("Temperatura °C")
        plt.legend()
        plt.grid(True)
        
        plt.savefig("REPORTE_RENDIMIENTO_HORMIGAS.png")
        print("✅ Gráfica corregida y sincronizada temporalmente.")
    except Exception as e:
        print(f"Error al generar gráfica: {e}")

if __name__ == "__main__":
    generar_grafica()
