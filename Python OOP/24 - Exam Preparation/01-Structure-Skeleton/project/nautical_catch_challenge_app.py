from fish.base_fish import BaseFish
from divers.base_diver import BaseDiver
from divers.free_diver import FreeDivers

from typing import List


class NauticalCatchChallengeApp:
    
    def __init__(self) -> None:
        self.divers: List[BaseDiver] = []
        self.fish: List[BaseFish] = []
        
        
    def dive_into_competition(diver_type: str, diver_name: str):
        pass    