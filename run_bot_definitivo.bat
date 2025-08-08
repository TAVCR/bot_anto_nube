@echo off
title Bot Runner - Antologias

echo ==================================================
echo  Iniciando el Bot de WhatsApp para Antologias...
echo ==================================================
echo.

:: Este comando es CRUCIAL.
:: Cambia el directorio de trabajo a la carpeta donde se encuentra este archivo .bat.
:: Esto asegura que Python pueda encontrar 'whatsapp_bot_gemini.py'.
cd /d "%~dp0"

echo Verificando ubicacion...
echo Estoy trabajando en: %cd%
echo.

echo Lanzando el script de Python...
echo.

python whatsapp_bot_gemini.py

echo.
echo ==================================================
echo El script del bot se ha detenido.
echo La ventana permanecera abierta para que puedas ver cualquier mensaje.
echo ==================================================

pause
