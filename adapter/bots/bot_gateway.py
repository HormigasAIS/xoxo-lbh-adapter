from fastapi import FastAPI, Request
import httpx

# --- AJUSTE DE CREDENCIALES ---
# Asegúrate de copiar el Token COMPLETO del BotFather aquí
BOT_TOKEN = "8121528657:AAFm9YjM8l0I18G1y8109A18m" 
MASTER_CHAT_ID = "8463843180"

app = FastAPI()

@app.post("/webhook/lbh")
async def lbh_event(req: Request):
    try:
        payload = await req.json()
        msg = payload.get("payload", {}).get("message", "🐜 Alerta LBH")
        
        async with httpx.AsyncClient() as client:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            # Si el token es 401, este POST fallará aquí
            resp = await client.post(url, json={
                "chat_id": MASTER_CHAT_ID, 
                "text": f"🛡️ *HormigasAIS*\n{msg}",
                "parse_mode": "Markdown"
            })
            return resp.json()
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def root(): return {"status": "online"}
