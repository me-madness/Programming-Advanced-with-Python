from abc import ABC, abstractmethod
from typing import List

from fish.base_fish import BaseFish


class BaseDiver:
    
    def __init__(self, name: str, oxygen_level: float) -> None:
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: List[BaseFish] = []
        
        
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
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")           
        self.__oxygen_level = value
        
        
            
    