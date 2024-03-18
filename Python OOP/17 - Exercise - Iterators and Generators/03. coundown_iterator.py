class countdown_iterator:
    
    def __init__(self) -> None:
        pass

    
    def __iter__(self):
        return self    
    
    
    def __next__(self):
        pass




# First input
iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

# Second input
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")