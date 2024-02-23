# First option

def cookbook(*recipes):
    cuisine_count = {}
    cuisine_recipes = {}
    for i in range(len(recipes)):
        recipe_name, cuisine, ingredients = recipes[i]
        if cuisine not in cuisine_count:
            cuisine_count[cuisine] = 1
            cuisine_recipes[cuisine] = [(recipe_name, ingredients)]
        else:
            cuisine_count[cuisine] += 1


# Second option

from collections import defaultdict

def cookbook(*recipes):
    cuisine_count = defaultdict(int)
    cuisine_recipes = defaultdict(list)
    for recipe_name, cuisine, ingredients in recipes:
        cuisine_count[cuisine] += 1
        cuisine_recipes[cuisine].append((recipe_name, ingredients))
        
        
print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))        