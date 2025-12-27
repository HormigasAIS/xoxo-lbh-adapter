import httpx  # Necesitarás instalarlo: pip install httpx

# ... resto de tu código ...

@app.post("/webhook/lbh")
async def lbh_event(req: Request):
    payload = await req.json()
    chat_id = "8463843180"
    token = "8121528657:AAFm9YjM8l0I18G1y8109A18m"
    
    # Extraer mensaje del payload del Centinela
    msg = payload.get("payload", {}).get("message", "🐜 Movimiento Detectado")
    
    # Relevo automático a Telegram
    async with httpx.AsyncClient() as client:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        await client.post(url, json={"chat_id": chat_id, "text": msg})
        
    print(f"✅ Relevo exitoso para Arquitecto: {chat_id}")
    return {"accepted": True, "relay": "success"}

