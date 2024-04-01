class HashTable:
    
    def __init__(self) -> None:
        self.__keys = [None, None, None, None]
        self.__values = [None, None, None, None]
        self.__length = 4
    
    
    def __setitem__(self, key, value):
        pass
        
        
    
table = HashTable()

table["name"] = "Peter"
table["age"] = 25

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))    