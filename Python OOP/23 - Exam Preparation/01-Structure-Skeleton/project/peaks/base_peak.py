from abc import ABC, abstractmethod


class BasePeak(ABC):
    
    def __init__(self, name: str, elevation: int):
        self.name = name
        self.elevation = elevation
        
        
    @property
    def name(self):
        return 
    
    
    @name.setter
    def name(self, value):
        pass