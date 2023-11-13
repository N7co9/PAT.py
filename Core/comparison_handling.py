from PIL import Image
import pyautogui
from pyautogui import ImageNotFoundException


class ComparisonHandling:
    def compare_sequence(self):
        # Open the template images
        up_template = Image.open('C:\\Users\\root\\Documents\\PythonProjects\\Wizzard101-PetAutomationTool\\Spy\\ImageTemplates\\up.png')
        down_template = Image.open('C:\\Users\\root\\Documents\\PythonProjects\\Wizzard101-PetAutomationTool\\Spy\\ImageTemplates\\down.png')
        left_template = Image.open('C:\\Users\\root\\Documents\\PythonProjects\\Wizzard101-PetAutomationTool\\Spy\\ImageTemplates\\left.png')
        right_template = Image.open('C:\\Users\\root\\Documents\\PythonProjects\\Wizzard101-PetAutomationTool\\Spy\\ImageTemplates\\right.png')

        # Open the request images
        first_request = Image.open('C:\\Users\\root\\Documents\\PythonProjects\\Wizzard101-PetAutomationTool\\Image_1.png')
        second_request = Image.open('C:\\Users\\root\\Documents\\PythonProjects\\Wizzard101-PetAutomationTool\\Image_2.png')
        third_request = Image.open('C:\\Users\\root\\Documents\\PythonProjects\\Wizzard101-PetAutomationTool\\Image_3.png')

        # Define a list of request images for easier iteration
        request_images = [first_request, second_request, third_request]

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
                    location = pyautogui.locate(request_image, template, confidence=0.9)
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