from fastapi import FastAPI, Request
import httpx
import time

BOT_TOKEN = "8539663975:AAHOujZ97fKHeOk2Y79DcjfBuKDUcfjGihA"
MASTER_CHAT_ID = "8463843180"

app = FastAPI()
last_notify = 0

def lbh_decision_engine(payload):
    global last_notify
    etype = payload.get("type", "UNKNOWN")
    conf = payload.get("confidence", 0.0)
    state = payload.get("swarm_state", "STABLE")
    msg = payload.get("message", "Evento LBH")
    
    # REGLA 1: Emergencias siempre pasan
    if state == "CRITICAL" or etype == "SYSTEM_FAILURE":
        return True, f"🚨 CRÍTICO: {msg}"
    
    # REGLA 2: Movimiento solo si es real (>0.85) y no repetitivo (>30s)
    if etype == "REAL_TIME_MOTION":
        if conf > 0.85 and (time.time() - last_notify) > 30:
            last_notify = time.time()
            return True, f"🐜 Movimiento Real ({int(conf*100)}%): {msg}"
        return False, "Ruido o repetitivo"
        
    return False, "Sin importancia"

@app.post("/webhook/lbh")
async def lbh_event(req: Request):
    data = await req.json()
    should_send, final_msg = lbh_decision_engine(data)
    
    if should_send:
        async with httpx.AsyncClient() as client:
            await client.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", 
                json={"chat_id": MASTER_CHAT_ID, "text": f"🛡️ *HormigasAIS*\n{final_msg}", "parse_mode": "Markdown"})
        return {"status": "sent"}
    return {"status": "filtered", "reason": final_msg}

@app.get("/")
async def root(): return {"status": "Brain Online"}
