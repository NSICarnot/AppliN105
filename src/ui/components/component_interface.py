import customtkinter as ctk

class ComponentInterface:
    """
    Abstract class that defines the methods that the child classes must implement
    """
    def __init__(self, root: ctk.CTkFrame):
        """
        Constructor of the SceneInterface class
        :param root: Root frame
        """
        self.root = root
        self.content: ctk.CTkFrame = None
        
    def build_interface(self):
        """
        Abstract method that the child classes must implement
        :return:
        """
        pass
    
    def set_parent(self, parent):
        """
        Set the parent of the scene
        :param parent: Parent frame
        :return:
        """
        self.root = parent
        
    def get_content(self):
        """
        Get the content of the scene
        :return:
        """
        return self.content