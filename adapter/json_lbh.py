# COPYRIGHT CONSECUTIVO (C) 2024-2026 ING. CRISTHIAM LEONARDO HERNÁNDEZ QUIÑONEZ (CLHQ)
# SOBERANÍA HORMIGASAIS - VALIDACIÓN LBH PROTEGIDA
import json
import hmac
import hashlib

# 🔐 CLAVE SECRETA DEL ENJAMBRE 
# Debe ser la misma en la Worker y en el Manager
SECRET_KEY = b"hormigasais_secret_token_2025"

def json_to_lbh(data_dict: dict) -> str:
    """Convierte un diccionario a un Frame LBH firmado (Hexadecimal)"""
    json_str = json.dumps(data_dict, separators=(',', ':'))
    payload_bytes = json_str.encode()
    
    # Crear firma HMAC-SHA256
    signature = hmac.new(SECRET_KEY, payload_bytes, hashlib.sha256).hexdigest()
    
    # Unir payload y firma con un separador '|' y convertir todo a hex
    full_packet = f"{json_str}|{signature}"
    return full_packet.encode().hex()

def lbh_to_json(hex_str: str) -> dict:
    """Decodifica un Frame LBH y VALIDA la firma HMAC"""
    try:
        # 1. Convertir de hexadecimal a texto
        decoded_str = bytes.fromhex(hex_str).decode()
        
        # 2. Separar el JSON de la firma
        if "|" not in decoded_str:
            raise ValueError("Formato LBH inválido: falta separador de firma")
            
        payload_str, received_signature = decoded_str.rsplit("|", 1)
        payload_bytes = payload_str.encode()
        
        # 3. VERIFICACIÓN CRIPTOGRÁFICA
        expected_signature = hmac.new(SECRET_KEY, payload_bytes, hashlib.sha256).hexdigest()
        
        if not hmac.compare_digest(expected_signature, received_signature):
            raise PermissionError("⚠️ [ALERTA] Firma HMAC no válida. ¡Mensaje posiblemente alterado!")
            
        return json.loads(payload_str)
        
    except Exception as e:
        raise Exception(f"Fallo en decodificación LBH: {str(e)}")

