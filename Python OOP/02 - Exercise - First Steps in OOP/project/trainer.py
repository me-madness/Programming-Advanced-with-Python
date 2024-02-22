from typing import List
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.pokemons: List[Pokemon] = []
    
    
    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        
        self.pokomons.append(pokemon)
    
        return f"Caught {pokemon.pokemon_details()}"
    
    def release_pokemon(self, pokemon_name: str):
        ## Option 1 _> fast but long
        # pokemon = None
        
        # for p in self.pokemons:
        #     if p.name == pokemon_name:
        #         pokemon = p
        #         break
        
        
        ## Option 2 -> slow but short
        # try:
        #     pokemon = [p for p in self.pokemons if p.name == pokemon_name][0]
        # except IndexError:
        #     return "Pokemon is not caught"
        
        
        ## Option 3
        
        
        
        
        self.pokemons.remove(pokemon)    
    
        return f"Tou have released {pokemon_name}"
    
    
    def trainer_data(self):
        pass
    
    
pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())     