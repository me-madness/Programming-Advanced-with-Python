def multiply(times):
    def decorator(function):
        pass
        
        return decorator    
    
    
# First input
@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))

# Second input
@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))    