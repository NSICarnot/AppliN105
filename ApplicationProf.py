from tkinter import ttk
from customtkinter import CTk


class App():
    def __init__(self):
        self.root = CTk()
        self.root.title('Application N105 - Professeur')
        self.root.geometry('1200x900')
        self.root.resizable(False, False)
        
        self.build_interface()
        
    def build_interface(self):
        toolbar_style = ttk.Style()
        toolbar_style.configure("ToolBarStyle.TFrame", background='red')
        sidebar_style = ttk.Style()
        sidebar_style.configure("SideBarStyle.TFrame", background='blue')
        
        # Frame qui contient la toolbar d'une hauteur de 50px
        toolbar = ttk.Frame(self.root, height=30, style="ToolBarStyle.TFrame")
        toolbar.pack(side='top', fill='x')
        
        # Content de la toolbar
        
        # Frame qui contient la menubar à gauche de la fenêtre
        menubar = ttk.Frame(self.root, width=50, style="SideBarStyle.TFrame")
        menubar.pack(side='left', fill='y')
        
        # Content de la menubar
        
        # Frame qui contient le contenu de l'application
        content = ttk.Frame(self.root)
        content.pack(side='right', fill='both', expand=True)
        
        # Content de l'application
    
    def mainloop(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.mainloop()