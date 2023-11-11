from PIL import Image
import pyautogui


class ComparisonHandling:
    def compare_sequence(self):
        # Open the template images
        up_template = Image.open('../Spy/ImageTemplates/up.png')
        down_template = Image.open('../Spy/ImageTemplates/down.png')
        left_template = Image.open('../Spy/ImageTemplates/left.png')
        right_template = Image.open('../Spy/ImageTemplates/right_new.png')

        # Open the first request image
        first_request = Image.open('../Spy/Image_1.png')

        result = pyautogui.locate(first_request, up_template, confidence=0.7)
        print(result)


# Example usage
comparator = ComparisonHandling()
comparator.compare_sequence()
