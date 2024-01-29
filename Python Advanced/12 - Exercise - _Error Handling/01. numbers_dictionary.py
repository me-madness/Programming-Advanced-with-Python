# First task from the lecture

numbers_dictionary = {}

line = input()

while line != "Search":
    numbers_as_string = line
    number = int(input())
    numbers_dictionary[numbers_as_string] = number
    
line = input()    

while line != "Remove":
    searched = line
    print(numbers_dictionary[searched])
    
line = input()

while line != "End":
    searched = line
    del numbers_dictionary[searched]
    
print(numbers_dictionary)        


# Second task from me



