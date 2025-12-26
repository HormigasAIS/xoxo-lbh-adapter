import sys
# Importamos la lógica del enjambre comercial
sys.path.append('./commercial_swarm')
from lbh_validator_service import process_freemium_request

print("🚀 [CLIENTE-SIM] Iniciando petición desde HormigasAIS.com...")
# Simulamos el envío de una imagen para validación
input_usuario = {"resource_id": "img_001", "type": "visual_asset"}

# El Enjambre Comercial procesa
resultado = process_freemium_request(input_usuario)

print("\n--- RESPUESTA DEL ENJAMBRE ---")
print(f"Estado: {resultado['status']}")
print(f"Firma Generada: {resultado['signature']}")
print(f"Ganancia de Eficiencia: {resultado['efficiency_gain']}")
print(f"Mensaje: {resultado['message']}")
print("------------------------------")
