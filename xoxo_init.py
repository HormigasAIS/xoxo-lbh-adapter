import sys
import asyncio
import platform

# Detectar Termux
IS_TERMUX = 'android' in platform.system().lower()

# Intentar uvloop si no estamos en Termux
try:
    if not IS_TERMUX:
        import uvloop
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        print("✅ uvloop activado")
    else:
        print("⚡ Termux detectado: usando asyncio nativo")
except ImportError:
    print("⚡ uvloop no disponible: usando asyncio nativo")

# Crear loop de eventos seguro
try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

print(f"Loop de eventos listo: {loop}")

# Función de prueba
async def prueba_xoxo():
    print("🐜 XOXO listo y funcionando en tu entorno!")

if __name__ == "__main__":
    asyncio.run(prueba_xoxo())
