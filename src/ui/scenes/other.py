import config as c

from tkinter import ttk 
from src.ui.scenes.scene_interface import SceneInterface

class OtherScene(SceneInterface):
    def __init__(self, root: "CTk"):
        super().__init__(root)
        
    def build_interface(self):
        self.content = ttk.Frame(self.root)
        
        self.text = ttk.Label(self.content, text='Autre Scene', style='HeadTitle.TLabel')
        self.text.pack(side='top')
        
    def set_parent(self, parent):
        return super().set_parent(parent)

    def get_content(self):
        return self.content