# First task from the lecture

import os

def save_extensions(dir_name):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)    
    
        if os.path.isfile(file):
            extension = filename.split(".")[-1]   
    
            if extension not in extensions:
                extensions[extension] = []
                
                
            extensions[extension].append()(filename)
            
            extensions.get(extension, []) + [filename]
            
            
                
directory = input()
extensions = {}    