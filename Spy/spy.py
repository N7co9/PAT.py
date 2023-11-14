import pyautogui
import time
import win32gui
import pyscreeze
from pyautogui import ImageNotFoundException
from PIL import Image
from PIL import ImageGrab


class Spy:

    def locate_dance_game_popup(self):
        try:
            img = Image.open(
                'C:\\Users\\root\\Documents\\PythonProjects\\Wizzard101-PetAutomationTool\\Spy\\ImageTemplates\\DanceGamePopUp.png')
            pyautogui.locateOnScreen(img, 0.0, confidence=0.7)
        except ImageNotFoundException:
            return ImageNotFoundException

    def locate_level(self):
        try:
            img = Image.open(
                'C:\\Users\\root\\Documents\\PythonProjects\\Wizzard101-PetAutomationTool\\Spy\\ImageTemplates\\Level.png')
            coordinates = pyautogui.locateOnScreen(img, 0.0, confidence=0.9)
            return coordinates
        except ImageNotFoundException:
            return ImageNotFoundException

    def locate_play(self):
        try:
            img = Image.open(
                'C:\\Users\\root\\Documents\\PythonProjects\\Wizzard101-PetAutomationTool\\Spy\\ImageTemplates\\Play.png')
            coordinates = pyautogui.locateOnScreen(img, 0.0, confidence=0.7)
            return coordinates
        except ImageNotFoundException:
            return ImageNotFoundException

    def wait_for_loading(self):
        hwndMain = win32gui.FindWindow('Wizard Graphical Client', 'Wizard101')
        region = win32gui.GetWindowRect(hwndMain)

        # Maximum time (in seconds) to search for the image
        max_search_time = 10

        start_time = time.time()

        while True:
            # Take a screenshot of the specified region
            im = ImageGrab.grab(region)
            center = pyscreeze.center(region)

            try:
                pixel = im.getpixel(center)
                if pixel != (67, 64, 135):
                    self.catch_sequence()
                    # yay, finished loading
                    break

            except Exception as e:
                # Handle exceptions here, if needed
                pass

            # Check if the maximum search time has passed
            if time.time() - start_time > max_search_time:
                print("Image not found within the specified time.")
                break

    def catch_sequence(self):
        time.sleep(2)
        MatchThisRequest = Image.open(
            'C:\\Users\\root\\Documents\\PythonProjects\\Wizzard101-PetAutomationTool\\Spy\\ImageTemplates\\request.png')
        window_region = pyautogui.locateOnScreen(MatchThisRequest, 0.0, confidence=0.7)
        region = (
            int(window_region[0]), int(window_region[1]), int(window_region[2]), int(window_region[3]))
        num_screenshots = 3

        for i in range(num_screenshots):
            time.sleep(0.5)
            screenshot = pyscreeze.screenshot(region=region)
            screenshot.save(f"image_{i + 1}.png")
