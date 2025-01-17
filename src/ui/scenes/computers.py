import config as c

from tkinter import ttk
from src.ui.scenes.scene_interface import SceneInterface
from src.ui.components.computer_compo import ComputerComponent

class ComputersScene(SceneInterface):
    def __init__(self, root: "CTk"):
        super().__init__(root)
        
        self.computers: list[ComputerComponent] = []
        
    def build_interface(self):
        self.content = ttk.Frame(self.root)
        
        self.text = ttk.Label(self.content, text='Ordinateurs Connectées', style='HeadTitle.TLabel')
        self.text.grid(row=0, column=0, columnspan=4)
        
        self.computers = [ComputerComponent(self.content) for _ in range(12)]
        # Grid the elements and set the grid to space around each element
        for i, computer in enumerate(self.computers):
            computer.build_interface()
            computer.get_content().grid(row=i//4+1, column=i%4, padx=((1150)-250*4)//10, pady=20)
        
        
    def set_parent(self, parent):
        return super().set_parent(parent)

    def get_content(self):
        return self.content
