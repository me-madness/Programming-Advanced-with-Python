class Point:
    def __init__(self, _x: int, _y: int) -> None:
        self.x = _x
        self.y = _y
    
    
    def set_x(self):
        pass
    
    
    def set_y(self):
        pass
    
    
    def __str__(self) -> str:
        pass
    
    
p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)    