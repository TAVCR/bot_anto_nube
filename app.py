import threading
import os
from flask import Flask
from whatsapp_bot_gemini import main as run_bot_logic

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Esta ruta mantiene feliz al verificador de salud de Render."""
    return 'El servidor del bot está activo y el bot de WhatsApp está corriendo en segundo plano.'

def start_bot():
    """Función para ejecutar la lógica principal del bot en un hilo separado."""
    print("Iniciando la lógica del bot de WhatsApp en un hilo de fondo...")
    run_bot_logic()

# --- INICIO DE LA CORRECCIÓN ---
# Movemos el inicio del bot fuera del bloque __main__.
# Esto asegura que se ejecute cuando Gunicorn importa el archivo.
print("Archivo app.py cargado por Gunicorn. Preparando para iniciar el bot...")
bot_thread = threading.Thread(target=start_bot, daemon=True)
bot_thread.start()
# --- FIN DE LA CORRECCIÓN ---

if __name__ == "__main__":
    # Este bloque ahora solo se usará si ejecutas 'python app.py' localmente.
    port = int(os.environ.get('PORT', 5000))
    print(f"Iniciando servidor web para desarrollo local en el puerto {port}...")
    app.run(host='0.0.0.0', port=port)
