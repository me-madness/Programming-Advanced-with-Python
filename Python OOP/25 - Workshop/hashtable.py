class HashTable:
    
    def __init__(self) -> None:
        self.__keys = [None, None, None, None]
        self.__values = [None, None, None, None]
        self.__length = 4
    
    
    def __len__(self):
        return len([el for el in self.__key if el is not None])
    
    
    def __setitem__(self, key, value):
        if self.__len__() == self.__length:
            # Resize the lists, so that the new value
            self.__resize()
        index = self.__find_index(self.hash(key))
        self.__keys[index] = key
        self.__values[index] = value
        
        
    def __find_index(self, index):
        if index == self.__length:
            index = 0
        if self.__keys[index] is None:
            return index    
        return self.__find_index(index + 1)
        
    def hash(self, key: str) -> int:
        return sum([ord(el) for el in key]) % self.__length 
    
    
    def __resize(self):
        self.__keys = self.__keys + [None] * self.__length
        self.__values = self.__values + [None] * self.__length
        self.__length *= 2   
    
table = HashTable()

table["name"] = "Peter"
table["age"] = 25

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))    