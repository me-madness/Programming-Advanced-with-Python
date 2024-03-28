from peaks.base_peak import BasePeak
from typing import List


class ArcticPeak(BasePeak):
    
    def get_recommended_gear(self) ->List[str]:
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]
    
    
    def calculate_difficulty_level(self):
        pass
    