class Flower:
    def __init__(self, name: str, water_requirements: int, is_happy: False) -> None:
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = is_happy
    
    
    def water(self):
        pass
    
    
    def status(self):
        pass

    
flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())    