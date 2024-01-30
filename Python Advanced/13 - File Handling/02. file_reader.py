# First task from the lecture

import os

path = os.path.join("resources", "numbers.txt")

file = open(path)

total_amount = 0
for line in file.readlines():
    total_amount += line
    
print(line)    

# Second task from me



