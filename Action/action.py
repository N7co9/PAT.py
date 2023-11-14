import pyautogui
import time
import pyscreeze


class Action:

    def simulate_popup_press(self, coordinates):
        """Simulates a popup press at the given coordinates."""
        if coordinates is not None:
            pyautogui.press('x')

    def simulate_level_selection(self, coordinates):
        """Simulates a level selection at the given coordinates."""
        if coordinates is not None:
            coordinates = pyscreeze.center(coordinates)
            pyautogui.moveTo(coordinates)
            pyautogui.click(coordinates, clicks=1)

    def simulate_play_execution(self, coordinates):
        """Simulates a play execution at the given coordinates."""
        if coordinates is not None:
            coordinates = pyscreeze.center(coordinates)
            pyautogui.moveTo(coordinates)
            pyautogui.click(coordinates, clicks=1)

    def simulate_key_presses(self, keys):
        """Simulates pressing a sequence of keys."""
        for key in keys:
            pyautogui.press(key)
            time.sleep(0.3)  # Adjust the sleep duration if needed
