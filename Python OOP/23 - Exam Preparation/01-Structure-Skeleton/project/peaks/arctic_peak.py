from peaks.base_peak import BasePeak
from typing import List


class ArcticPeak(BasePeak):
    
    def get_recommended_gear(self) ->List[str]:
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]
    
    
    def calculate_difficulty_level(self) -> str:
        if self.elevation > 3000:
            return "Extreme"
        elif 2000 <= self.elevation <= 3000:
            return "Advanced"
        
        
        