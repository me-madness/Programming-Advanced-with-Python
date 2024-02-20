class Phone:
    
    def __init__(self, color, size):
        self.color = color
        self.size = size
        
        
    def turn_on(self):
        return 'The phone is turned on'    
    

p1 = Phone("Green", 2)
p2 = Phone("Red", 12)   
print(p1.turn_on())


class Animal:
    def __init__(self, name):
        self.name = name
        
     
    def sleep(self):
        return 'sleeping'
    
    
animal = Animal("cat")     
print(animal.sleep())   