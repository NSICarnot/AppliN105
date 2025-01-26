import config as c

from src.commands.command_interface import Command
import asyncio


class CommandHandler:
    """
    CommandHandler class that listens to commands and performs them
    """
    def __init__(self):
        self.commands = c.COMMANDS

        # TODO: Listen to the server for commands asynchronously
        
    async def listen(self, cmd: str):
        """
        Function taking a command and executing it if it exists
        :param cmd: Command name
        :return:
        """
        if cmd in self.commands:
            await self.perform_command(self.commands[cmd])

    async def perform_command(self, cmd: Command):
        """
        Function that executes a command
        :param cmd: Command object
        :return:
        """
        return cmd.execute()