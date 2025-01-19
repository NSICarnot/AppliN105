import config as c
import customtkinter as ctk

from src.ui.scenes.scene_interface import SceneInterface

class ControlScene(SceneInterface):
    def __init__(self, root: "CTk"):
        super().__init__(root)

    def build_interface(self):
        self.content = ctk.CTkFrame(self.root)

        self.text = ctk.CTkLabel(self.content, text='Contrôle des ordinateurs', font=c.HEADTITLE_FONT)
        self.text.pack()

    def set_parent(self, parent):
        return super().set_parent(parent)

    def get_content(self):
        return self.content
