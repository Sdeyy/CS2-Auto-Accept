import pyautogui
import time
from colorama import Fore, Style
import sys
import os
import cv2 # type: ignore

print(Fore.RED + Style.BRIGHT + """
   ___  __  ____________    ___  _________________  ______
  / _ |/ / / /_  __/ __ \  / _ |/ ___/ ___/ __/ _ \/_  __/
 / __ / /_/ / / / / /_/ / / __ / /__/ /__/ _// ___/ / /   
/_/ |_\____/ /_/  \____/ /_/ |_\___/\___/___/_/    /_/    
"""+ Fore.BLUE + """
                                                    """ + Fore.YELLOW + """
  ____________ 
 / ___/ __/_  |
/ /___\ \/ __/ 
\___/___/____/ 
                """+ Fore.WHITE + """      
""")

print(Fore.GREEN + "Starting in 3 seconds !" + Style.RESET_ALL)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Asegurar que la ruta es correcta
image_path = "C:\\Users\\villa\\Desktop\\test\\cheto\\autoaccept\\image.png"

if not os.path.exists(image_path):
    print(f"❌ La imagen no existe en la ruta: {image_path}")
else:
    print("✅ La imagen se encontró correctamente.")

def detect_and_click(image_path):
    time.sleep(3)
    while True:
        try:
            x, y = 900, 506
            if x and y:
                pyautogui.click(x, y)
                print(Fore.GREEN + "✅ CLICKED IN AUTOACCEPT Successfully" + Style.RESET_ALL)
                print(Fore.GREEN + "🔄 ReStarting in 3 seconds !" + Style.RESET_ALL)
                time.sleep(3)
            else:
                print("🔍 Botón no encontrado, intentando de nuevo...")
        except pyautogui.ImageNotFoundException:
            print("⚠️ Imagen no encontrada, reintentando en 1 segundo...")
            time.sleep(1)

detect_and_click(image_path)