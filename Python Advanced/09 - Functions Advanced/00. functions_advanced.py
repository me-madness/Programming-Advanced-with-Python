# Practice

def sum_nums(a, b , *args):
    total_sum = a + b
    for el in args:
        total_sum += el
    return total_sum


print(sum_nums( a = 5, b = 7))

# Practice

def sum_nums(a, b ):
    print(f"a is {a} and b is {b}")
    
    
sum_nums(a = 1, b = 2)    

# Practice

def greet_me(**kwargs):
    for key, value, in kwargs.items():
        print(f"{value}, {key}")
        
        
greet_me(a = 5, b = 6, c =7, d = 8,)     

# Practice Unpacking Dictionaries

def print_nums(a, b, c):
    print(a, b, c)


nums = [1, 2, 3]
a, b, c = nums
print_nums(*nums)

# Practice Unpacking Dictionaries

def some_func(name, age):
    print(f"{name} is {age} years old.")
    
    
person = {'age': 20, 'name': "Peter"}
some_func(person['name'], person['age'])
some_func(**person)   

# Practice Sorted Dictionary by Value

a = [10, 5, -3, 28]
people = {"Peter": 21, "George": 18, "John": 45}

print(sorted(a, reverse=True))    
print(sorted(people.items(), key=lambda kvp: kvp[0]))

# Practice Sorted Dictionary by Value

people = {"Peter": 21, "George": 18, "John": 45}

print(sorted(people.items(), key=lambda kvp: - kvp[0]))

# Practice Nested Functions

def factorial(number):
    if not isinstance(number, int) or number < 0:
        return f"Sorry. 'number' is incorrect."

    def inner_factorial(n):
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return inner_factorial(number)    
        
        
print(factorial(5))

# Practice Closures Example 

def greeting(name):
    pass

# Practice Recursion - Function Calling Itself

def factorial(number):
    if not isinstance(number, int) or number < 0:
        return f"Sorry. 'number' is incorrect."

    def inner_factorial(n):
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return inner_factorial(number)    


