from src.server.command_handler import CommandHandler


class ApplicationEleve:
    def __init__(self):
        self.command_handler = CommandHandler()
        
        # Créer le web socket et se connecter au socket python de l'application professeur
        
    def run(self):
        while True:
            cmd = self.command_handler.listen("Entrée du socket")  # TODO: get input from socket
            if cmd:
                eval(f"from src.commands.{cmd} import {cmd}")  # import the command
                print(self.command_handler.perform_command(eval(f"{cmd}().execute()")))  # execute the command
            else:
                print("Commande inconnue")