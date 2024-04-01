class HashTable:
    
    def __init__(self) -> None:
        self.__keys = [None, None, None, None]
        self.__values = [None, None, None, None]
        self.__length = 4
    
    
    def __setitem__(self, key, value):
        index = self.hash(key)
        if self.__keys[index] is not None:
            pass
        self.__keys[index] = key
        self.__values[index] = value
        
        
    def __find_index(self, index):
        if self.__keys[index] is None:
            return index    
        
        
    def hash(self, key: str) -> int:
        return sum([ord(el) for el in key]) % self.__length    
    
table = HashTable()

table["name"] = "Peter"
table["age"] = 25

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))    