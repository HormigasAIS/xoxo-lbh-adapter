#!/usr/bin/env python3
import os, pandas as pd, matplotlib.pyplot as plt, matplotlib.dates as mdates
from datetime import datetime

plt.style.use('dark_background')

try:
    # Ruta al repo (ajustada a la variable HOME de Termux)
    ruta_repo = os.path.expanduser("~/xoxo-lbh-adapter/HormigasAIS-AirCity")
    carpeta_salida = os.path.join(ruta_repo, "docs/reportes")
    os.makedirs(carpeta_salida, exist_ok=True)
    ruta_salida = os.path.join(carpeta_salida, "LATEST_MONITOR.png")

    df = pd.read_csv("AUDITORIA_HORMIGAS_2025.csv")
    df['FECHA_HORA'] = pd.to_datetime(df['FECHA_HORA'])
    ahora = datetime.now()
    df = df[df['FECHA_HORA'] > (ahora - pd.Timedelta(hours=1))]

    if not df.empty:
        df = df.sort_values('FECHA_HORA')
        fig, ax = plt.subplots(figsize=(12, 6))
        fig.patch.set_facecolor('#000000')
        ax.set_facecolor('#000000')
        plt.plot(df['FECHA_HORA'], df['DATO_VALOR'], color='#00ff00', marker='o', linestyle='-', linewidth=2)
        plt.title(f"Auditoria LBH - Monitor de Misión ({ahora.strftime('%Y-%m-%d')})", color='#00ff00')
        
        # Firma de autor
        plt.figtext(0.99, 0.01, 'Soberanía LBH - HormigasAIS / CLHQ', color='#00ff00', alpha=0.6, ha='right', va='bottom')
        
        plt.tight_layout()
        plt.savefig(ruta_salida, facecolor=fig.get_facecolor())
        plt.close()

        # Sincronización automática con Gitea
        os.system(f"cd {ruta_repo} && git add docs/reportes/LATEST_MONITOR.png")
        os.system(f"cd {ruta_repo} && git commit -m '🤖 [AUTO] Actualización de monitor: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}'")
        os.system(f"cd {ruta_repo} && git push origin main")

        print(f"📊 Gráfico enviado a Gitea: {ruta_salida}")
    else:
        print("⚠️ No hay datos para graficar.")
except Exception as e:
    print(f"❌ Error en el flujo: {e}")
