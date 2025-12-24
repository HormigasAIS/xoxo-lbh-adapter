# Este es el secreto compartido del enjambre
SECRET_KEY = "HormigasAIS_2025_Secure"
TOPIC_SWARM = "hormigasais/swarm/telemetry"

def get_auth():
    return {
        "key": SECRET_KEY,
        "topic": TOPIC_SWARM
    }

