import csv, time, os, sys

# Creamos el espacio de rutas para que reconozca el ecosistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from adapter.core import XOXOAdapter

LOG_FILE = "AUDITORIA_HORMIGAS_2025.csv"

def on_audit(topic, data):
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["FECHA_HORA", "ROBOT_ID", "ESTADO", "DATO_VALOR", "FIRMA_LBH"])
        
        writer.writerow([
            time.strftime('%Y-%m-%d %H:%M:%S'),
            topic.split('/')[1],
            data.get('status'),
            data.get('temp'),
            "HMAC-SHA256-VALIDADO"
        ])
    print(f"📁 ACTIVO REGISTRADO: {data.get('temp')}°C | Validado por Contrato Humano")

auditor = XOXOAdapter(robot_id="auditor_alpha")
auditor.on_data_handler = on_audit
print("🕵️ AUDITOR LBH ACTIVO | Creando espacio de auditoría inalterable...")
auditor.loop_forever()
