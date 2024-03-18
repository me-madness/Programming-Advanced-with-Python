class dictionary_iter:
    def __init__(self) -> None:
        pass

        



# First input
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

# Second input
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)