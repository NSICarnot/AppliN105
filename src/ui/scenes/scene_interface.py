from typing import Union

import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkScrollableFrame


class SceneInterface:
    """
    Abstract class that defines the methods that the child classes must implement
    """
    def __init__(self, root: CTk):
        """
        Constructor of the SceneInterface class
        :param root:
        """
        self.root = root
        self.content: ctk.CTkFrame = None
        
    def build_interface(self):
        """
        Abstract method that the child classes must implement
        :return:
        """
        pass
    
    def set_parent(self, parent: CTkFrame | CTkScrollableFrame):
        """
        Set the parent of the scene
        :param parent:
        :return:
        """
        self.root = parent
        
    def get_content(self):
        """
        Get the content of the scene
        :return:
        """
        return self.content