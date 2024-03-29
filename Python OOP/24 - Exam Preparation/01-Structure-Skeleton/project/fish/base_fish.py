from abc import ABC, abstractmethod


class BaseFish:
    
    def __init__(self, name: str, point: float, time_to_catch: int) -> None:
        self.name = name
        self.point = point
        self.time_to_catch = time_to_catch