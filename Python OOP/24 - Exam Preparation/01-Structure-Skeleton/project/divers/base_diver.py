from abc import ABC, abstractmethod


class BaseDiver:
    
    def __init__(self, name: str, oxygen_level: float) -> None:
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: list = []
        
        
    @property
    def name(self):
        return self.__name
    
    
    @name.setter
    def name(self, value) :
        if value.strip() == "":
            raise ValueError("Diver name cannot be null or empty!")           
        self.__name = value
        
        
    @property
    def oxygen_level(self):
        return self.__oxygen_level
    
    
    @oxygen_level.setter
    def oxygen_level(self, value) :
        pass           
        self.__oxygen_level = value
        
        
            
    