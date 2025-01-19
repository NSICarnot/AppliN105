import customtkinter as ctk

class ComponentInterface:
    def __init__(self, root: ctk.CTkFrame):
        self.root = root
        self.content: ctk.CTkFrame = None
        
    def build_interface(self):
        pass
    
    def set_parent(self, parent):
        self.root = parent
        
    def get_content(self):
        return self.content