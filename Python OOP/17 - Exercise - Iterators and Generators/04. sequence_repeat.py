class sequence_repeat:
    
    def __init__(self, sequence: str, number: int) -> None:
        self.sequence = sequence
        self.number = number
        
        
    def __iter__(self):
        return self    


    def __next__(self):
        if self.idx == self.number -1:
            raise StopIteration
        
        self.idx += 1 
        
        return self.sequence[self.idx % len(self.sequence)]


# First input 
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

# Second input
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')