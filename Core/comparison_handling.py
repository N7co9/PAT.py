import os
import re
from pyautogui import ImageNotFoundException
from PIL import Image
import pyautogui

class ComparisonHandling:

    def compare_sequence(self):
        # Open the template images
        up_template = Image.open('Spy\\ImageTemplates\\up.png')
        down_template = Image.open('Spy\\ImageTemplates\\down.png')
        left_template = Image.open('Spy\\ImageTemplates\\left.png')
        right_template = Image.open('Spy\\ImageTemplates\\right.png')

        # Define the naming pattern for request images
        pattern = re.compile(r'image_(\d+)\.png')

        # Get a list of files in the root directory
        root_files = os.listdir()

        # Filter files based on the naming pattern
        request_images = [Image.open(file) for file in root_files if pattern.match(file)]

        # Define a list of templates for easier iteration
        templates = [up_template, down_template, left_template, right_template]

        # Initialize an empty list to store the results
        results = []

        # Iterate through each request image
        for request_index, request_image in enumerate(request_images):
            # Initialize the result string for the current request
            result_for_request = "Unknown"

            # Iterate through each template
            for template_index, template in enumerate(templates):
                try:
                    # Locate the template within the current request image
                    location = pyautogui.locate(request_image, template, confidence=0.91)
                    # If the template is found, set the result for the current request
                    if location:
                        result_for_request = ['Up', 'Down', 'Left', 'Right'][template_index]
                        break  # Break out of the inner loop once a match is found
                except ImageNotFoundException:
                    # Handle the case when the template is not found
                    pass

            # Append the result for the current request to the results list
            results.append(result_for_request)

        # Return the list of results
        return results
