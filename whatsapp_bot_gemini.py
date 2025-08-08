import os
import time
import re
import random
from datetime import datetime, timezone, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException, InvalidSessionIdException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import google.generativeai as genai
from selenium.webdriver.chrome.service import Service as ChromeService
import smtplib
import ssl
from email.message import EmailMessage

# --- Configuración ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ALERT_EMAIL_SENDER = os.getenv("ALERT_EMAIL_SENDER")
ALERT_EMAIL_PASSWORD = os.getenv("ALERT_EMAIL_PASSWORD")
ALERT_EMAIL_RECIPIENT = os.getenv("ALERT_EMAIL_RECIPIENT")
LOCATION_LINK = os.getenv("LOCATION_LINK", "https://maps.app.goo.gl/DcR4KxG6fPea8TMJ7")
MENU_LINK = os.getenv("MENU_LINK", "https://antologias.co.cr/menu/")
FACEBOOK_LINK = os.getenv("FACEBOOK_LINK", "https://www.facebook.com/antologiascr")
INSTAGRAM_LINK = os.getenv("INSTAGRAM_LINK", "https://www.instagram.com/antologiascr/")
TIKTOK_LINK = os.getenv("TIKTOK_LINK", "https://www.tiktok.com/@antologiascr")

COSTA_RICA_TZ = timezone(timedelta(hours=-6))
CONTACT_INFO_BLOCK = f"""¡Claro! Aquí tenés toda nuestra información:

📍 **Ubicación:**
San Rafael Arriba de Desamparados, 400 Metros Sur de Walmart
{LOCATION_LINK}

🍽️ **Menú:**
{MENU_LINK}

📱 **Redes Sociales:**
- Facebook: {FACEBOOK_LINK}
- Instagram: {INSTAGRAM_LINK}
- TikTok: {TIKTOK_LINK}

¡Te esperamos! ✨"""
HUMAN_KEYWORDS = [
    "persona", "humano", "humana", "agente", "asesor", 
    "hablar con alguien", "encargado", "encargada", "ayuda"
]
CONTACT_KEYWORDS = [
    "teléfono", "numero", "contacto", "llamar", "escribir"
]
PROCESS_COOLDOWN = 120
CONVERSATION_TIMEOUT = 90

# --- Variables Globales ---
recently_processed_chats = {}
model = None

# --- Lógica de Alertas por Correo ---
def send_human_alert_email(user_name):
    """Envía una alerta por correo electrónico cuando se solicita un humano."""
    if not all([ALERT_EMAIL_SENDER, ALERT_EMAIL_PASSWORD, ALERT_EMAIL_RECIPIENT]):
        print("ALERTA: Faltan variables de entorno de correo (ALERT_EMAIL_SENDER, ALERT_EMAIL_PASSWORD, ALERT_EMAIL_RECIPIENT). No se puede enviar la alerta.")
        return

    subject = f"¡Alerta Humana! - Se necesita intervención en el chat de Antologías"
    body = f"""
    Hola,

    Se ha detectado una solicitud de intervención humana en el chat de WhatsApp.

    - **Cliente:** {user_name}
    - **Hora:** {datetime.now(COSTA_RICA_TZ).strftime('%Y-%m-%d %H:%M:%S')}

    Por favor, revisa la conversación en WhatsApp Web lo antes posible.

    Atentamente,
    Bot Anto
    """

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = ALERT_EMAIL_SENDER
    msg['To'] = ALERT_EMAIL_RECIPIENT

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(ALERT_EMAIL_SENDER, ALERT_EMAIL_PASSWORD.replace(" ", ""))
            server.send_message(msg)
            print(f"ALERTA HUMANA: Correo de alerta enviado exitosamente a {ALERT_EMAIL_RECIPIENT}.")
    except Exception as e:
        print(f"ALERTA HUMANA: Fallo el envío del correo de alerta. Error: {e}")

