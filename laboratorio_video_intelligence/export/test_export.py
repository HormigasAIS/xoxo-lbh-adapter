#!/usr/bin/env python3

import json
import time
from datetime import datetime

payload = {
    "status": "LABORATORIO_ACTIVO",
    "motor": "LBH_VIDEO_ANALYZER",
    "timestamp": datetime.now().isoformat(),
    "ts": int(time.time()),
    "nodo": "A16"
}

with open(
    "hormigasais-site/laboratorio_video_intelligence/json/status.json",
    "w"
) as f:
    json.dump(payload, f, indent=2)

print("✅ Exportación completada")
