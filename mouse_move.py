import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False

try:
    x, y = pyautogui.position()
    while True:
        pyautogui.moveTo(x+30, y+30)
        pyautogui.moveTo(x-30, y-30)
except KeyboardInterrupt:
    print('End')