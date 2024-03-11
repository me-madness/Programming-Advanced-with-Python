from abc import ABC
import abc

class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        
        
    @abc.abstractmethod
    def drive(self, distance: float) -> None:
        ...
        
    
    @abc.abstractmethod    
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
            
            
    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * self.TANK_PERCENTAGE_FILL      
        
        
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)        