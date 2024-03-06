class Pizza:
    def __init__(self, ingredients: str) -> None:
        self.ingredients = ingredients
        
        
    @classmethod
    def pepperoni(cls):
        return cls(["tomato sauce", "parmesan", "pepperoni"])    
    
    
    @classmethod
    def quattro_formaggi(cls):
        return cls(["mozzarella", "gorgonzola", "fontina", "parmigiano"])
    
    
first_pizza = Pizza.pepperoni()    
second_pizza = Pizza.quattro_formaggi()    