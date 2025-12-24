import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib
matplotlib.use('Agg')

FILE_CSV = "AUDITORIA_HORMIGAS_2025.csv"
OUTPUT_IMAGE = "REPORTE_RENDIMIENTO_HORMIGAS.png"
ALERTA_FILE = "ALERTA_CRITICA.md"
UMBRAL_MAX = 32.0

def generar_grafica():
    if not os.path.exists(FILE_CSV): return

    try:
        # Cargamos el CSV y forzamos a que la columna de valor sea numérica
        df = pd.read_csv(FILE_CSV)
        df['DATO_VALOR'] = pd.to_numeric(df['DATO_VALOR'], errors='coerce')
        df['FECHA_HORA'] = pd.to_datetime(df['FECHA_HORA'])
        
        # Eliminamos filas que no tengan números válidos
        df = df.dropna(subset=['DATO_VALOR'])

        max_temp = df['DATO_VALOR'].max()
        
        if max_temp > UMBRAL_MAX:
            with open(ALERTA_FILE, "w") as f:
                f.write(f"# ⚠️ ALERTA CRÍTICA DETECTADA\n")
                f.write(f"**Temperatura Máxima:** {max_temp}°C\n")
                f.write(f"**Fecha:** {df.iloc[-1]['FECHA_HORA']}\n")
            print(f"🔥 ¡ALERTA! {max_temp}°C detectada.")
        else:
            if os.path.exists(ALERTA_FILE): os.remove(ALERTA_FILE)

        plt.figure(figsize=(10, 6))
        plt.plot(df['FECHA_HORA'], df['DATO_VALOR'], marker='o', color='#00ff41', label='Temp Enjambre')
        plt.axhline(y=UMBRAL_MAX, color='red', linestyle='--', label='Límite Seguridad')
        plt.title('Reporte de Rendimiento e Incidentes')
        plt.legend()
        plt.savefig(OUTPUT_IMAGE)
        print(f"✅ Reporte actualizado sin errores de formato.")
    except Exception as e:
        print(f"❌ Error crítico: {e}")

if __name__ == "__main__":
    generar_grafica()
