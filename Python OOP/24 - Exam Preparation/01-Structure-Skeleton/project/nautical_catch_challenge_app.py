from fish.base_fish import BaseFish
from divers.base_diver import BaseDiver
from divers.free_diver import FreeDiver

from typing import List


class NauticalCatchChallengeApp:
    divers_mapper = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    
    def __init__(self) -> None:
        self.divers: List[BaseDiver] = []
        self.fish: List[BaseFish] = []
        
        
    def dive_into_competition(diver_type: str, diver_name: str):
        pass  
    
    
    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        pass  