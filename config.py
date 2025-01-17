from tkinter import ttk


def init_styles():
    DEBUG_STYLE = ttk.Style()
    DEBUG_STYLE.configure("Debug.TLabel", background='yellow')
    
    TOOLBAR_STYLE = ttk.Style()
    TOOLBAR_STYLE.configure("ToolBarStyle.TFrame", background='red')
    
    SIDEBAR_STYLE = ttk.Style()
    SIDEBAR_STYLE.configure("SideBarStyle.TFrame", background='blue')
    
    HEADTITLE_STYLE = ttk.Style()
    HEADTITLE_STYLE.configure("HeadTitle.TLabel", padding=10, font=HEADTITLE_FONT)
    
    
HEADTITLE_FONT = ('Arial', 20, 'bold')
