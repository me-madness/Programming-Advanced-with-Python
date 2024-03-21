def cache(func):
    def wrapper(num):
        if not wrapper.log.get(num):
            wrapper.log[num] = func(num)

        return wrapper.log[num]

    wrapper.log = {}


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

# First Input    
fibonacci(3)
print(fibonacci.log)

# Second Input  
fibonacci(4)
print(fibonacci.log) 