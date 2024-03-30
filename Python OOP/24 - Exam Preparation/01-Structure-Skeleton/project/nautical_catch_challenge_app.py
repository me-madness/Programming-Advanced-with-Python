from fish.base_fish import BaseFish
from divers.base_diver import BaseDiver
from divers.free_diver import FreeDiver
from divers.scuba_diver import ScubaDiver
from fish.deep_sea_fish import DeepSeaFish
from fish.predatory_fish import PredatoryFish

from typing import List


class NauticalCatchChallengeApp:
    divers_mapper = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    fish_mapper = {"DeepSeaFish": DeepSeaFish, "PredatoryFish": PredatoryFish}
    
    def __init__(self) -> None:
        self.divers: List[BaseDiver] = []
        self.fish: List[BaseFish] = []
        
        
    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.divers_mapper:  
            return f"{diver_type} is not allowed in our competition."
    
        try:
            diver = [d for d in self.divers if d.name == diver_name][0]
            return f"{diver.name} is already a participant."
        except IndexError:
            new_diver = self.divers_mapper[diver_type](diver_name)
            self.divers.append(new_diver)
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."
                
    
    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.fish_mapper:
            return f"{fish_type} is forbidden for chasing in our competition."
        
        try:
            fish = [f for f in self.fish if f.name == fish_name][0] 
            return f"{fish.name} is already permitted."
        except IndexError:
            
              
    
    
    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        pass