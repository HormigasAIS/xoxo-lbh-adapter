#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

try:
    df = pd.read_csv("AUDITORIA_HORMIGAS_2025.csv")
    df['FECHA_HORA'] = pd.to_datetime(df['FECHA_HORA'])
    
    # Filtramos solo datos de HOY para evitar errores de años futuros
    hoy = datetime.now().strftime('%Y-%m-%d')
    df = df[df['FECHA_HORA'].dt.strftime('%Y-%m-%d') == hoy]

    if not df.empty:
        plt.figure(figsize=(12, 6))
        # Dibujamos con marcadores claros
        plt.plot(df['FECHA_HORA'], df['DATO_VALOR'], color='#00ff00', marker='o', linewidth=1.5, label='Latido Enjambre')
        plt.axhline(y=28.5, color='red', linestyle='--', label='Límite Seguridad (28.5°C)')
        
        # ZOOM DINÁMICO: El eje X solo mostrará desde el primer hasta el último dato
        plt.xlim(df['FECHA_HORA'].min(), df['FECHA_HORA'].max())
        
        # Formato de HORAS y MINUTOS (Eliminamos los días para que se expanda)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        
        plt.title(f"📊 Auditoría en Tiempo Real - Zoom Activo ({hoy})")
        plt.xlabel("Tiempo (HH:MM:SS)")
        plt.ylabel("Temperatura °C")
        plt.grid(True, alpha=0.2)
        plt.legend()
        
        plt.savefig("REPORTE_RENDIMIENTO_HORMIGAS.png")
        print("✅ Zoom aplicado: La gráfica ahora es legible.")
except Exception as e:
    print(f"Error: {e}")
