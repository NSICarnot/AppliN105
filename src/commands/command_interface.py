class Command:
    def __init__(self):
        self.command: str = self.__class__.__name__
        
    def execute(self):
        """
        Abstract method that the child classes must implement
        :return:
        """
        pass
    
    def __repr__(self):
        return self.command