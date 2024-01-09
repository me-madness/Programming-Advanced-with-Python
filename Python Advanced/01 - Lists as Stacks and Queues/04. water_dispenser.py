# First task from the lecture
from collections import deque

name = input()
customers = deque()

while name != "End":
    if name == "Paid":
        pass
    else:
        customers.append(name)
    name = input()
    
    
    
# Second task from me