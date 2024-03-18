class sequence_repeat:
    
    def __init__(self, sequance: int, number: int) -> None:
        self.sequance = sequance
        self.number = number
        
        
    def __iter__(self):
        return self    



    def __next__(self):
        if self.
            raise StopIteration
        
        self.
        
        return self.


# First input 
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

# Second input
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')