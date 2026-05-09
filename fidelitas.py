import pywhatkit as kit
import datetime
import pyautogui # Importamos la herramienta de teclado
import time

hora = datetime.datetime.now().hour
minuto = datetime.datetime.now().minute + 1

# Ejecutamos la función
kit.sendwhatmsg(
    "+50671691824",
    "Hola, este es un mensaje automático",
    hora,
    minuto,
    15, True, 3
)

# TRUCO EXTRA: Forzar el Enter manualmente por código
# Esperamos 20 segundos (15 de carga + unos 5 de margen)
time.sleep(20) 
pyautogui.press('enter')