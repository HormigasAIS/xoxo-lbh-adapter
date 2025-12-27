from fastapi import FastAPI, Request
import httpx
import logging

# Configuración Soberana
BOT_TOKEN = "8121528657:AAFm9YjM8l0I18G1y8109A18m"
MASTER_CHAT_ID = "8463843180"
BOT_NAME = "@Hormigas_SM_bot"

app = FastAPI(
    title="HormigasAIS Gateway",
    version="1.1",
    description=f"Gateway para {BOT_NAME} - Nodo San Miguel"
)

@app.get("/")
async def root():
    return {"status": "HormigasAIS Bot Gateway ONLINE", "bot": BOT_NAME}

@app.post("/webhook/lbh")
async def lbh_event(req: Request):
    try:
        payload = await req.json()
        # Extraer el mensaje del evento LBH
        msg_content = payload.get("payload", {}).get("message", "🐜 Alerta de Movimiento Detectada")
        
        # Formatear mensaje para Telegram con sello de HormigasAIS
        formatted_msg = f"🐜 *HormigasAIS Alert*\n\n{msg_content}\n\n📍 Nodo: San Miguel\n🛡️ Estatus: Soberano"

        async with httpx.AsyncClient() as client:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            response = await client.post(url, json={
                "chat_id": MASTER_CHAT_ID,
                "text": formatted_msg,
                "parse_mode": "Markdown"
            })
            
            if response.status_code == 200:
                return {"status": "success", "relay": "Telegram", "sent_to": MASTER_CHAT_ID}
            else:
                return {"status": "error", "detail": response.text}

    except Exception as e:
        return {"status": "critical_error", "detail": str(e)}

@app.post("/webhook/telegram")
async def telegram_webhook(req: Request):
    return {"status": "active"}
