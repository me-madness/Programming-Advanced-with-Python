# First task from the lecture

import os

def save_extensions(dir_name):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)    
    
directory = input()
extensions = {}    