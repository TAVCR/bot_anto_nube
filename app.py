import threading
import os
from flask import Flask
from whatsapp_bot_gemini import main as run_bot_logic

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Esta ruta mantiene feliz al verificador de salud de Render."""
    return 'El servidor del bot está activo y escuchando.'

def start_bot():
    """Función para ejecutar la lógica principal del bot en un hilo separado."""
    print("Iniciando la lógica del bot de WhatsApp en un hilo de fondo...")
    run_bot_logic()

if __name__ == "__main__":
    # Iniciar el bot en un hilo separado para no bloquear el servidor web.
    # El 'daemon=True' asegura que el hilo del bot se cierre si el servidor principal cae.
    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()

    # Iniciar el servidor Flask. Render asignará el puerto dinámicamente.
    port = int(os.environ.get('PORT', 5000))
    print(f"Iniciando servidor web en el puerto {port}...")
    app.run(host='0.0.0.0', port=port)
