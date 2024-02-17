def cookbook(*args):
    orders_list = {}
    for cuisine, country_name, ingredients in args:
        if country_name not in orders_list:
            orders_list[country_name] = []
        orders_list[country_name].append((cuisine, ingredients))

    sorted_orders = sorted(orders_list.keys(), key=lambda x: (len(orders_list[x]), x))

    for country_name in sorted_orders:
        recipes_in_cuisine = len(orders_list[country_name])
        print(f"  {country_name} cuisine contains {recipes_in_cuisine} recipes:")
        sorted_recipes = sorted(orders_list[country_name], key=lambda x: x[0])
        for recipe_name, ingredients in sorted_recipes:
            ingredient_list = ", ".join(ingredients)
            print(f"    * {recipe_name} -> Ingredients: {ingredient_list}")



print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
