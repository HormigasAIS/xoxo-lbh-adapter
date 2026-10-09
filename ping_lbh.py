import time
import socket

def medir_latencia(target_ip, port=9001):
    start = time.time()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((target_ip, port))
        end = time.time()
        print(f"✅ Latencia: {(end - start) * 1000:.2f} ms")
        sock.close()
    except Exception as e:
        print(f"❌ Error de conexión: {e}")

# Cambia 127.0.0.1 si el adapter está en otro dispositivo Android
medir_latencia("127.0.0.1", 3000)
