from abc import ABC, abstractmethod


class BasePeak(ABC):
    
    def __init__(self, name: str, elevation: int):
        self.name = name
        self.elevation = elevation
        self.difficulty_level = self.calculate_difficulty_level()
        
    @property
    def name(self):
        return 
    
    
    @name.setter
    def name(self, value):
        pass
    
    
    @property
    def elevation(self):
        return
    
    
    @elevation.setter
    def elevation(self, value):
        pass
    
    
    @abstractmethod
    def calculate_difficulty_level(self):
        pass