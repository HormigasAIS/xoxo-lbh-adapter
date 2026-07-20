import os
import json
import sys

class XOXOAdapter:
    def __init__(self, robot_id="generic_node"):
        self.robot_id = robot_id
        self.contract_path = "/data/data/com.termux/files/home/xoxo-lbh-adapter/config.human"
        self.active_role = "ALPHA"
        print(f"📖 [LBH-CORE] Inicializando nodo: {self.robot_id}")
        self.verificar_contrato_maestro()

    def verificar_contrato_maestro(self):
        if not os.path.exists(self.contract_path):
            print(f"❌ [LBH-CRÍTICO] Contrato ausente! Bloqueo preventivo.")
            sys.exit(1)
            
        try:
            with open(self.contract_path, "r") as f:
                contract = json.load(f)
            
            # Ajuste directo al puente de Cristhiam: Lectura plana del contrato real
            fundador = contract.get("fundador", "")
            if "Cristhiam Leonardo Hernández Quiñonez" not in fundador:
                raise ValueError("Firma del fundador inválida o alterada.")
                
            return contract
        except Exception as e:
            print(f"🚨 [LBH-VIOLACIÓN] Contrato corrupto o alterado: {e}. Auto-bloqueo.")
            sys.exit(1)

    def evaluar_gobernanza_dinamica(self, accion_solicitada):
        contract = self.verificar_contrato_maestro()
        permisos = contract.get("PERMISSIONS", {})
        
        if not permisos.get(accion_solicitada, False):
            print(f"🚫 [LBH-ENFORCEMENT] Acción [{accion_solicitada}] DENEGADA!")
            sys.exit(1)
            
        return True

    def loop_forever(self):
        print(f"✅ Conectado al Broker: localhost")
        while True:
            self.evaluar_gobernanza_dinamica("M2M_COMMUNICATION")
            import time
            time.sleep(1)
