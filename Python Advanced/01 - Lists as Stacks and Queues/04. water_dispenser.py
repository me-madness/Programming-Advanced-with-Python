# First task from the lecture

from collections import deque

water = int(input())

name = input()
people = deque()


while name != "Start":
    people.append()    
    name = input()

command = input()

while command != "End":
    data = command.split()
    if len(data) == 1:
        liters_requested = int(data[0])
        person = people.popleft()
        
        
        if water >= liters_requested:
            print(f"{person} got water")
            water -= liters_requested
        else:
            print(f"{person} must wait")
            
    elif len(data) == 2:
        _, liters_to_add = data            
            
            
            
# Second task from me