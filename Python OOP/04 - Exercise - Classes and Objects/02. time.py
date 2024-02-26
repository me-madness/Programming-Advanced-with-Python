class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59
    
    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        pass


    def set_time(self):
        pass
    
    
    def get_time(self):
        return f""
    
    
    def make_order(self):    
        return f"You've ordered pizza {pizza_name} prepared with {ingredient: quantity} and the price will be {price}lv."
        return f"Pizza {name} already prepared, and we can't make any changes!"



margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))