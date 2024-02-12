# First task is from the lecture

from collections import deque

initial_fuel = [int(el) for el in input().split()]
additional_consumption_index = deque([int(el) for el in input().split()])
amount_of_fuel_needed = deque([int(el) for el in input().split()])

while initial_fuel and additional_consumption_index and amount_of_fuel_needed:
    fuel = initial_fuel[-1]
    index = additional_consumption_index[0]
    needed = amount_of_fuel_needed[0]

    if (fuel - index) >=  needed:
        initial_fuel.pop()
        additional_consumption_index.popleft()
        amount_of_fuel_needed.popleft()
    else:
        
        break    
        



# Second task is from me



