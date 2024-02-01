# First task from the lecture

import os



def save_extensions(dir_name):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)    
    
        if os.path.isfile(file):
            extension = filename.split(".")[-1]   
            extensions[extension] = extensions.get(extension, []) + [filename]
        elif os.path.isdir(file):
            save_extensions(file)    
            
            
                
directory = input()
extensions = {} 
save_extensions(directory)
print(extensions)   