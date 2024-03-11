from abc import ABC

class Vehicle(ABC):
    def __init__(self, fuel_capacity: float, fuel_consumption: float) -> None:
        self.fuel_capacity = fuel_capacity
        self.fuel_consumption = fuel_consumption
        
        
    @abstractmethod
    def drive(self, distance: float):
        ...
        
    
    @abstractmethod    
    def refuel(self, fuel: float):
        pass    
            