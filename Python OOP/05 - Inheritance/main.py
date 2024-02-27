class Person:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        
        
    def get_ful_name(self):
        return f"{self.first_name} {self.last_name}"


class Student(Person):
    def __init__(self, first_name: str, last_name: str, fac_number: int) -> None:
        super().__init__(first_name, last_name)
        # This is the same 
        # Person.__init__(self, first_name, last_name)
        self.fac_number = fac_number
    
    
    def go_to_school(self):
        return f"Walking to school"
    
    
    def display_info(self):
        return f"{self.get_ful_name()} with fac number {self.fac_number}"
    

person = Person("Test", "Testov", 213455)    
student = Student("Test", "Testov", 213455)    
print(person.first_name)    
print(person.last_name)    
print(person.get_ful_name) 
print(student.first_name)    
print(student.last_name)    
print(student.fac_number)    
print(student.get_ful_name)   
print(student.go_to_school)   
print(student.display_info)   