# --- Inicialización ---
def initialize_ai():
    global model
    if GEMINI_API_KEY:
        try:
            genai.configure(api_key=GEMINI_API_KEY)
            model = genai.GenerativeModel('gemini-1.5-flash')
            print("Modelo de Gemini cargado correctamente.")
        except Exception as e:
            print(f"Error al configurar Gemini: {e}")
    else:
        print("Advertencia: La IA no funcionará sin la variable de entorno GEMINI_API_KEY.")

# --- Lógica de IA ---
def get_gemini_response(user_message, user_name):
    if not model:
        return "En este momento nuestros asistentes de IA no están disponibles, pero en breve un agente te atenderá."
    try:
        prompt = f"""
        Eres "Anto", un asistente de IA para "Antologías", un restaurante de cocina internacional.

        **REGLA #1: Saluda a `{user_name}` por su nombre de forma amigable.**

        **REGLA #2: Tu misión es responder su pregunta y siempre invitarlo a ver la agenda de eventos en redes sociales.**

        **REGLA #3 (MUY IMPORTANTE): NO menciones proactivamente ningún tipo de comida (como "sushi", "pizza", etc.).** Si el usuario te pregunta directamente por un tipo de comida que no manejas, simplemente responde que tu especialidad es la "cocina internacional" e invítalo a ver el menú.

        **REGLA #4: Sé breve, usa "voseo" (habla de "vos") y responde en un solo párrafo.**

        **REGLA #5:** Si necesitas dar información de contacto (menú, ubicación, teléfono, etc.), usa la palabra `[CONTACTO]`.

        Ahora, responde al mensaje de {user_name}: "{user_message}"
        """
        response = model.generate_content(prompt)
        return re.sub(r'[\*#]', '', response.text).strip()
    except Exception as e:
        print(f"Error al contactar con Gemini: {e}")
        return "En este momento nuestros asistentes de IA no están disponibles, pero en breve un agente te atenderá."

# --- LÓGICA DEL BOT (ARQUITECTURA DE MENSAJE ÚNICO) ---

def send_final_message(driver, message):
    """Envía un único bloque de texto, manejando saltos de línea."""
    try:
        sanitized_text = "".join(c for c in message if c <= '\uFFFF').strip()
        if not sanitized_text:
            return False
        
        inp_xpath = '//div[@contenteditable="true"][@data-tab="10"]'
        input_box = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
        
        input_box.clear()
        
        lines = sanitized_text.split('\n')
        for i, line in enumerate(lines):
            input_box.send_keys(line)
            if i < len(lines) - 1:
                input_box.send_keys(Keys.SHIFT, Keys.ENTER)
        
        input_box.send_keys(Keys.ENTER)
        
        print(f"Respuesta única enviada: {sanitized_text[:80]}...")
        return True
    except Exception as e:
        print(f"Error al enviar mensaje final: {e}")
        return False

