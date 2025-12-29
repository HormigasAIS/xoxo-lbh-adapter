# -*- coding: utf-8 -*-
# 🐜 Hormiga 07 - Centinela de Integridad Web
# REPO: El-Hormiguero-Live
# DELEGACIÓN: Cristhiam Leonardo Hernández Quiñonez

import os

class Ant07Sentinel:
    def __init__(self):
        self.fundador = "Cristhiam Leonardo Hernández Quiñonez"
        self.contrato = "contracts/config/lbh.human"
        self.archivos_criticos = ["index.html", "style.css", "imagenesLBH.js"]

    def validar_autoridad(self):
        if os.path.exists(self.contrato):
            with open(self.contrato, 'r') as f:
                if self.fundador in f.read():
                    return True
        return False

    def vigilar_web(self):
        if not self.validar_autoridad():
            print("🚨 [ERROR] Hormiga 07 sin contrato. Abortando.")
            return

        print(f"🔍 [Ant_07] Vigilando integridad de El-Hormiguero-Live...")
        for archivo in self.archivos_criticos:
            if os.path.exists(archivo):
                print(f"✅ {archivo}: Protegido.")
            else:
                print(f"⚠️ {archivo}: NO DETECTADO.")
        
        print("🟢 [STATUS] Nodo Live sincronizado bajo Nivel 3.")

if __name__ == "__main__":
    Ant07Sentinel().vigilar_web()
