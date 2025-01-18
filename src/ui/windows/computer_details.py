from tkinter import ttk

import _tkinter
from customtkinter import CTk

class ComputerDetailScene:
    def __init__(self, ipaddr: str, logged_usr: str):
        self.root = CTk()
        self.root.geometry('600x600')
        self.root.resizable(False, False)
        self.root.title(f"Détails de l'ordinateur: {ipaddr} ({logged_usr})")

        self.ipaddr: str = ipaddr
        self.logged_usr: str = logged_usr

        self.build_interface()

    def build_interface(self):
        self.content = ttk.Frame(self.root)
        
        self.text = ttk.Label(self.content, text='Autre Scene', style='HeadTitle.TLabel')
        self.text.pack(side='top')

    def get_content(self):
        return self.content

    def mainloop(self):
        self.root.mainloop()

    # TODO: Régler le problème de la classe qui ne se supprime pas en mémoire et qui gaspille de la mémoire
    def terminate(self):
        try:
            if self.root.winfo_exists():
                self.root.destroy()
        except _tkinter.TclError:
            pass
        del self