def get_final_response(message_text, has_image, user_name):
    """Prepara un único string final para enviar. NO envía nada."""
    message_buffer = []
    human_handover = False
    
    # Definimos respuestas automáticas por defecto que pueden ser sobreescritas por variables de entorno
    AUTO_REPLIES = {
        "gracias": "¡De nada! Estamos para servirte.",
        "ubicacion": "[CONTACTO]",
        "dirección": "[CONTACTO]",
        "localización": "[CONTACTO]",
        "ubicación": "[CONTACTO]",
        "menu": "¡Claro! Aquí puedes ver nuestro menú completo: [CONTACTO]",
        "menú": "¡Claro! Aquí puedes ver nuestro menú completo: [CONTACTO]",
        "evento": "¡Tenemos eventos especiales toda la semana! Te invito a revisar nuestras redes sociales para ver la agenda completa. [CONTACTO]",
        "eventos": "¡Tenemos eventos especiales toda la semana! Te invito a revisar nuestras redes sociales para ver la agenda completa. [CONTACTO]",
        "musica": "¡Claro! Tenemos música en vivo varios días. Revisa la agenda en nuestras redes para que no te lo pierdas. [CONTACTO]",
        "música": "¡Claro! Tenemos música en vivo varios días. Revisa la agenda en nuestras redes para que no te lo pierdas. [CONTACTO]",
        "reserva": "Para reservaciones, por favor llámanos al 2250-4789. ¡Será un placer atenderte!",
        "reservacion": "Para reservaciones, por favor llámanos al 2250-4789. ¡Será un placer atenderte!",
        "reservación": "Para reservaciones, por favor llámanos al 2250-4789. ¡Será un placer atenderte!",
        "horario": "Nuestro horario es de Martes a Domingo, de 12:00 MD a 10:00 PM. ¡Te esperamos!",
        "humano": "Entendido. En un momento un miembro de nuestro equipo te atenderá personalmente."
    }
    IMAGE_REPLY = os.getenv("IMAGE_REPLY", "¡Gracias por la imagen! La estamos revisando.")


    if has_image:
        message_buffer.append(IMAGE_REPLY)
    elif message_text:
        message_lower = message_text.lower()

        for keyword in HUMAN_KEYWORDS:
            if re.search(r'\b' + re.escape(keyword) + r'\b', message_lower):
                message_buffer.append(AUTO_REPLIES.get("humano", "En breve te atenderá un asesor."))
                send_human_alert_email(user_name) # <-- ¡AQUÍ SE LLAMA A LA ALERTA!
                human_handover = True
                break
        
        if not human_handover:
            contact_request_found = False
            for keyword in CONTACT_KEYWORDS:
                if re.search(r'\b' + re.escape(keyword) + r'\b', message_lower):
                    message_buffer.append("Llamanos al 2250-4789 o escribinos por aquí a este WhatsApp")
                    contact_request_found = True
                    break

            if not contact_request_found:
                response_found = False
                for keyword, reply in AUTO_REPLIES.items():
                    if keyword in HUMAN_KEYWORDS: continue
                    if re.search(r'\b' + re.escape(keyword) + r'\b', message_lower):
                        message_buffer.append(reply)
                        response_found = True
                        break
                
                if not response_found:
                    gemini_response = get_gemini_response(message_lower, user_name)
                    message_buffer.append(gemini_response)

    final_parts = []
    for msg in message_buffer:
        if "[CONTACTO]" in msg:
            intro = msg.replace("[CONTACTO]", "").strip()
            if intro:
                final_parts.append(intro)
            final_parts.append(CONTACT_INFO_BLOCK)
        else:
            final_parts.append(msg)
    
    final_response = "\n\n".join(final_parts)
    
    return final_response, human_handover

def get_last_incoming_message_details(driver):
    try:
        message_bubbles = driver.find_elements(By.CSS_SELECTOR, "div.message-in")
        if not message_bubbles: return None, None, False, None
        last_incoming_bubble = message_bubbles[-1]
        message_id, text = None, None
        try: message_id = last_incoming_bubble.get_attribute("data-id")
        except Exception: pass
        try:
            text_element = last_incoming_bubble.find_element(By.CSS_SELECTOR, "span.selectable-text")
            text = text_element.text
        except NoSuchElementException: pass
        if not message_id or message_id.startswith("false_"):
            try:
                meta_element = last_incoming_bubble.find_element(By.CSS_SELECTOR, "div.copyable-text")
                timestamp_str = meta_element.get_attribute("data-pre-plain-text")
            except NoSuchElementException: timestamp_str = time.time()
            message_id = f"{timestamp_str}-{text}"
        has_image = False
        try:
            if last_incoming_bubble.find_element(By.CSS_SELECTOR, "div[role='img'], img[src^='blob:']"):
                has_image = True
        except NoSuchElementException: pass
        return text, 'in', has_image, message_id
    except (NoSuchElementException, StaleElementReferenceException) as e:
        print(f"[DEBUG] Error en get_last_incoming_message_details: {e}")
        return None, None, False, None

