
# -*- coding: utf-8 -*-

# --- Enlaces y Datos del Restaurante ---
FACEBOOK_LINK = "https://www.facebook.com/restauranteantologias"
INSTAGRAM_LINK = "https://www.instagram.com/antologias_cr/"
TIKTOK_LINK = "https://www.tiktok.com/@antologias_cr"
MENU_LINK = "app.bystro.cr/antologias/menu"
SINPE_NUMBER = "6168-0909"
LOCATION_LINK = "https://maps.app.goo.gl/vBG7p5fLUxsw3EV18"
PHONE_NUMBER_RESTAURANT = "2250-4789"
PHONE_NUMBER_EVENTS = "8830-7837"

# --- Configuración de Alertas por Correo ---
# Dirección desde donde se enviará la alerta
ALERT_EMAIL_SENDER = "tavocr@gmail.com"
# Contraseña de Aplicación de 16 letras generada en Google
ALERT_EMAIL_PASSWORD = "rclm phpp tfev liyh"
# Dirección que recibirá la alerta
ALERT_EMAIL_RECIPIENT = "tavocr@gmail.com"


# --- Respuestas Automáticas Predefinidas ---
# El nuevo bot buscará estas palabras clave en los mensajes.
AUTO_REPLIES = {
    "hola": "¡Hola! 👋 ¡Bienvenid@ al sistema de venta de entradas de Antologías! ¿En qué puedo ayudarte?",
    "buenos días": "¡Buenos días! ☀️ ¡Bienvenid@ al sistema de venta de entradas de Antologías! ¿En qué puedo ayudarte?",
    "buenas tardes": "¡Buenas tardes! 🌤️ ¡Bienvenid@ al sistema de venta de entradas de Antologías! ¿En qué puedo ayudarte?",
    "buenas noches": "¡Buenas noches! 🌙 ¡Bienvenid@ al sistema de venta de entradas de Antologías! ¿En qué puedo ayudarte?",
    "precio": f"Para información de precios, por favor visitá nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}). 📲 Buscá el banner del evento que te interese y ahí tendrás los precios y otros detalles. 🎟️",
    "precios": f"Para información de precios, por favor visitá nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}). 📲 Buscá el banner del evento que te interese y ahí tendrás los precios y otros detalles. 🎟️",
    "costo": f"Para información de precios, por favor visitá nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}). 📲 Buscá el banner del evento que te interese y ahí tendrás los precios y otros detalles. 🎟️",
    "costos": f"Para información de precios, por favor visitá nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}). 📲 Buscá el banner del evento que te interese y ahí tendrás los precios y otros detalles. 🎟️",
    "gracias": "¡Con mucho gusto! 😊 Si necesitás algo más, solo preguntá.",
    "sinpe":  f"El número SINPE para depositar el monto de tus entradas es {SINPE_NUMBER}. 💳 No olvidés adjuntar el comprobante incluyendo tu nombre, apellidos y el número de entradas adquiridas para poder gestionar tu reservación. ¡Gracias!",
    "información":  f"¡Claro! La información más relevante para los eventos de tu interés está en cada banner que publicamos en nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}). 🧐 Buscá el del evento que te interese y ahí verás todos los detalles.",
    "info":  f"¡Claro! La información más relevante para los eventos de tu interés está en cada banner que publicamos en nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}). 🧐 Buscá el del evento que te interese y ahí verás todos los detalles.",
    "hora": f"La hora de cada evento está especificada en su banner. 🕒 Podés encontrar toda la info en nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}).",
    "horas": f"La hora de cada evento está especificada en su banner. 🕒 Podés encontrar toda la info en nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}).",
    "horario": f"El horario de cada evento está especificado en su banner. 🕒 Podés encontrar toda la info en nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}). Adicionalmente, te comento que Antologías se encuentra abierto al público de Domingo a Jueves de 11:00 AM a 11:00 PM, Viernes y Sábados de 11:00 AM a 12:00 MN.",
    "abierto": f"Antologías se encuentra abierto al público de Domingo a Jueves de 11:00 AM a 11:00 PM, Viernes y Sábados de 11:00 AM a 12:00 MN. La hora de cada evento está especificada en su banner. 🕒 Podés encontrar toda la info en nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}).",
    "abiertos": f"Antologías se encuentra abierto al público de Domingo a Jueves de 11:00 AM a 11:00 PM, Viernes y Sábados de 11:00 AM a 12:00 MN. La hora de cada evento está especificada en su banner. 🕒 Podés encontrar toda la info en nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}).",
    "reservar": f"Para hacer tu reservación, por favor depositá el monto adecuado para el número de entradas que deseás al Sinpe {SINPE_NUMBER}. 📲 No olvidés adjuntar la imagen del comprobante con tu nombre, el número de entradas adquiridas y el evento de tu interés para poder gestionar tu reservación. ¡Gracias! 🙏 En días en los que no hay eventos programados, puede hacer su reservación al teléfono: {PHONE_NUMBER_RESTAURANT}. ¡Te esperamos! 😉",
    "reservación": f"Para hacer tu reservación, por favor depositá el monto adecuado para el número de entradas que deseás al Sinpe {SINPE_NUMBER}. 📲 No olvidés adjuntar la imagen del comprobante con tu nombre, el número de entradas adquiridas y el evento de tu interés para poder gestionar tu reservación. ¡Gracias! 🙏 En días en los que no hay eventos programados, puede hacer su reservación al teléfono: {PHONE_NUMBER_RESTAURANT}. ¡Te esperamos! 😉",
    "reservaciones": f"Para hacer tu reservación, por favor depositá el monto adecuado para el número de entradas que deseás al Sinpe {SINPE_NUMBER}. 📲 No olvidés adjuntar la imagen del comprobante con tu nombre, el número de entradas adquiridas y el evento de tu interés para poder gestionar tu reservación. ¡Gracias! 🙏 En días en los que no hay eventos programados, puede hacer su reservación al teléfono: {PHONE_NUMBER_RESTAURANT}. ¡Te esperamos! 😉",
    "evento": f"Toda la información de los eventos de este mes está en nuestra agenda. 🗓️ La podés encontrar como mensaje fijado en nuestro Facebook ({FACEBOOK_LINK}). Si te interesa algún evento en particular, buscá el banner en nuestro Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}).",
    "eventos": f"Toda la información de los eventos de este mes está en nuestra agenda. 🗓️ La podés encontrar como mensaje fijado en nuestro Facebook ({FACEBOOK_LINK}). Si te interesa algún evento en particular, buscá el banner en nuestro Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}).",
    "entradas": f"¡Claro! Si ya sabés a cuál evento querés asistir, podés hacer tu reservación depositando el monto correspondiente al Sinpe {SINPE_NUMBER}. 🎟️ Luego nos enviás una imagen del comprobante junto con tu nombre, el evento de interés y la cantidad de entradas que compraste. ¡Y listo!",
    "ticket": f"¡Claro! Si ya sabés a cuál evento querés asistir, podés hacer tu reservación depositando el monto correspondiente al Sinpe {SINPE_NUMBER}. 🎟️ Luego nos enviás una imagen del comprobante junto con tu nombre, el evento de interés y la cantidad de entradas que compraste. ¡Y listo!",
    "tickets": f"¡Claro! Si ya sabés a cuál evento querés asistir, podés hacer tu reservación depositando el monto correspondiente al Sinpe {SINPE_NUMBER}. 🎟️ Luego nos enviás una imagen del comprobante junto con tu nombre, el evento de interés y la cantidad de entradas que compraste. ¡Y listo!",
    "bandas": f"Los artistas que se presentan en Antologías cambian cada semana. 🎤 Te invitamos a revisar nuestra agenda en Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}) donde publicamos los banners con toda la info.",
    "quién toca": f"Los artistas que se presentan en Antologías cambian cada semana. 🎤 Te invitamos a revisar nuestra agenda en Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}) donde publicamos los banners con toda la info.",
    "artista": f"Los artistas que se presentan en Antologías cambian cada semana. 🎤 Te invitamos a revisar nuestra agenda en Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}) donde publicamos los banners con toda la info.",
    "artistas": f"Los artistas que se presentan en Antologías cambian cada semana. 🎤 Te invitamos a revisar nuestra agenda en Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}) donde publicamos los banners con toda la info.",
    "música": f"¡Tenemos música para todos los gustos! 🎶 Los artistas cambian cada semana. Te invitamos a revisar nuestra agenda en Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}).",
    "tocan": f"Los artistas que se presentan en Antologías cambian cada semana. 🎤 Te invitamos a revisar nuestra agenda en Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}) donde publicamos los banners con toda la info.",
    "cuánto cuesta": f"Los precios pueden variar dependiendo del evento. Para ver los precios actualizados, buscá el banner del evento que te interesa en nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}). 🤑",
    "cuál es el precio": f"Los precios pueden variar dependiendo del evento. Para ver los precios actualizados, buscá el banner del evento que te interesa en nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}). 🤑",
    "tarifa": f"Los precios pueden variar dependiendo del evento. Para ver los precios actualizados, buscá el banner del evento que te interesa en nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}). 🤑",
    "tarifas": f"Los precios pueden variar dependiendo del evento. Para ver los precios actualizados, buscá el banner del evento que te interesa en nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}). 🤑",
    "cuánto vale": f"Los precios pueden variar dependiendo del evento. Para ver los precios actualizados, buscá el banner del evento que te interesa en nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}). 🤑",
    "hay espacio": f"¡Hola! 👋 A menos que anunciemos lo contrario en nuestras redes sociales (Facebook: {FACEBOOK_LINK}, Instagram: {INSTAGRAM_LINK} o TikTok: {TIKTOK_LINK}), ¡aún podés reservar! Para confirmar tu espacio, te recomendamos hacerlo con tiempo depositando por Sinpe al {SINPE_NUMBER}. ¿Para qué fecha o evento te gustaría consultar?",
    "queda campo": f"¡Hola! 👋 A menos que anunciemos lo contrario en nuestras redes sociales (Facebook: {FACEBOOK_LINK}, Instagram: {INSTAGRAM_LINK} o TikTok: {TIKTOK_LINK}), ¡aún podés reservar! Para confirmar tu espacio, te recomendamos hacerlo con tiempo depositando por Sinpe al {SINPE_NUMBER}. ¿Para qué fecha o evento te gustaría consultar?",
    "todavía hay lugar": f"¡Hola! 👋 A menos que anunciemos lo contrario en nuestras redes sociales (Facebook: {FACEBOOK_LINK}, Instagram: {INSTAGRAM_LINK} o TikTok: {TIKTOK_LINK}), ¡aún podés reservar! Para confirmar tu espacio, te recomendamos hacerlo con tiempo depositando por Sinpe al {SINPE_NUMBER}. ¿Para qué fecha o evento te gustaría consultar?",
    "disponible": f"¡Hola! 👋 A menos que anunciemos lo contrario en nuestras redes sociales (Facebook: {FACEBOOK_LINK}, Instagram: {INSTAGRAM_LINK} o TikTok: {TIKTOK_LINK}), ¡aún podés reservar! Para confirmar tu espacio, te recomendamos hacerlo con tiempo depositando por Sinpe al {SINPE_NUMBER}. ¿Para qué fecha o evento te gustaría consultar?",
    "disponibilidad": f"¡Hola! 👋 A menos que anunciemos lo contrario en nuestras redes sociales (Facebook: {FACEBOOK_LINK}, Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}), ¡aún podés reservar! Para confirmar tu espacio, te recomendamos hacerlo con tiempo depositando por Sinpe al {SINPE_NUMBER}. ¿Para qué fecha o evento te gustaría consultar?",
    "cuántas personas por mesa": f"Nuestras mesas usualmente son para grupos de 2 a 6 personas. 👨‍👩‍👧‍👦 Si venís con un grupo más grande, avisános con tiempo y haremos lo posible por acomodarlos juntos. También podemos negociar precio por volumen de entradas. Para reservar, depositá al Sinpe {SINPE_NUMBER} y mandános el comprobante.",
    "mesas": f"Nuestras mesas usualmente son para grupos de 2 a 6 personas. 👨‍👩‍👧‍👦 Si venís con un grupo más grande, avisános con tiempo y haremos lo posible por acomodarlos juntos. También podemos negociar precio por volumen de entradas. Para reservar, depositá al Sinpe {SINPE_NUMBER} y mandános el comprobante.",
    "capacidad": f"Nuestras mesas usualmente son para grupos de 2 a 6 personas. 👨‍👩‍👧‍👦 Si venís con un grupo más grande, avisános con tiempo y haremos lo posible por acomodarlos juntos. También podemos negociar precio por volumen de entradas. Para reservar, depositá al Sinpe {SINPE_NUMBER} y mandános el comprobante.",
    "cancelar": "Lamentamos que no podás asistir. 😔 En general, las entradas no son reembolsables, pero si querés transferirlas a otra persona, avisános para actualizar los datos de la reservación.",
    "devolver": "Lamentamos que no podás asistir. 😔 En general, las entradas no son reembolsables, pero si querés transferirlas a otra persona, avisános para actualizar los datos de la reservación.",
    "reembolso": "Lamentamos que no podás asistir. 😔 En general, las entradas no son reembolsables, pero si querés transferirlas a otra persona, avisános para actualizar los datos de la reservación.",
    "no puedo ir": "Lamentamos que no podás asistir. 😔 En general, las entradas no son reembolsables, pero si querés transferirlas a otra personan, avisános para actualizar los datos de la reservación.",
    "menú": f"¡Por supuesto! Antologías es un Restaurante con opciones gastronómicas para todos los gustos. 🧑‍🍳 Podés ver nuestro menú completo aquí: {MENU_LINK}",
    "menu": f"¡Por supuesto! Antologías es un Restaurante con opciones gastronómicas para todos los gustos. 🧑‍🍳 Podés ver nuestro menú completo aquí: {MENU_LINK}",
    "comida": f"¡Claro! Antologías es un Restaurante con opciones gastronómicas para todos los gustos. 🧑‍🍳 Podés ver nuestro menú completo aquí: {MENU_LINK}",
    "carta": f"¡Claro! Antologías es un Restaurante con opciones gastronómicas para todos los gustos. 🧑‍🍳 Podés ver nuestro menú completo aquí: {MENU_LINK}",
    "cenar": f"¡Claro! Antologías es un Restaurante con opciones gastronómicas para todos los gustos. 🧑‍🍳 Podés ver nuestro menú completo aquí: {MENU_LINK}",
    "comen": f"¡Claro! Antologías es un Restaurante con opciones gastronómicas para todos los gustos. 🧑‍🍳 Podés ver nuestro menú completo aquí: {MENU_LINK}",
    "niños": "La mayoría de nuestros eventos son para toda la familia. 👨‍👩‍👧‍👦 Te recomendamos revisar el banner del evento que te interesa, donde indicaríamos restricción de edad si fuera el caso. Pero en general somos un Restaurante familiar y siempre tenemos lugar para los pequeñines. PD: ellos pagan el total de su entrada.",
    "niña": "La mayoría de nuestros eventos son para toda la familia. 👨‍👩‍👧‍👦 Te recomendamos revisar el banner del evento que te interesa, donde indicaríamos restricción de edad si fuera el caso. Pero en general somos un Restaurante familiar y siempre tenemos lugar para los pequeñines. PD: ellos pagan el total de su entrada.",
    "chiquito": "La mayoría de nuestros eventos son para toda la familia. 👨‍👩‍👧‍👦 Te recomendamos revisar el banner del evento que te interesa, donde indicaríamos restricción de edad si fuera el caso. Pero en general somos un Restaurante familiar y siempre tenemos lugar para los pequeñines. PD: ellos pagan el total de su entrada.",
    "menores": "La mayoría de nuestros eventos son para toda la familia. 👨‍👩‍👧‍👦 Te recomendamos revisar el banner del evento que te interesa, donde indicaríamos restricción de edad si fuera el caso. Pero en general somos un Restaurante familiar y siempre tenemos lugar para los pequeñines.",
    "chicos": "La mayoría de nuestros eventos son para toda la familia. 👨‍👩‍👧‍👦 Te recomendamos revisar el banner del evento que te interesa, donde indicaríamos restricción de edad si fuera el caso. Pero en general somos un Restaurante familiar y siempre tenemos lugar para los pequeñines.",
    "chiquitos": "La mayoría de nuestros eventos son para toda la familia. 👨‍👩‍👧‍👦 Te recomendamos revisar el banner del evento que te interesa, donde indicaríamos restricción de edad si fuera el caso. Pero en general somos un Restaurante familiar y siempre tenemos lugar para los pequeñines.",
    "edad mínima": "La mayoría de nuestros eventos son para toda la familia. 👨‍👩‍👧‍👦 Te recomendamos revisar el banner del evento que te interesa, donde indicaríamos restricción de edad si fuera el caso. Pero en general somos un Restaurante familiar y siempre tenemos lugar para los pequeñines.",
    "pueden ir niños": "La mayoría de nuestros eventos son para toda la familia. 👨‍👩‍👧‍👦 Te recomendamos revisar el banner del evento que te interesa, donde indicaríamos restricción de edad si fuera el caso. Pero en general somos un Restaurante familiar y siempre tenemos lugar para los pequeñines.",
    "pago": f"Las reservaciones se hacen mediante depósito al Sinpe {SINPE_NUMBER}. 💳 No olvidés enviar el comprobante con tu nombre completo, número de entradas y a qué evento asistís.",
    "forma de pago": f"Las reservaciones se hacen mediante depósito al Sinpe {SINPE_NUMBER}. 💳 No olvidés enviar el comprobante con tu nombre completo, número de entradas y a qué evento asistís.",
    "transferencia": f"Las reservaciones se hacen mediante depósito al Sinpe {SINPE_NUMBER}. 💳 No olvidés enviar el comprobante con tu nombre completo, número de entradas y a qué evento asistís.",
    "depositar": f"Las reservaciones se hacen mediante depósito al Sinpe {SINPE_NUMBER}. 💳 No olvidés enviar el comprobante con tu nombre completo, número de entradas y a qué evento asistís.",
    "ubicación": f"¡Claro! Estamos ubicados en San Rafael Arriba. De Walmart Desamparados, 500 metros hacia el Sur sobre carretera a Aserrí. 📍 ¡Te esperamos! {LOCATION_LINK}",
    "dónde están": f"¡Claro! Estamos ubicados en San Rafael Arriba. De Walmart Desamparados, 500 metros hacia el Sur sobre carretera a Aserrí. 📍 ¡Te esperamos! {LOCATION_LINK}",
    "cómo llego": f"¡Claro! Estamos ubicados en San Rafael Arriba. De Walmart Desamparados, 500 metros hacia el Sur sobre carretera a Aserrí. 📍 ¡Te esperamos! {LOCATION_LINK}",
    "dirección": f"¡Claro! Estamos ubicados en San Rafael Arriba. De Walmart Desamparados, 500 metros hacia el Sur sobre carretera a Aserrí. 📍 ¡Te esperamos! {LOCATION_LINK}",
    "teléfono": f"¡Por supuesto! Nuestro número de teléfono es {PHONE_NUMBER_RESTAURANT}. 📞",
    "gerente": f"Para contactar al gerente, puedes llamar al {PHONE_NUMBER_EVENTS}, pregunta por Fernando, es un tipo muy buena onda 😉",
    "propietario": f"Para contactar al propietario, puedes llamar al {PHONE_NUMBER_EVENTS}, pregunta por Fernando, es un tipo muy buena onda 😉",
    "dueño": f"Para contactar al dueño, puedes llamar al {PHONE_NUMBER_EVENTS}, pregunta por Fernando, es un tipo muy buena onda 😉",
    "administrador": f"Para contactar al administrador, puedes llamar al {PHONE_NUMBER_EVENTS}, pregunta por Fernando, es un tipo muy buena onda 😉",
    "jefe": f"Para contactar al jefe, puedes llamar al {PHONE_NUMBER_EVENTS}, pregunta por Fernando, es un tipo muy buena onda 😉",
    "que incluye": "Te recordamos que el pago de la entrada a nuestros eventos no incluye el consumo dentro del restaurante. ¡Gracias por tu comprensión! 😉",
    "qué incluye": "Te recordamos que el pago de la entrada a nuestros eventos no incluye el consumo dentro del restaurante. ¡Gracias por tu comprensión! 😉",
    "incluido": "Te recordamos que el pago de la entrada a nuestros eventos no incluye el consumo dentro del restaurante. ¡Gracias por tu comprensión! 😉",
    "persona": "Hemos alertado a un colaborador humano y a la mayor brevedad posible te atenderá en esta misma conversación. 🧑‍💼",
    "humano": "Hemos alertado a un colaborador humano y a la mayor brevedad posible te atenderá en esta misma conversación. 🧑‍💼",
    "agente": "Hemos alertado a un colaborador humano y a la mayor brevedad posible te atenderá en esta misma conversación. 🧑‍💼",
    "asesor": "Hemos alertado a un colaborador humano y a la mayor brevedad posible te atenderá en esta misma conversación. 🧑‍💼",
    "hablar con alguien": "Hemos alertado a un colaborador humano y a la mayor brevedad posible te atenderá en esta misma conversation. 🧑‍💼",
    "ayuda": "Hemos alertado a un colaborador humano y a la mayor brevedad posible te atenderá en esta misma conversación. 🧑‍💼",
    "a que hora me atienden": "Te atenderemos a la mayor brevedad posible. Gracias por tu paciencia. 🙏",
    "gratis": f"Nuestra exhibición de vehículos los primeros martes del mes es totalmente gratuita. 🚗 También podés ir a nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}) donde tenemos fijada nuestra agenda de eventos; ahí aparecen aquellos que son de reserva y aquellos que son de entrada gratuita.",
    "gratuito": f"Nuestra exhibición de vehículos los primeros martes del mes es totalmente gratuita. 🚗 También podés ir a nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}) donde tenemos fijada nuestra agenda de eventos; ahí aparecen aquellos que son de reserva y aquellos que son de entrada gratuita.",
    "free": f"Nuestra exhibición de vehículos los primeros martes del mes es totalmente gratuita. 🚗 También podés ir a nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK}) donde tenemos fijada nuestra agenda de eventos; ahí aparecen aquellos que son de reserva y aquellos que son de entrada gratuita.",
    "cuando me atienden": "Te atenderemos a la mayor brevedad posible. Gracias por tu paciencia. 🙏",
    "imagen": "¡Gracias por adjuntarnos la imagen! 👍 Si corresponde a un SINPE para adquisición de entradas, te confirmaremos tu reservación a la mayor brevedad posible."
}

# --- Mensajes de Fallback para la IA ---
# Estos mensajes se usarán si la API de Gemini falla.
AI_FALLBACK_MESSAGES = [
    f"¡Vaya! Parece que mis musas creativas se tomaron un café. ☕ Mientras vuelven, ¿por qué no le echás un vistazo a nuestra increíble agenda de eventos en Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK})?",
    f"En este momento, mi generador de respuestas ingeniosas está en una pausa para el té. 🍵 Pero la diversión nunca se detiene en Antologías. ¡Descubrí a nuestros próximos artistas en Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK})!",
    f"Mis circuitos de charla están recalculando... 🤖 ¡Pero nuestra cartelera de eventos está más clara que nunca! Te invito a que la veas en nuestro Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK})!",
    f"Se me acaba de cruzar un cable... ¡pero de la emoción por los shows que vienen! 🤩 Mejor te cuento de ellos. Revisá toda la información en Facebook ({FACEBOOK_LINK}), Instagram ({INSTAGRAM_LINK}) o TikTok ({TIKTOK_LINK})!"
]
