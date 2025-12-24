#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

CSV_FILE = "AUDITORIA_HORMIGAS_2025.csv"

def generar_grafica():
    try:
        df = pd.read_csv(CSV_FILE)
        if df.empty:
            print("Esperando nuevos datos del enjambre...")
            return
            
        df['FECHA_HORA'] = pd.to_datetime(df['FECHA_HORA'])
        
        # Ordenamos por fecha para evitar líneas cruzadas
        df = df.sort_values('FECHA_HORA')

        plt.figure(figsize=(10, 5))
        plt.plot(df['FECHA_HORA'], df['DATO_VALOR'], color='#00ff00', marker='o', linestyle='-', linewidth=2, label='Temp Enjambre')
        plt.axhline(y=28.5, color='red', linestyle='--', label='Límite Crítico (28.5°C)')
        
        # Ajuste dinámico del eje X: solo muestra el rango de los datos presentes
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        
        plt.title(f"📊 Monitoreo de Activos LBH - {datetime.now().strftime('%d/%m/%Y')}")
        plt.ylabel("Temperatura °C")
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        plt.savefig("REPORTE_RENDIMIENTO_HORMIGAS.png")
        print("✅ Gráfica expandida y actualizada.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    generar_grafica()
