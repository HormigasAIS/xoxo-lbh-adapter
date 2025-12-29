import pandas as pd
import matplotlib.pyplot as plt
import os

CSV_FILE = "AUDITORIA_HORMIGAS_2025.csv"

def generar_grafico():
    if not os.path.exists(CSV_FILE):
        print("❌ Error: No se encuentra el archivo de auditoría.")
        return

    # Cargar datos con la nueva estructura LBH
    df = pd.read_csv(CSV_FILE)
    
    # Convertir FECHA_HORA a objeto datetime para un eje X fluido
    df['FECHA_HORA'] = pd.to_datetime(df['FECHA_HORA'])
    df = df.sort_values('FECHA_HORA')

    plt.figure(figsize=(10, 6))
    
    # Graficar DATO_VALOR (Temperatura/Rendimiento)
    plt.plot(df['FECHA_HORA'], df['DATO_VALOR'], marker='o', linestyle='-', color='#b22222', label='Pulso del Enjambre')
    
    plt.title('HormigasAIS: Telemetría de Resiliencia (LBH-L3)', fontsize=14)
    plt.xlabel('Eje Temporal (Sincronizado)', fontsize=10)
    plt.ylabel('Valor de Operación (Temp/Load)', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Guardar para el Dashboard de GitHub Pages
    plt.savefig('rendimiento.png')
    print("📈 [SISTEMA] Gráfico de rendimiento actualizado con éxito.")

if __name__ == "__main__":
    generar_grafico()
