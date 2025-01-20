import config as c

from src.commands.command_interface import Command


class CommandHandler:
    def __init__(self):
        self.commands = c.COMMANDS
        
    def listen(self, cmd: str):
        if cmd in self.commands:
            return self.commands[cmd]
        else:
            return None
        
    def perform_command(self, cmd: Command):
        return cmd.execute() 