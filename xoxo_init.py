import asyncio
# © 2025-2026 HormigasAIS - Proyectado por Cristhiam Leonardo Hernández Quiñonez (CLHQ)
# Propiedad Intelectual Protegida bajo el Protocolo de Soberanía LBH
import platform

def main():
    # Detectar Termux
    IS_TERMUX = 'android' in platform.system().lower()

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

    asyncio.run(prueba_xoxo())


# Permite ejecutar con python xoxo_init.py directamente
if __name__ == "__main__":
    main()
