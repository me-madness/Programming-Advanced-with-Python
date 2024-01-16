# First task from the lecture

from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbol = deque(input().split())

functions = {
    "*": lambda a, b: a * b, 
    "/": lambda a, b: a / b if b != 0 else 0, 
    "*": lambda a, b: a * b, 
    "*": lambda a, b: a * b, 
}



while bees and nectar:
    curr_bee = bees.popleft()
    curr_nectar = nectar.pop()
    
    if curr_nectar < curr_bee:
        bees.appendleft(curr_bee)
    else:
        pass    


# Second task from me

