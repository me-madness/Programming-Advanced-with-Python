from abc import ABC

class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        
        
    @abstractmethod
    def drive(self, distance: float) -> None:
        pass
        
    
    @abstractmethod    
    def refuel(self, fuel: float) -> None:
        pass    
            
            
class Car(Vehicle):
    CONDITIONER_ON: float = 0.9
    
    
    def drive(self, distance: float):
        consumption = (self.CONDITIONER_ON + self.fuel_consumption) * distance
        
        if self.fuel_quantity > consumption:
            self.fuel_quantity -= consumption


    def refuel(self, fuel: float):
        self.fuel_quantity += fuel
        

class Truck(Vehicle):
    CONDITIONER_ON: float = 1.6
    TANK_PERCENTAGE_FILL: float = 0.95
    
    
    def drive(self, distance: float):
        consumption = (self.CONDITIONER_ON + self.fuel_consumption) * distance
        
        if self.fuel_quantity > consumption:
            self.fuel_quantity -= consumption