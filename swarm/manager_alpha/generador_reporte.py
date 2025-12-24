import pandas as pd
import matplotlib.pyplot as plt
import os

# Forzamos a Matplotlib a no usar una ventana gráfica (modo headless)
import matplotlib
matplotlib.use('Agg')

FILE_CSV = "AUDITORIA_HORMIGAS_2025.csv"
OUTPUT_IMAGE = "REPORTE_RENDIMIENTO_HORMIGAS.png"

def generar_grafica():
    if not os.path.exists(FILE_CSV):
        print(f"❌ Error: No se encuentra {FILE_CSV}. ¿Ya corriste el auditor?")
        return

    try:
        # Leer datos
        df = pd.read_csv(FILE_CSV)
        df['FECHA_HORA'] = pd.to_datetime(df['FECHA_HORA'])

        # Crear la gráfica
        plt.figure(figsize=(10, 6))
        plt.plot(df['FECHA_HORA'], df['DATO_VALOR'], marker='o', linestyle='-', color='#00ff41', label='Temperatura Enjambre')
        
        plt.title('Reporte de Rendimiento - HormigasAIS 2025', fontsize=14)
        plt.xlabel('Tiempo de Operación', fontsize=12)
        plt.ylabel('Valor (Temp)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Guardar el activo visual
        plt.savefig(OUTPUT_IMAGE)
        print(f"✅ EXITO: Reporte generado en {OUTPUT_IMAGE}")
    except Exception as e:
        print(f"❌ Error al procesar: {e}")

if __name__ == "__main__":
    generar_grafica()
