class Vet:
    animals: list[str] = []
    space: int = 5     #SPACE: int = 5
    
    def __init__(self,vet_name: str) -> None:
        self.name = vet_name
        self.animals: list[str] = []
        
        
    def register_animal(self, animal_name: str) -> str:
        if len(Vet.animals) == Vet.space:
            return f"Not enough space"
        
        self.animals.append(animal_name)
        Vet.animals.append(animal_name)
        
        return f"{animal_name} registered in the clinic"
    
    
    def unregister_animal(self, animal_name: str) -> str:
        if animal_name not in self.animals:
            return f"{animal_name} not in the clinic"
        
        self.animals.remove(animal_name)
        Vet.animals.remove(animal_name)
    
        return f"{animal_name} unregistered successfully"
    
    def info(self) -> str:
        pass
        return f"{self.name} has {len(self.animals)} animals. {Vet.space - len(Vet.animals)} space ;eft in vet."    