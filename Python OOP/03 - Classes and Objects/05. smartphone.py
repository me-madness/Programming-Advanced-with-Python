class Smartphone:
    def __init__(self, memory) -> None:
        self.memory = memory
        self.apps = []
        self.is_on = False
    
    
    def power(self):
        if not self.is_on:
            self.is_on = True
        self.is_on = False    
    
    
    def power(self):
        pass
    
    
    def power(self):
        pass
    
    
smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())    