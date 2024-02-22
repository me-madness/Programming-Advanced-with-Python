class Employee:
    def __init__(self, _id: int, first_name: str, last_name: str, salary: float) -> None:
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary


    def get_full_name(self, first_name, last_name):
        pass


    def get_annual_salary(self):
        pass
    
    
    def raise_salary(self):
        pass    

employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())
