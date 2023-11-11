import pyautogui
import win32gui
import time
import pyscreeze
from pyautogui import ImageNotFoundException
from PIL import Image


class Spy:
    def set_active(self):
        hwndMain = win32gui.FindWindow('Wizard Graphical Client', 'Wizard101')
        win32gui.SetForegroundWindow(hwndMain)

    def locate_dance_game_popup(self):
        try:
            img = Image.open(
                'ImageTemplates/DanceGamePopUp.png')
            coordinates = pyautogui.locateCenterOnScreen(img, 3, confidence=0.7)
            return coordinates
        except ImageNotFoundException:
            return ImageNotFoundException

    def locate_level(self):
        try:
            img = Image.open(
                'ImageTemplates/Level.png')
            coordinates = pyautogui.locateCenterOnScreen(img, 3, confidence=0.7)
            return coordinates
        except ImageNotFoundException:
            return ImageNotFoundException

    def locate_play(self):
        try:
            img = Image.open(
                'ImageTemplates/Play.png')
            coordinates = pyautogui.locateCenterOnScreen(img, 3, confidence=0.7)
            return coordinates
        except ImageNotFoundException:
            return ImageNotFoundException

    def catch_sequence_1(self):
        MatchThisRequest = Image.open(
            'ImageTemplates/request.png')
        window_region = pyautogui.locateOnScreen(MatchThisRequest, 0.0, confidence=0.7)
        region = (
            int(window_region[0]), int(window_region[1]), int(window_region[2]), int(window_region[3]))
        num_screenshots = 3

        for i in range(num_screenshots):
            time.sleep(0.5)
            screenshot = pyscreeze.screenshot(region=region)
            screenshot.save(f"image_{i + 1}.png")

    def catch_sequence_2(self):
        img = Image.open(
            'ImageTemplates/MatchThisRequest.png')
        window_region = pyautogui.locateOnScreen(img, 0.0, confidence=0.7)
        region = (
            int(window_region[0]), int(window_region[1]), int(window_region[2]), int(window_region[3]))
        num_screenshots = 4

        for i in range(num_screenshots):
            time.sleep(0.5)
            screenshot = pyscreeze.screenshot(region=region)
            screenshot.save(f"image_{i + 1}.png")

    def catch_sequence_3(self):
        img = Image.open(
            'ImageTemplates/MatchThisRequest.png')
        window_region = pyautogui.locateOnScreen(img, 0.0, confidence=0.7)
        region = (
            int(window_region[0]), int(window_region[1]), int(window_region[2]), int(window_region[3]))
        num_screenshots = 5

        for i in range(num_screenshots):
            time.sleep(0.5)
            screenshot = pyscreeze.screenshot(region=region)
            screenshot.save(f"image_{i + 1}.png")

    def catch_sequence_4(self):
        img = Image.open(
            'ImageTemplates/MatchThisRequest.png')
        window_region = pyautogui.locateOnScreen(img, 0.0, confidence=0.7)
        region = (
            int(window_region[0]), int(window_region[1]), int(window_region[2]), int(window_region[3]))
        num_screenshots = 6

        for i in range(num_screenshots):
            time.sleep(0.5)
            screenshot = pyscreeze.screenshot(region=region)
            screenshot.save(f"image_{i + 1}.png")

    def catch_sequence_5(self):
        img = Image.open(
            'ImageTemplates/MatchThisRequest.png')
        window_region = pyautogui.locateOnScreen(img, 0.0, confidence=0.7)
        region = (
            int(window_region[0]), int(window_region[1]), int(window_region[2]), int(window_region[3]))
        num_screenshots = 7

        for i in range(num_screenshots):
            time.sleep(0.5)
            screenshot = pyscreeze.screenshot(region=region)
            screenshot.save(f"image_{i + 1}.png")


# Create an instance of the observer class
observer_instance = Spy()

# Call the locatePlayerStatus function
observer_instance.catch_sequence_1()
