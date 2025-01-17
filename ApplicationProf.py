import config as c

from tkinter import ttk
from customtkinter import CTk
from src.ui.scenes.scene_interface import SceneInterface
from src.ui.scenes.computers import ComputersScene
from src.ui.scenes.other import OtherScene


class App():
    def __init__(self):
        self.root = CTk()
        self.root.title('Application N105 - Professeur')
        self.root.geometry('1200x900')
        self.root.resizable(False, False)
        
        self.scenes: list[SceneInterface] = [ComputersScene(self.root), OtherScene(self.root)]
        self.actual_scene: SceneInterface = self.scenes[0]
        
        c.init_styles()
        self.build_interface()
        
    def build_interface(self):        
        # Frame qui contient la toolbar d'une hauteur de 50px
        toolbar = ttk.Frame(self.root, height=30, style="ToolBarStyle.TFrame")
        toolbar.pack(side='top', fill='x')
        
        # Content de la toolbar
        # Frame qui contient la menubar à gauche de la fenêtre
        menubar = ttk.Frame(self.root, width=50, style="SideBarStyle.TFrame")
        menubar.pack(side='left', fill='y')
        
        # Content de la menubar
        # Bouton sous forme d'image qui affiche la scene affichant tous les ordinateurs connectées
        computers_button = ttk.Button(menubar, text='Ord.', command=lambda: self.change_scene(self.scenes[0]), width=5)
        computers_button.pack(side='top', fill='x')
        
        other_button = ttk.Button(menubar, text='Oth.', command=lambda: self.change_scene(self.scenes[1]), width=5)
        other_button.pack(side='top', fill='x')
        
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
    app = App()
    app.mainloop()