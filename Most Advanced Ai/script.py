import pyautogui
from time import sleep

def info():
    result = pyautogui.position()
    print(result)

sleep(7)
info()