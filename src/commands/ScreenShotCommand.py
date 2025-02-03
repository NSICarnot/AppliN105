from src.commands.command_interface import Command
from PIL import ImageGrab

import os

class ScreenShotCommand(Command):
    def __init__(self):
        super().__init__()

    def execute(self):
        screenshot = None

        try:
            screenshot = ImageGrab.grab()
            if os.path.exists("./out/screenshots") is False:
                os.makedirs("./out/screenshots")
            screenshot.save("./out/screenshots/screenshot.png")
        except Exception as e:
            print(f"Error while taking screenshot: {e}")
        finally:
            return screenshot


if __name__ == "__main__":
    ScreenShotCommand().execute()
