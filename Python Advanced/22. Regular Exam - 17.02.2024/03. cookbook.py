def cookbook(*args):
    orders_list = {}
    for cuisine, country_name, ingredients in args:
        if country_name not in orders_list:
            orders_list[country_name] = []
        orders_list[country_name].append((cuisine, ingredients))
    print(orders_list)







print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
