class Shape:
    def calculate_area(self):
        pass
    
    
    
class Circle(Shape):
    def calculate_area(self):
        print("Calculating area of a circle") 
        
        
class Triangle:
    def calculate_area(self):
        print("Calculating area of a triangle") 
                 

class Square:
    def calculate_area(self):
        print("Calculating area of a square")
        
                         
shapes = [Triangle(), Circle(), Circle(), Triangle(), Square()]       

for s in shapes:
    s.calculate_area()          