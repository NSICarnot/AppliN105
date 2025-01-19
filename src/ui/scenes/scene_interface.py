import customtkinter as ctk
from customtkinter import CTk

# Classe Interface qui crée une Frame qui contient le contenu de l'application
class SceneInterface:
    def __init__(self, root: CTk):
        self.root = root
        self.content: ctk.CTkFrame = None
        
    def build_interface(self):
        pass
    
    def set_parent(self, parent):
        self.root = parent
        
    def get_content(self):
        return self.content