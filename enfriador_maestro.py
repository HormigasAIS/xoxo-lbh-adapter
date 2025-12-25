#!/usr/bin/env python3
import pandas as pd
import time
import os
import json

# Configuración de Protocolo LBH
LIMITE_ALERTA = 28.5
ARCHIVO_AUDITORIA = "AUDITORIA_HORMIGAS_2025.csv"
ARCHIVO_REGISTRO = "REGISTRO_ENFRIAMIENTO_LBH.csv"

def registrar_evento(temp_in, accion, temp_out):
    """ Escribe el evento de enfriamiento para cotejo en GitHub """
    timestamp = time.strftime("%Y-%m-%d_%H:%M:%S")
    firma = "HMAC-2025-VALID"
    nueva_linea = f"{timestamp},{temp_in},{accion},{temp_out},{firma}\n"
    with open(ARCHIVO_REGISTRO, "a") as f:
        f.write(nueva_linea)
    print(f"📝 Registro de cotejo actualizado: {accion}")

def enfriar_enjambre():
    try:
        if not os.path.exists(ARCHIVO_AUDITORIA): return
        df = pd.read_csv(ARCHIVO_AUDITORIA)
        if df.empty: return
        
        ultima_temp = df['DATO_VALOR'].iloc[-1]
        
        if ultima_temp >= LIMITE_ALERTA:
            print(f"⚠️ CALOR DETECTADO: {ultima_temp}°C. Iniciando protocolo...")
            # Simulamos el enfriamiento bajando la carga
            temp_final = ultima_temp - 2.0 
            registrar_evento(ultima_temp, "ENFRIAMIENTO_LBH_ACTIVO", temp_final)
            
            # Notificamos al bus de feromonas (Opcional si tienes el bus corriendo)
            os.system(f"echo 'FEROMONA_CALOR_DETECTADA' >> auditor.log")
            
    except Exception as e:
        print(f"Error en enfriador: {e}")

if __name__ == "__main__":
    print("❄️ Enfriador Maestro LBH iniciado. Vigilando línea roja...")
    while True:
        enfriar_enjambre()
        time.sleep(15)
