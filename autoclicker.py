import pyautogui
import time

Switch=True
time.sleep(2)
ticks=1
while Switch:
    pyautogui.click(pyautogui.position())
    time.sleep(ticks/20)
