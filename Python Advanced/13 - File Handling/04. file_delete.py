# First task from the lecture
# First option

import os

path = os.path.join("resources", "numbers.txt")

try:
    os.remove(path)
except FileNotFoundError:
    print("The file is already deleted")
    
# Second option
        
if os.path.exists(path):
    os.remove(path)
else:
    print("The file is already deleted")
    
# Second task from me



