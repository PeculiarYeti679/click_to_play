import pyautogui
import time 



stop = False

while not stop:
    pos = pyautogui.position()
    time.sleep(2)
    print(pos)


