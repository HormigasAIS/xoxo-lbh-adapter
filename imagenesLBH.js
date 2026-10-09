// 🐜 HormigasAIS: Lógica de Interfaz Delegada
const CLIENT_ID = "ant_visual_node_" + Math.random().toString(16).slice(2);
const client = new Paho.MQTT.Client("192.168.1.3", 9001, CLIENT_ID);

client.onMessageArrived = function(message) {
    const payload = JSON.parse(message.payloadString);
    const monitor = document.getElementById('monitor');
    const status = document.getElementById('status');

    // Actualización instantánea del DOM
    status.innerText = "Nodo San Miguel: EN LÍNEA (LBH-ACTIVE)";
    status.style.color = "#00ff00";

    // Formateo de Feromona recibida
    monitor.innerHTML = `
        <div style="border-left: 3px solid #00ff00; padding-left: 10px; margin-bottom: 10px;">
            <strong style="color: #00ff00;">🐜 FEROMONA:</strong> ${payload.type}<br>
            <strong>📡 ORIGEN:</strong> ${payload.origin || 'Edge-Node'}<br>
            <strong>🔑 LBH_SIGN:</strong> <span style="font-family: monospace;">${payload.lbh_sign || '01001100'}</span><br>
            <strong>⏱️ TIMESTAMP:</strong> ${new Date().toLocaleTimeString()}
        </div>
    `;
    
    console.log("📥 Feromona procesada por el enjambre visual.");
};

client.onConnectionLost = function(response) {
    document.getElementById('status').innerText = "⚠️ BUSCANDO RASTRO (Reconectando...)";
    document.getElementById('status').style.color = "#ff3300";
    setTimeout(conectarEnjambre, 3000);
};

function conectarEnjambre() {
    client.connect({
        onSuccess: () => {
            console.log("✅ Conectado al Bus XOXO");
            client.subscribe("hormigas/+/feromona");
        },
        onFailure: (err) => {
            console.log("❌ Error de conexión:", err);
            setTimeout(conectarEnjambre, 5000);
        },
        keepAliveInterval: 30,
        useSSL: false
    });
}

// Inicio de la Hormiga Visual
conectarEnjambre();
