import pyautogui
import time 
import random


x = random.randint(0,50)
y = random.randint(0,100)
y 
x_coord = 1680
y_coord = 600

time.sleep(30)

stop = ""

while not stop:
    pyautogui.click(x, y)
    time.sleep(12)
    pyautogui.click(x=1680, y=600)
    time.sleep(12)
    pyautogui.click(x, y)


