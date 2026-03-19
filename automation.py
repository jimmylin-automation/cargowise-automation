import pyautogui
import time

def update_eta(position, date_text):

    x, y = position

    pyautogui.click(x, y)
    time.sleep(0.5)

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')

    pyautogui.write(date_text, interval=0.1)
    pyautogui.press('tab')