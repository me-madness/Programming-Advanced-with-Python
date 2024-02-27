class Person:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        
        
    def get_ful_name(self):
        return f"{self.first_name} {self.last_name}"
    

person = Person("Test", "Testov")    
print(person.first_name)    
print(person.last_name)    
print(person.get_ful_name)    