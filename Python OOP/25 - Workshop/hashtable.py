class HashTable:
    
    def __init__(self) -> None:
        self.array = [None, None, None, None]
    
    
    def __setitem__(self, key, value):
        pass
        
        
    
table = HashTable()

table["name"] = "Peter"
table["age"] = 25

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))    