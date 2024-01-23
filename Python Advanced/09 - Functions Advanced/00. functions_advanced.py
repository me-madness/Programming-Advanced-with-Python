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

# Practice Unpacking Dictionary

def print_nums(a, b, c):
    print(a, b, c)


nums = [1, 2, 3]
a, b, c = nums
print_nums(*nums)

# Practice

def some_func(name, age):
    print(f"{name} is {age} years old.")
    
    
person = {'age': 20, 'name': "Peter"}
some_func(person['name'], person['age'])
some_func(**person)       