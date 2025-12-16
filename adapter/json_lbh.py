# json_lbh.py
"""
XOXO-LBH Adapter - JSON <-> LBH Conversion
Autor: Cristhiam Quiñonez
Descripción:
Provee funciones para convertir datos entre formato JSON y LBH binario
para la comunicación segura con LBH-M2M.
"""

import json
from bridge.protocol.encoder import encode_packet
from bridge.protocol.decoder import decode_lbh_packet

def json_to_lbh(payload: dict) -> str:
    """
    Convierte un diccionario JSON a un frame LBH.
    :param payload: Diccionario con datos a enviar
    :return: Frame LBH codificado
    """
    try:
        json_str = json.dumps(payload)
        frame = encode_packet(header="00000001", type_code="00000010", payload=json_str)
        return frame
    except Exception as e:
        print("[json_lbh] Error convirtiendo JSON a LBH:", e)
        raise

def lbh_to_json(frame: str) -> dict:
    """
    Convierte un frame LBH a JSON.
    :param frame: Frame LBH recibido
    :return: Diccionario decodificado
    """
    try:
        decoded = decode_lbh_packet(frame)
        payload_str = decoded.get("payload", "{}")
        return json.loads(payload_str)
    except Exception as e:
        print("[json_lbh] Error convirtiendo LBH a JSON:", e)
        raise
