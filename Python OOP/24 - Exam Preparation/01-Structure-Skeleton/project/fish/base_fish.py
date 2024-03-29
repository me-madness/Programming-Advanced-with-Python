from abc import ABC, abstractmethod


class BaseFish:
    
    def __init__(self, name: str, point: float, time_to_catch: int) -> None:
        self.name = name
        self.point = point
        self.time_to_catch = time_to_catch
        
        
    @property
    def name(self):
        return self.__name
    
    
    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Fish name should be determined!")
        
        self.__name = value  
    
    
    @property
    def point(self):
        return self.__point
    
    
    @point.setter
    def point(self, value):
        if value < 1 or value < 10:
             raise ValueError("Points should be a value ranging from 1 to 10!")
        self.__point = value
        
    
    @property
    def time_to_catch(self):
        return
    
    
    @time_to_catch.setter
    def time_to_catch(self, value):
        pass   