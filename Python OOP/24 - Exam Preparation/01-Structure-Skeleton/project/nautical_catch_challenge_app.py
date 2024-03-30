from fish.base_fish import BaseFish
from divers.base_diver import BaseDiver
from divers.free_diver import FreeDiver
from divers.scuba_diver import ScubaDiver

from typing import List


class NauticalCatchChallengeApp:
    divers_mapper = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    
    def __init__(self) -> None:
        self.divers: List[BaseDiver] = []
        self.fish: List[BaseFish] = []
        
        
    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.divers_mapper:  
            return f"{diver_type} is not allowed in our competition."
    
        try:
            diver = [d for d in self.divers if d.name == diver_name][0]
            return f"{diver_name} is already a participant."
        except IndexError:
                
    
    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        pass  
    
    
    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        pass