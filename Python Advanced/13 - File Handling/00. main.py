# First task from the lecture

import os

file_name = "text.txt"
path = os.path.join("resources", file_name)
try:
    file = open(file_name)
    print("File found")
except FileNotFoundError:
    print("File is not found")
    
    
        

# Second task from me



