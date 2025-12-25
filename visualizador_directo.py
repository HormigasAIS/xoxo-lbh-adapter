#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

try:
    df = pd.read_csv("AUDITORIA_HORMIGAS_2025.csv")
    # Convertimos a datetime y aseguramos que no haya errores de zona horaria
    df['FECHA_HORA'] = pd.to_datetime(df['FECHA_HORA'])
    
    # Filtramos solo los datos generados en la última hora para máximo detalle
    ahora = datetime.now()
    df = df[df['FECHA_HORA'] > (ahora - pd.Timedelta(hours=1))]

    if not df.empty:
        # Ordenamos por tiempo para que la línea no salte aleatoriamente
        df = df.sort_values('FECHA_HORA')
        
        plt.figure(figsize=(12, 6))
        # Usamos un estilo de línea más grueso y puntos claros
        plt.plot(df['FECHA_HORA'], df['DATO_VALOR'], color='#00ff00', marker='o', 
                 linestyle='-', linewidth=2, markersize=5, label='Latido Enjambre (LBH)')
        
        # EL TRUCO: Ajustamos el eje X estrictamente al rango de datos actuales
        plt.xlim(df['FECHA_HORA'].min(), df['FECHA_HORA'].max())
        
        # Formato de eje X: Solo Minutos y Segundos
        ax = plt.gca()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        
        # Rotamos las etiquetas para que no se encimen
        plt.xticks(rotation=45)
        
        plt.title(f"📊 Auditoría LBH - Zoom de Precisión ({ahora.strftime('%Y-%m-%d')})")
        plt.xlabel("Tiempo Real (HH:MM:SS)")
        plt.ylabel("Temperatura °C")
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.legend()
        
        plt.tight_layout() # Evita que se corten las etiquetas
        plt.savefig("REPORTE_RENDIMIENTO_HORMIGAS.png")
        print("✅ Configuración ajustada: Zoom de precisión activado.")
except Exception as e:
    print(f"Error: {e}")
