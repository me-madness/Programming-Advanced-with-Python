def cookbook(*args):
    orders_list = {}
    for cuisine, country_name, ingredients in args:
        if country_name not in orders_list:
            orders_list[country_name] = []
        orders_list[country_name].append((cuisine, ingredients))

    result = ""
    
    sorted_order_list = sorted(orders_list.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for country, cuisine_two in sorted_order_list:
        cuisine_count = len(cuisine_two) 
        result += f"{country} cuisine contains {cuisine_count} recipes:\n"
        sorted_recipes = sorted(orders_list[country], key=lambda kvp: (-len(kvp[1]), kvp[0]))
        for cuisine_name, ingredients_name in sorted_recipes:
            result += f" * {cuisine_name} -> Ingredients: {', '.join(el for el in ingredients_name)}\n"
    return result

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))

# print(cookbook(
#     ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
#     ))


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
