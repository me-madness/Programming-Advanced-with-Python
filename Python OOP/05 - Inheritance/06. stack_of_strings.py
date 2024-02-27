class Stack:
    def __init__(self) -> None:
        self.data = []
        
        
    def push(self, el):
        self.data.append()(el)   
    
    
    def pop(self):
        return self.data.pop() 
    
    
    def top(self):
        return self.data[-1] 
    
    
    def is_empty(self):
        return False if self.data else True
    
    
    def __str__(self) -> str:
        reversed_data = reversed(self.data)
        result = ", ".join(reversed_data)
        return f"[{result}]"
    
    
s = Stack()
print(s.is_empty)
s.push("5")    
s.push("6")
print(s.top)
s.push("7")    
print(s.top)

print(s.is_empty)
print(s)
s.pop()
print(s)