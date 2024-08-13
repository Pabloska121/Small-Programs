import pyautogui
import time
import keyboard

Switch=True

def detener_autoclicker():
    global Switch
    Switch = False

keyboard.add_hotkey('q', detener_autoclicker)

ticks=1

time.sleep(2)
while Switch:
    pyautogui.click(pyautogui.position())
    time.sleep(ticks/20)

print("Autoclicker detenido")
