from fastapi import FastAPI, Request
import httpx
import time
from datetime import datetime

BOT_TOKEN = "8539663975:AAHOujZ97fKHeOk2Y79DcjfBuKDUcfjGihA"
MASTER_CHAT_ID = "8463843180"

app = FastAPI()
last_notify = 0

def lbh_decision_engine(payload):
    global last_notify
    etype = payload.get("type", "UNKNOWN")
    conf = payload.get("confidence", 0.0)
    msg = payload.get("message", "Evento LBH")
    
    current_hour = datetime.now().hour
    # Umbral de madrugada (2:44 AM) para evitar falsos positivos
    umbral = 0.90 if (0 <= current_hour <= 5) else 0.85
    
    if etype == "REAL_TIME_MOTION":
        if conf >= umbral and (time.time() - last_notify) > 30:
            last_notify = time.time()
            return True, f"🌙 Guardia Nocturna ({int(conf*100)}%): {msg}"
        return False, f"Filtrado (Conf: {conf}/{umbral})"
        
    return False, "Evento sin prioridad"

@app.post("/webhook/lbh")
async def lbh_event(req: Request):
    try:
        data = await req.json()
        should_send, final_msg = lbh_decision_engine(data)
        
        if should_send:
            async with httpx.AsyncClient() as client:
                await client.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", 
                    json={"chat_id": MASTER_CHAT_ID, "text": f"🛡️ *HormigasAIS*\n{final_msg}", "parse_mode": "Markdown"})
            status_code = "sent"
        else:
            status_code = "filtered"

        # DEVOLVER LA FIRMA QUE EL CENTINELA REQUIERE
        return {
            "status": status_code,
            "node_signature": "LBH-SM-MASTER-2025", 
            "reason": final_msg
        }
    except Exception as e:
        return {"status": "error", "node_signature": "ERROR", "detail": str(e)}

@app.get("/")
async def root(): return {"status": "Sovereign Gateway Active"}
