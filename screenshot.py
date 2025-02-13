import pyautogui
import base64
from io import BytesIO


def process_screenshot():
    screenshot = pyautogui.screenshot()
    cropped_image = screenshot.crop((8, 137, 1863, 1117))

    buffer = BytesIO()
    cropped_image.save(buffer, format="PNG")
    buffer.seek(0)

    base64_image = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return base64_image
