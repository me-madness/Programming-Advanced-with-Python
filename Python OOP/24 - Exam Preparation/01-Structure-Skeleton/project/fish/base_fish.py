from abc import ABC, abstractmethod


class BaseFish:
    
    def __init__(self, name: str, point: float, time_to_catch: int) -> None:
        self.name = name
        self.point = point
        self.time_to_catch = time_to_catch
        
        
    @property
    def name(self):
        return
    
    
    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Fish name should be determined!")
        
        self.__name = value  
    
    
    @property
    def point(self):
        pass
    
    
    @point.setter
    def point(self, value):
        pass 
    
    
    @property
    def time_to_catch(self):
        pass
    
    
    @time_to_catch.setter
    def time_to_catch(self, value):
        pass   