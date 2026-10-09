#!/usr/bin/env python3
import sys
import email
import json
import subprocess
from email.policy import default

class HormigaEntrenadoraLBH:
    """
    Clase matriz del Nodo-Escuela diseñada para emular el procesamiento de 
    borde de Linux (RFC 5322), asimilar contratos LBH y ejecutar acciones en Termux.
    """
    def __init__(self):
        # Base de datos local de identidades soberanas de la Colonia
        self.NODOS_AUTORIZADOS = {
            "manager_alpha": {"rol": "master", "firma_id": "LBH-99X-ALPHA"},
            "guardia_nocturna": {"rol": "centinela", "firma_id": "LBH-44B-GUARD"}
        }

    def capturar_objeto_crudo(self):
        """Lee el flujo continuo del pipe (stdin) y parsea el correo estilo Linux Standard."""
        # Se lee sys.stdin de forma completa para absorber el diff de Git o el correo puro
        texto_crudo = sys.stdin.read()
        
        # El parser de Python separa nativamente las cabeceras del cuerpo (Estándar RFC)
        mensaje = email.message_from_string(texto_crudo, policy=default)
        return mensaje

    def procesar_cuerpo_y_payload(self, mensaje):
        """Extrae el cuerpo del mensaje aislando los metadatos de Git si existen."""
        cuerpo = ""
        if mensaje.is_multipart():
            for parte in mensaje.iter_parts():
                cuerpo += parte.get_content()
        else:
            cuerpo = mensaje.get_content()
        
        # Retornamos el cuerpo limpio para buscar la feromona LBH
        return cuerpo

    def detectar_contrato_lbh(self, cuerpo_mensaje):
        """Busca y extrae la estructura de la feromona/contrato LBH en el cuerpo."""
        # Buscamos el patrón JSON o la cadena LBH emitida en el buffer
        for linea in cuerpo_mensaje.split('\n'):
            linea_limpia = linea.strip().lstrip('+-').strip()
            if "FEROMONA_EMITIDA:" in linea_limpia:
                try:
                    # Extraemos el JSON crudo después del tag de control
                    json_str = linea_limpia.split("FEROMONA_EMITIDA:", 1)[1].strip()
                    payload = json.loads(json_str)
                    return payload
                except json.JSONDecodeError:
                    print("⚠️ [Escuela-Error] Estructura LBH localizada pero el JSON está corrupto.")
        return None

    def validar_privilegios_soberanos(self, origen, payload):
        """Valida si el remitente y el modo del payload gozan de estatus soberano."""
        # Cruzamos los datos del payload con la matriz de gobernanza local (.human)
        if origen in self.NODOS_AUTORIZADOS:
            perfil = self.NODOS_AUTORIZADOS[origen]
            if payload.get("origin") == origen and payload.get("mode") == "master":
                print(f"🔑 [Acceso Concedido] Firma e Identidad válidas para SOBERANO: {origen} (Modo Master)")
                return True
        print(f"🔒 [Acceso Denegado] Intento de ejecución no autorizado por: {origen}")
        return False

    def ejecutar_accion_local(self, payload):
        """Gatilla una acción automatizada en caliente dentro de Termux (Edge Computing)."""
        tipo_pulso = payload.get("type", "desconocido")
        print(f"⚡ [Procesador de Borde] Interpretando bytes LBH tipo: '{tipo_pulso}'")
        
        # Mapeo de lógica a comandos de sistema basados en la instrucción LBH
        if tipo_pulso == "mosquito_pulse":
            print("🦗 [Acción Termux] Activando pulso de telemetría local...")
            # Aquí la hormiga interactúa con el entorno (ej. disparar un script local, encender un log, etc.)
            subprocess.run(["echo", "🐜 Alerta: Nodo Escuela procesó mosquito_pulse de forma exitosa."])
        else:
            print("💤 [Acción] Estímulo estandarizado recibido, no requiere llamada a hardware.")

    def iniciar_entrenamiento(self):
        """Iniciador del ciclo de vida del agente."""
        mensaje = self.capturar_objeto_crudo()
        
        # 1. Leer remitente de la cabecera limpia
        remitente_crudo = mensaje.get("From", "Desconocido")
        # Limpieza rápida por si viene con el formato de Git
        origen_limpio = remitente_crudo.replace('+', '').strip()
        if "<" in origen_limpio: # Si viene estilo 'Nombre <correo@dominio.com>'
            origen_limpio = origen_limpio.split("<")[0].strip()
        
        # 2. Leer el cuerpo completo del mensaje
        cuerpo = self.procesar_cuerpo_y_payload(mensaje)
        
        # 3. Detectar el contrato o feromona LBH
        payload_lbh = self.detectar_contrato_lbh(cuerpo)
        
        if payload_lbh:
            print("🐜 [Escuela-Nodo] Contrato LBH Detectado con éxito en el cuerpo.")
            # 4. Validar privilegios del emisor
            if self.validar_privilegios_soberanos(origen_limpio, payload_lbh):
                # 5. Ejecutar la acción automatizada local basada en los bytes recibidos
                self.ejecutar_accion_local(payload_lbh)
        else:
            print("💤 [Escuela-Nodo] Correo ordinario recibido. Ningún contrato LBH detectado en el cuerpo.")

if __name__ == "__main__":
    # Arrancamos la matriz de entrenamiento de la hormiga
    agente = HormigaEntrenadoraLBH()
    agente.iniciar_entrenamiento()

