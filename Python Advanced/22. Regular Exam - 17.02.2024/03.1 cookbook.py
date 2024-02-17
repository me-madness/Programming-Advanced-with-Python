def cookbook(*recipes):
    # Organize recipes by cuisine
    cuisine_dict = {}
    for recipe in recipes:
        name, cuisine, ingredients = recipe
        if cuisine not in cuisine_dict:
            cuisine_dict[cuisine] = []
        cuisine_dict[cuisine].append((name, ingredients))

    # Sort cuisines by the number of recipes and alphabetically
    sorted_cuisines = sorted(cuisine_dict.keys(), key=lambda x: (len(cuisine_dict[x]), x))

    # Print the output
    for cuisine in sorted_cuisines:
        recipes_in_cuisine = len(cuisine_dict[cuisine])
        print(f"  {cuisine} cuisine contains {recipes_in_cuisine} recipes:")
        sorted_recipes = sorted(cuisine_dict[cuisine], key=lambda x: x[0])
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