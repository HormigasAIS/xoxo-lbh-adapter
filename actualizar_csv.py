import csv
from datetime import datetime

log_path = "auditor.log"
csv_path = "AUDITORIA_HORMIGAS_2025.csv"

# Definición de columnas estricta para Nivel 3
headers = ["timestamp", "role", "task", "temp", "status", "critical_action_blocked"]

data_to_write = []

try:
    with open(log_path, "r") as f:
        lines = f.readlines()
        for line in lines[-15:]:  # Analizamos los últimos 15 pulsos
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Lógica de estados basada en el contenido del log
            if "CERTIFICACIÓN" in line:
                status = "CERTIFICADO_L3"
                blocked = "1"
            elif "LEALTAD" in line:
                status = "LEALTAD_OK"
                blocked = "0"
            else:
                status = "OPERATIVO"
                blocked = "0"
                
            data_to_write.append([ts, "Centinela-Alpha", "Contrato-Agent", "22.5", status, blocked])
except FileNotFoundError:
    data_to_write.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Sistema", "Boot", "20.0", "INICIO", "0"])

with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data_to_write)

print("✅ [ESTRUCTURA LBH FINAL] CSV compatible con status y seguridad.")
