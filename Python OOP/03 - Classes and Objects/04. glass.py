class Glass:
    def __init__(self) -> None:
        self.content = 0
    
    
    def fill(self):
        pass


    def empty(self):
        return f"Glass is now empty"
    
    
    def info(self):
        pass
    

glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())    