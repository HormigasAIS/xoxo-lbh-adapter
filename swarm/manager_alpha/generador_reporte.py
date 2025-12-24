import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib
matplotlib.use('Agg')

FILE_CSV = "AUDITORIA_HORMIGAS_2025.csv"
OUTPUT_IMAGE = "REPORTE_RENDIMIENTO_HORMIGAS.png"
ALERTA_FILE = "ALERTA_CRITICA.md"
UMBRAL_MAX = 32.0  # Si la temperatura supera esto, se activa la alarma

def generar_grafica():
    if not os.path.exists(FILE_CSV): return

    try:
        df = pd.read_csv(FILE_CSV)
        df['FECHA_HORA'] = pd.to_datetime(df['FECHA_HORA'])
        
        # --- LÓGICA DE ALERTA ---
        max_temp = df['DATO_VALOR'].max()
        if max_temp > UMBRAL_MAX:
            with open(ALERTA_FILE, "w") as f:
                f.write(f"# ⚠️ ALERTA CRÍTICA DETECTADA\n")
                f.write(f"El enjambre ha superado el umbral de seguridad.\n\n")
                f.write(f"**Temperatura Máxima Detectada:** {max_temp}°C\n")
                f.write(f"**Fecha del Suceso:** {df.iloc[-1]['FECHA_HORA']}\n")
            print(f"🔥 ¡ALERTA! Temperatura de {max_temp}°C detectada.")
        else:
            if os.path.exists(ALERTA_FILE):
                os.remove(ALERTA_FILE) # Limpiar alerta si ya todo está normal
                print("✅ Sistema operando en rangos normales.")

        # --- DIBUJAR GRÁFICA ---
        plt.figure(figsize=(10, 6))
        plt.plot(df['FECHA_HORA'], df['DATO_VALOR'], marker='o', color='#00ff41')
        plt.axhline(y=UMBRAL_MAX, color='red', linestyle='--', label='Límite de Seguridad')
        plt.title('Reporte de Rendimiento e Incidentes')
        plt.legend()
        plt.savefig(OUTPUT_IMAGE)
        print(f"✅ Reporte actualizado.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generar_grafica()
