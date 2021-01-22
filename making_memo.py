import psutil
import pyautogui
import subprocess
import time
import win32gui
import win32con

# Config
MAX_HOUR = 3
MEMO_EXE_PATH = r'%windir%\system32\notepad.exe'

def main():
    max_minutues = MAX_HOUR*60

    memo_process = subprocess.Popen(MEMO_EXE_PATH, shell=True)
    time.sleep(1)

    memo_hander = win32gui.GetForegroundWindow()
    stop_requested = False
    for m in range(max_minutues):
        try:
            pyautogui.typewrite("[" + str(m+1) + "] ")
            for s in range (60):
                pyautogui.typewrite(str(s+1))
                if s != 60:
                    pyautogui.typewrite(", ")
                time.sleep(1)
            pyautogui.press("enter")

        except KeyboardInterrupt:
            print("STOP WAS REQUESTED")
            stop_requested = True
            win32gui.PostMessage(memo_hander, win32con.WM_QUIT,0,0)
            memo_process.wait()
            break

    if not stop_requested:
        print("TIME IS OVER(" + str(MAX_HOUR) + ")")

    input()
    pyautogui.hotkey('alt','f4')

if __name__ == "__main__":
    main()