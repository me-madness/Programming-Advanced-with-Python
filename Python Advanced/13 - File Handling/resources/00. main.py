# First task - Create file 

import os

ABSOLUTE_DIR_PATH = os.path.abspath(__file__)
file_name = "text.txt"
path = os.path.join("resources", file_name)

try:
    file = open(file_name)
    print("File found")
except FileNotFoundError:
    print("File is not found")
    
# Second task - Reading file

file = open("my_example.txt")

print(file.read(2))
print(file.read(2))
print(file.read(5))

lines = file.readline()

for line in lines:
    print(line)

[print(line, end="") for line in lines]
        
# Third task - writing 

file = open("my_example.txt")

print(file.closed)

file.close()

print(file.closed)

# Forth task - writing

import os

path = os.path.join("my_example.txt")

with open(path) as file:
    lines = file.readlines()
    print(file.closed)
    
print(file.closed)    
