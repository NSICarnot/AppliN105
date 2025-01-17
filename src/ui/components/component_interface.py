from tkinter import ttk

class ComponentInterface:
    def __init__(self, root: ttk.Frame):
        self.root = root
        self.content: ttk.Frame = None
        
    def build_interface(self):
        pass
    
    def set_parent(self, parent):
        self.root = parent
        
    def get_content(self):
        return self.content