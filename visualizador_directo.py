import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('AUDITORIA_HORMIGAS_2025.csv')
    plt.figure(figsize=(10,6))
    plt.plot(df['DATO_VALOR'], marker='o', color='green', label='Temp Enjambre (2025)')
    plt.axhline(y=32.0, color='red', linestyle='--', label='Límite Riesgo')
    plt.title('Reporte de Rendimiento - HormigasAIS 2025')
    plt.xlabel('Lecturas Recientes')
    plt.ylabel('Valor (Temp)')
    plt.legend()
    plt.grid(True)
    plt.savefig('REPORTE_RENDIMIENTO_HORMIGAS.png')
    print("✅ Gráfica generada directamente desde el ADN del CSV.")
except Exception as e:
    print(f"❌ Error: {e}")
