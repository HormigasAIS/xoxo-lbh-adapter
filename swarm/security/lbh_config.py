# Este es el secreto compartido del enjambre
import os as _os
SECRET_KEY = _os.environ.get("LBH_SWARM_SECRET", "")
TOPIC_SWARM = "hormigasais/swarm/telemetry"

def get_auth():
    return {
        "key": SECRET_KEY,
        "topic": TOPIC_SWARM
    }

