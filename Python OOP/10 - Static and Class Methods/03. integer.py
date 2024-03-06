class Integer:
    def __init__(self, value: int) -> None:
        self.value = value
        
    @classmethod    
    def from_float(cls, value: int):
        if not isinstance(value, float):
            return f"value is not a float"
    
        return cls(int(value))
    
    
    @classmethod
    def from_roman(cls, value: int):
        pass
    
    
    def from_string(cls, value: int):
        if not isinstance(value, str):
            return "wrong type"
        
        return cls(int(value))


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))        