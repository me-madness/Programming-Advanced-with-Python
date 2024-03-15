class reverse_iter:
    def __init__(self, iterable) -> None:
        self.iterable = iterable
        self.i = len(self.iterable)
    
    
    def __iter__(self):
        return self
    
    
    def __next__(self):
        i = self.i
        self.i += 1
        return i
    
    
reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)    