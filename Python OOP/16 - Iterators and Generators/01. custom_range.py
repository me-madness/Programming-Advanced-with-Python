class custom_range:
    def __init__(self, start, end) -> None:
        self.i = start
        self.n = end
        
        
    def __iter__(self):
      return self    
    