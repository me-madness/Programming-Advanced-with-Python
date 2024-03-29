from abc import ABC, abstractmethod
from fish.base_fish import BaseFish


class PredatoryFish(BaseFish):
    
    def __init__(self, name: str, points: float):
        self.name = name
        self.points = points