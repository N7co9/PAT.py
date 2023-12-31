import pyautogui
import time
import win32gui
import os
import pyscreeze
from pyautogui import ImageNotFoundException
from PIL import Image
from PIL import ImageGrab


class Spy:

    def locate_dance_game_popup(self):
        try:
            img = Image.open(
                'Spy\\ImageTemplates\\DanceGamePopUp.png')
            coordinates = pyautogui.locateOnScreen(img, 0.0, confidence=0.7)
            return coordinates
        except ImageNotFoundException:
            return ImageNotFoundException

    def locate_level(self):
        time.sleep(0.5)
        try:
            img = Image.open(
                'Spy\\ImageTemplates\\Level.png')
            coordinates = pyautogui.locateOnScreen(img, 0.0, confidence=0.8)
            return coordinates
        except ImageNotFoundException:
            return ImageNotFoundException

    def locate_play(self):
        try:
            img = Image.open(
                'Spy\\ImageTemplates\\Play.png')
            coordinates = pyautogui.locateOnScreen(img, 0.0, confidence=0.7)
            return coordinates
        except ImageNotFoundException:
            return ImageNotFoundException

    def locate_next(self):
        time.sleep(3)
        try:
            img = Image.open(
                'Spy\\ImageTemplates\\next.png')
            coordinates = pyautogui.locateOnScreen(img, 0.0, confidence=0.7)
            return coordinates
        except ImageNotFoundException:
            return ImageNotFoundException

    def locate_finish(self):
        time.sleep(1)
        try:
            img = Image.open(
                'Spy\\ImageTemplates\\finish.png')
            coordinates = pyautogui.locateOnScreen(img, 0.0, confidence=0.7)
            return coordinates
        except ImageNotFoundException:
            return ImageNotFoundException

    def wait_for_loading(self):
        hwndMain = win32gui.FindWindow('Wizard Graphical Client', 'Wizard101')
        region = win32gui.GetWindowRect(hwndMain)

        # Maximum time (in seconds) to search for the image
        max_search_time = 10

        im = ImageGrab.grab(region)
        center = pyscreeze.center(region)
        loading_pixel = im.getpixel(center)

        start_time = time.time()

        while True:
            # Take a screenshot of the specified region
            im = ImageGrab.grab(region)
            center = pyscreeze.center(region)

            try:
                new_pixel = im.getpixel(center)

                if new_pixel != loading_pixel:
                    return bool('true')
                    # yay, finished loading

            except Exception as e:
                # Handle exceptions here, if needed
                pass

            # Check if the maximum search time has passed
            if time.time() - start_time > max_search_time:
                print("Image not found within the specified time.")
                break

    def wait_for_start(self, loaded, num):
        sleep_time = 1 if num == 3 else 2.5
        time.sleep(sleep_time)
        hwndMain = win32gui.FindWindow('Wizard Graphical Client', 'Wizard101')
        region = win32gui.GetWindowRect(hwndMain)

        # Calculate the height of the original region
        original_height = region[3] - region[1]

        # Calculate the new bottom coordinate for half of the lower region
        half_lower_bottom = region[1] + original_height // 2

        # Create a new tuple representing half of the lower region
        half_lower_region = (region[0], half_lower_bottom, region[2], region[3])

        hay = ImageGrab.grab(half_lower_region)
        needle = Image.open('Spy\\ImageTemplates\\request.png')
        request_coordinates = pyautogui.locate(needle, hay, confidence=0.7)
        request_center = pyscreeze.center(request_coordinates)

        default_request_pixel = hay.getpixel(request_center)

        code_executed = False  # Flag to track whether the code has been executed

        while True:
            # Check if loaded is False
            if not loaded:
                code_executed = False  # Reset the flag when not loaded
                time.sleep(0.1)
                continue

            # Execute the code only if the flag is False
            if not code_executed:
                # Take a screenshot of the specified region
                loaded_im = ImageGrab.grab(half_lower_region)
                try:
                    new_pixel = loaded_im.getpixel(request_center)
                    if new_pixel != default_request_pixel:
                        self.catch_sequence(num=num)
                        code_executed = True  # Set the flag to True after executing the code
                        break
                except Exception as e:
                    # Handle exceptions here, if needed
                    pass

    def catch_sequence(self, num):
        MatchThisRequest = Image.open('Spy\\ImageTemplates\\request.png')
        window_region = pyautogui.locateOnScreen(MatchThisRequest, 0.0, confidence=0.7)
        region = (
            int(window_region[0]), int(window_region[1]), int(window_region[2]), int(window_region[3]))
        num_screenshots = num

        # Create a folder structure: root -> Spy -> Sequence -> Screenshots_num
        root_folder = "Spy"
        sequence_folder = "Sequence"
        folder_name = f"Screenshots_{num}"

        # Create Spy folder if it doesn't exist
        os.makedirs(root_folder, exist_ok=True)

        # Create Sequence folder if it doesn't exist
        os.makedirs(os.path.join(root_folder, sequence_folder), exist_ok=True)

        # Create Screenshots_num folder
        screenshots_folder = os.path.join(root_folder, sequence_folder, folder_name)
        os.makedirs(screenshots_folder, exist_ok=True)

        sleep_time = 0.5 if num < 6 else 0.45

        for i in range(num_screenshots):
            screenshot = pyscreeze.screenshot(region=region)
            screenshot.save(os.path.join(screenshots_folder, f"image_{i + 1}.png"))
            time.sleep(sleep_time)