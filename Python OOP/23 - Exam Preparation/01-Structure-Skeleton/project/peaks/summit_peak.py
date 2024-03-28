from peaks.base_peak import BasePeak
from typing import List


class SummitPeak(BasePeak):
    
    def get_recommended_gear(self) ->List[str]:
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]
    
    
    def calculate_difficulty_level(self) -> str:
        if self.elevation > 2500:
            return "Extreme"
        elif 1500 <= self.elevation <= 2500:
            return "Advanced"     