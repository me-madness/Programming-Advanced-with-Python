class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        
        
    def __repr__(self) -> str:
        return f"{self.name} {self.surname}"    
    
    
    def __add__(self, other):
        return Person(self.name, other.surname)
    
    
class Group:
    def __init__(self, name: str, people: list[Person]):
      self.name = name
      self.people = people  
      
      
    def __len__(self):
        return len(self.people)  