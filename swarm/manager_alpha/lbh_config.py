# Configuración de Seguridad Unificada para el Enjambre
SECRET_KEY = "HormigasAIS_2025_Secure"
TOPIC_SWARM = "hormigasais/swarm/telemetry"

def get_auth():
    return {
        "key": SECRET_KEY,
        "topic": TOPIC_SWARM
    }

