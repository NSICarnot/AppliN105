from tkinter import ttk
from customtkinter import CTk


class App():
    def __init__(self):
        self.root = CTk()
        self.root.title('Custom Tkinter')
        self.root.geometry('1200x900')
        
    def mainloop(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.mainloop()