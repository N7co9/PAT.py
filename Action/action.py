import pyautogui
import time


class Action:
    def simulate_key_presses(self, keys):
        for key in keys:
            pyautogui.press(key)
            time.sleep(0.3)  # Adjust the sleep duration if needed

