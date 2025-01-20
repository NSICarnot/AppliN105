class Command:
    def __init__(self):
        self.command: str = self.__class__.__name__
        
    def execute(self):
        pass
    
    def __repr__(self):
        return self.command