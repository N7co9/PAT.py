
import pyautogui
import time
import pyscreeze
import os
import re


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
        time.sleep(1.5)

    def simulate_next_selection(self, coordinates):
        """Simulates a level selection at the given coordinates."""
        if coordinates is not None:
            coordinates = pyscreeze.center(coordinates)
            pyautogui.moveTo(coordinates)
            pyautogui.click(coordinates, clicks=1)

    def simulate_finish_selection(self, coordinates):
        """Simulates a level selection at the given coordinates."""
        if coordinates is not None:
            coordinates = pyscreeze.center(coordinates)
            pyautogui.moveTo(coordinates)
            pyautogui.click(coordinates, clicks=1)

    def simulate_key_presses(self, keys):
        """Simulates pressing a sequence of keys."""
        for key in keys:
            time.sleep(0.25)
            pyautogui.press(key)
            # Adjust the sleep duration if needed

    def clean_root_directory(self):
        # Define the naming pattern for image files to be deleted
        pattern = re.compile(r'image_(\d+)\.png')

        # Get a list of files in the root directory
        root_files = os.listdir()

        # Iterate through files and delete those that match the naming pattern
        for file in root_files:
            if pattern.match(file):
                try:
                    os.remove(file)
                    print(f"Deleted: {file}")
                except Exception as e:
                    print(f"Error deleting {file}: {e}")