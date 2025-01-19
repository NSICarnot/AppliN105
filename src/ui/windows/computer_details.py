import _tkinter
import src.helpers.image_helper as ih
import customtkinter as ctk

from customtkinter import CTk
from PIL import Image, ImageTk

class ComputerDetailScene:
    def __init__(self, ipaddr: str, logged_usr: str):
        self.root = CTk()
        self.root.geometry('800x800')
        self.root.resizable(False, False)
        self.root.title(f"Détails de l'ordinateur: {ipaddr} ({logged_usr})")

        self.ipaddr: str = ipaddr
        self.logged_usr: str = logged_usr

        self.build_interface()

    def build_interface(self):
        self.content = ctk.CTkFrame(self.root)
        self.content.pack()

        self.details_dict = {
            'Adresse IP': self.ipaddr,
            'Utilisateur connecté': self.logged_usr,
            'Système d\'exploitation': 'Kali Linux',
            'Version': '2021.1',
            'Architecture': '64 bits',
            'RAM': '8 Go',
            'Processeur': 'Intel Core i5-8250U',
            'Stockage': '256 Go SSD',
            'Carte graphique': 'Intel UHD Graphics 620',
            'Résolution': '1920x1080',
            'Audio': 'Haut-parleurs stéréo',
            'Clavier': 'AZERTY',
        }

        for i, (key, value) in enumerate(self.details_dict.items()):
            ctk.CTkLabel(self.content, text=key).grid(row=i+1, column=0, sticky='w')
            ctk.CTkLabel(self.content, text=value).grid(row=i+1, column=1, sticky='w')

        img = ih.resize_image("./res/img/kali-desktop-xfce.jpg", 500, 300)
        self.image = ImageTk.PhotoImage(img, master=self.content)  # Reset master to avoid garbage collector to delete the image
        self.screen_image = ctk.CTkLabel(self.content, image=self.image)
        self.screen_image.grid(row=100, column=0, columnspan=4)

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