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