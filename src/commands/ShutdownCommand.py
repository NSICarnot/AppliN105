from src.commands.command_interface import Command

import os


class ShutdownCommand(Command):
    def __init__(self):
        super().__init__()

    def execute(self):
        try:
            os.system("shutdown /s /t 1")
        except Exception as e:
            print(f"Error while shutting down: {e}")