# -*- coding: utf-8 -*-
# 🐜 Hormiga Recolectora - Protocolo LBH-XOXO
# Recolecta reportes de la Hormiga 07 y genera visualización

import json
import os
import matplotlib.pyplot as plt
from datetime import datetime

class CollectorAnt:
    def __init__(self):
        self.source = "../El-Hormiguero-Live/telemetria_hormiga_07.json"
        self.output_graph = "../El-Hormiguero-Live/img/telemetria_live.png"
        self.founder = "Cristhiam Leonardo Hernández Quiñonez"

    def procesar_y_graficar(self):
        if not os.path.exists(self.source):
            print("🚨 [Collector] No se encontró feromona de Hormiga 07.")
            return

        with open(self.source, 'r') as f:
            data = json.load(f)

        if data["signature"] == self.founder:
            print(f"✅ [Collector] Firma validada: {self.founder}")
            self.generar_grafico(data)
        else:
            print("🛑 [CRITICAL] Firma no válida. Comunicación abortada.")

    def generar_grafico(self, data):
        # Simulación de pulso de trabajo para el gráfico
        plt.figure(figsize=(8, 4))
        plt.plot([1, 2, 3, 4], [23, 25, 24, 26], color='red', marker='o')
        plt.title(f"Telemetría Hormiga 07 - {datetime.now().strftime('%Y-%m-%d')}")
        plt.xlabel("Eje Temporal (Sincronizado LBH)")
        plt.ylabel("Nivel de Actividad")
        plt.grid(True)
        
        # Guardar directamente en el repo Live
        plt.savefig(self.output_graph)
        plt.close()
        print(f"📊 [Collector] Gráfico actualizado en: {self.output_graph}")

if __name__ == "__main__":
    CollectorAnt().procesar_y_graficar()
