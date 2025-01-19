import config as c
import customtkinter as ctk

from customtkinter import CTk
from src.ui.scenes.scene_interface import SceneInterface
from src.ui.scenes.computers_scene import ComputersScene
from src.ui.scenes.control_scene import ControlScene
from src.helpers import image_helper as ih


class App():
    def __init__(self):
        self.root = CTk()
        self.root.title('Application N105 - Professeur')
        self.root.geometry('1200x900')
        self.root.resizable(False, False)
        
        self.scenes: list[SceneInterface] = [ComputersScene(self.root), ControlScene(self.root)]
        self.actual_scene: SceneInterface = self.scenes[0]
        
        c.init_styles()
        self.build_interface()
        
    def build_interface(self):        
        # Frame qui contient la toolbar d'une hauteur de 50px
        toolbar = ctk.CTkFrame(self.root, height=30, fg_color="red")
        toolbar.pack(side='top', fill='x')
        
        # Content de la toolbar
        # Frame qui contient la menubar à gauche de la fenêtre
        menubar = ctk.CTkFrame(self.root, width=500, fg_color="blue")
        menubar.pack(side='left', fill='y')
        
        # Content de la menubar
        # Bouton sous forme d'image qui affiche la scene affichant tous les ordinateurs connectées
        self.computer_img = ih.tk_CTkImage(
            ih.open_image('./res/img/computer.png'), 50, 50
        )  # Self pour garder trace de l'image dans la classe et pour ne pas la supprimer de la mémoire
        computers_button = ctk.CTkLabel(menubar, image=self.computer_img, text='', width=50, height=50)
        computers_button.pack(side='top')
        computers_button.bind("<Button-1>", lambda e: self.change_scene(self.scenes[0]))

        self.control_img = ih.tk_CTkImage(
            ih.open_image('./res/img/access-control.png'), 50, 50
        )
        control_button = ctk.CTkLabel(menubar, image=self.control_img, text='', width=50, height=50)
        control_button.pack(side='top')
        control_button.bind("<Button-1>", lambda e: self.change_scene(self.scenes[1]))
        
        # Frame qui contient le contenu de l'application
        # Content de l'application
        self.actual_scene.build_interface()
        self.actual_scene.get_content().pack(side='top', fill='both', expand=True)
        
    def change_scene(self, scene: SceneInterface):
        # Enlevier le contenu de la scène sans la détruire
        self.actual_scene.get_content().destroy()
        self.actual_scene = scene
        self.actual_scene.build_interface()
        self.actual_scene.get_content().pack(side='top', fill='both', expand=True)

    def mainloop(self):
        self.root.mainloop()

if __name__ == "__main__":
    try:
        app = App()
        app.mainloop()
    except Exception as e:
        print(e)
    finally:
        exit(0)