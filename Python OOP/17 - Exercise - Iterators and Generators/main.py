class MyList:
    
    def __init__(self, my_list: list) -> None:
        self.my_list = my_list


    def __iter__(self):
        return self
    
    
    def __next__(self):
      x = self.a
      self.a += 1
      return x





# for loop in python

iterator = MyList([1, 2, 3]).__iter__()

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
    
    
def numbers_multiplied_by_two(numbers: list):
    for number in numbers:
        yield number * 2
        
        
a = (number * 2 for number in [1, 2, 3])
print(next(a))                
print(next(a))                