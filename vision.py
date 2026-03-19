import cv2
import numpy as np
import pyautogui

def find_eta_field(template_path):

    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    template = cv2.imread(template_path)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    h, w = template.shape[:2]
    center = (max_loc[0] + w // 2, max_loc[1] + h // 2)

    return max_val, center