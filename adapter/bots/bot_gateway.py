from fastapi import FastAPI, Request
import httpx

app = FastAPI(
    title="HormigasAIS Bot Gateway",
    version="1.0",
    description="Gateway de integración para bots LBH"
)

@app.get("/")
async def root():
    return {"status": "HormigasAIS Bot Gateway ONLINE"}

@app.post("/webhook/lbh")
async def lbh_event(req: Request):
    try:
        payload = await req.json()
        print("🐜 LBH EVENT RECEIVED:", payload)
        
        # Configuración de Telegram
        chat_id = "8463843180"
        token = "8121528657:AAFm9YjM8l0I18G1y8109A18m"
        msg = payload.get("payload", {}).get("message", "🐜 Movimiento detectado por HormigasAIS")
        
        # Relevo a Telegram
        async with httpx.AsyncClient() as client:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            await client.post(url, json={"chat_id": chat_id, "text": msg})
            
        return {"accepted": True, "relay": "success"}
    except Exception as e:
        print(f"❌ Error en Gateway: {e}")
        return {"accepted": False, "error": str(e)}

@app.post("/webhook/telegram")
async def telegram_webhook(req: Request):
    payload = await req.json()
    return {"ok": True}
