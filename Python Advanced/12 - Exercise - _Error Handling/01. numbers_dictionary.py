# First task from the lecture

numbers_dictionary = {}

line = input()

while line != "Search":
    numbers_as_string = line
    
    try:
        number = int(input())
        numbers_dictionary[numbers_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
        
    line = input()    
         

line = input()    

while line != "Remove":
    searched = line
    
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
    
    line = input()    
    
line = input()

while line != "End":
    searched = line
    
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
        
    line = input()
        
print(numbers_dictionary)        

# Second task from me



