# GeoGuessr Bot

A simple tool that captures a screenshot, crops a defined area, encodes it in Base64, and sends it to the OpenAI ChatGPT API to guess the geographic location.

## Features

- **PyQt5 GUI:** Minimal interface with a single button.
- **Screenshot & Crop:** Uses pyautogui and Pillow.
- **API Integration:** Sends the processed image to ChatGPT for location guessing.

## Usage
### 1. Set Up the API Key:
This bot requires an OpenAI API key to function. Set it as a Windows environment variable by running:

```setx OPENAI_API_KEY "your-api-key"```

Restart your system or open a new terminal for the changes to take effect.

### 2. Run the Application:
Simply launch the ```GeoGuessr Bot.exe``` file. Click the "Take Screenshot and Process" button, and the bot will capture a screenshot, process the image, and send it to the ChatGPT API for location estimation. The result will be displayed in the application window.

### 3. Troubleshooting:

- Ensure your API key is set correctly.
- Check your internet connection.
- If the application doesn’t start, try running it as an administrator.

## Requirements

- Python 3.6+
- [PyQt5](https://pypi.org/project/PyQt5/)
- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- [Pillow](https://pypi.org/project/Pillow/)
- [openai](https://pypi.org/project/openai/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/GeoGuessr-Bot.git
   cd GeoGuessr-Bot
2. (Optional) Create and activate a virtual environment:
   ```python -m venv venv
   source venv/bin/activate  # On Linux/macOS
   venv\Scripts\activate     # On Windows```
3. Install the dependencies:
   ```pip install -r requirements.txt```
## Usage

1. Update the OpenAI API key in the code.
2. Run the application:
   ```python main.py```
3. Click the "Take Screenshot and Process" button to capture the screen, process the image, and display the location guess.