def handle_conversation(driver, user_name, initial_message_id):
    """Maneja la conversación después del primer mensaje."""
    print(f"Iniciando modo conversación con '{user_name}'.")
    last_processed_message_id = initial_message_id
    start_time = time.time()
    
    while time.time() - start_time < CONVERSATION_TIMEOUT:
        text, _, has_image, message_id = get_last_incoming_message_details(driver)
        
        if message_id and message_id != last_processed_message_id:
            print(f"Nuevo mensaje en conversación con '{user_name}': {text}")
            last_processed_message_id = message_id
            
            final_response, human_handover = get_final_response(text, has_image, user_name)
            
            if final_response:
                send_final_message(driver, final_response)
            
            if human_handover:
                print(f"ALERTA HUMANA en conversación: Usuario '{user_name}' necesita ayuda.")
                break
            
            start_time = time.time()
        
        time.sleep(3)
    
    print(f"Fin del modo conversación con '{user_name}'.")

def find_and_process_unread_chat(driver):
    try:
        current_time = time.time()
        for user, timestamp in list(recently_processed_chats.items()):
            if current_time - timestamp > PROCESS_COOLDOWN:
                del recently_processed_chats[user]

        unread_chat_xpath = "//div[contains(@class, '_ak8l') and .//span[contains(@aria-label, 'mensaje no leído')]]"
        unread_chats = driver.find_elements(By.XPATH, unread_chat_xpath)
        if not unread_chats: return False

        chat_to_process, user_name = None, None
        for chat_element in unread_chats:
            try:
                user_id_element = chat_element.find_element(By.XPATH, ".//span[@title]")
                title = user_id_element.get_attribute("title")
                if title and title in recently_processed_chats:
                    continue
                chat_to_process = chat_element
                user_name = title
                break
            except Exception: continue

        if not chat_to_process: return False

        print(f"Procesando chat con '{user_name}'.")
        chat_to_process.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')))
        
        text, msg_type, has_image, message_id = get_last_incoming_message_details(driver)

        if msg_type == 'in':
            if user_name:
                recently_processed_chats[user_name] = time.time()

            final_response, human_handover = get_final_response(text, has_image, user_name)
            
            if final_response:
                send_final_message(driver, final_response)

            if not human_handover:
                handle_conversation(driver, user_name, message_id)

            return True
        return False
    except Exception as e:
        print(f"Error buscando chats no leídos: {e}")
        return False

def main():
    initialize_ai()
    if not model:
        print("El bot no puede iniciar sin la IA configurada.")
        return
    
    print("Configurando el navegador en modo headless para la nube...")
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    
    # Dejamos que Selenium y los buildpacks se encarguen de las rutas automáticamente
    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=options)
    # Agregamos un tiempo de espera máximo para la carga de la página
    driver.set_page_load_timeout(120)

    try:
        print("Intentando cargar https://web.whatsapp.com/ (max 120s)...")
        driver.get("https://web.whatsapp.com/")
    except Exception as e:
        print(f"¡ERROR! La carga de la página superó el tiempo de espera o falló: {e}")
        print("--- INICIANDO DIAGNÓSTICO DE PÁGINA ATASCADA ---")
        try:
            page_title = driver.title
            print(f"TÍTULO DE LA PÁGINA ATASCADA: '{page_title}'")
            page_source_snippet = driver.page_source.replace('\n', ' ').strip()[:800]
            print(f"INICIO DEL HTML ATASCADO: {page_source_snippet}")
        except Exception as diag_e:
            print(f"Error al obtener diagnósticos de la página atascada: {diag_e}")
        print("--- FIN DEL DIAGNÓSTICO ---")
        driver.quit()
        return # Detenemos la ejecución del bot

    print("Página cargada. Ahora, esperando a que el elemento 'side' aparezca (120s)...")
    
    try:
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "side")))
        print("WhatsApp Web cargado correctamente.")
    except Exception as e:
        print(f"No se pudo cargar WhatsApp Web. Error: {e}")
        driver.quit()
        return

    print("Bot con IA de Gemini iniciado. Presiona Ctrl+C para detener.")
    while True:
        try:
            if not find_and_process_unread_chat(driver):
                time.sleep(5)
        except KeyboardInterrupt:
            print("\nCerrando el bot.")
            break
        except InvalidSessionIdException:
            print("\nSesión de Selenium inválida.")
            break
        except Exception as e:
            print(f"Ocurrió un error en el bucle principal: {e}")
            time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    main()