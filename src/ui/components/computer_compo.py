from PIL import ImageTk, Image
from tkinter import ttk
from src.ui.components.component_interface import ComponentInterface
from src.ui.windows.computer_details import ComputerDetailScene


class ComputerComponent(ComponentInterface):
    def __init__(self, root: ttk.Frame):
        super().__init__(root)

        self.ip_addr: str = "172.16.105.1"
        self.logged_usr: str = "user.name"

        self.details_window: ComputerDetailScene | None = None
        
    def build_interface(self):
        # Frame de très petite taille
        self.content = ttk.Frame(self.root, width=250, height=200)
        
        self.text = ttk.Label(self.content, text=f'{self.ip_addr}  ({self.logged_usr})')
        self.text.pack(side='top')
        
        # adding the image in ./res/img/kali-desktop-xfce.jpg to the frame and resized to the size of 25x15
        img = Image.open('./res/img/kali-desktop-xfce.jpg')
        img.thumbnail((250, 150))
        self.image = ImageTk.PhotoImage(img)
        self.screen_image = ttk.Label(self.content, image=self.image)
        self.screen_image.pack(side='top')

    def show_details(self) -> None:
        if isinstance(self.details_window, ComputerDetailScene): self.details_window.terminate()
        self.details_window = ComputerDetailScene(self.ip_addr, self.logged_usr)
        self.details_window.mainloop()
        self.details_window = None
        
    def set_parent(self, parent):
        return super().set_parent(parent)

    def get_content(self):
        return self.content