import webbrowser
import sys
import pyautogui
import time


def save_to_notepad():
    pyautogui.click(50, 80);
    pyautogui.press('up')
    pyautogui.typewrite("notepad")
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.typewrite("Hello world!")
    pyautogui.press('enter')
    pyautogui.hotkey("Ctrl", "S")
    pyautogui.typewrite("C:/Temp/saved_from_pyautogui.txt")
    pyautogui.press('enter')
    pyautogui.hotkey("Alt", "F4")

def save_to_notepad_lin():

    # pyautogui.KEYBOARD_KEYS
    pyautogui.hotkey("winleft", "f")
    pyautogui.typewrite("geany")
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.typewrite("Hello world!")
    pyautogui.press('enter')
    pyautogui.hotkey("Ctrl", "S")
    pyautogui.typewrite("/tmp/saved_from_pyautogui.txt")
    pyautogui.press('enter')
    pyautogui.hotkey("Alt", "F4")

def simple_demo():

    for i in range(2):
        pyautogui.moveTo(100, 100, duration=0.25)
        pyautogui.click(10, 5)
        pyautogui.moveTo(200, 100, duration=0.25)
        pyautogui.moveTo(200, 200, duration=0.25)
        pyautogui.moveTo(100, 200, duration=0.25)


if __name__ == "__main__":

    pyautogui.PAUSE = 1

    #simple_demo()
    #save_to_notepad()
    save_to_notepad_lin()

