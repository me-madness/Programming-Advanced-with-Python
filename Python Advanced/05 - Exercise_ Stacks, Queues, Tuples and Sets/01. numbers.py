# First task from the lecture

first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

# First way from the lecture

for _ in range(int(input())):
    first_command, second_command, *data = input().split()  #"Add First 1 2 3" -> ["Add", "First", "1", "2", "3"]

    command = first_command + " " + second_command
    
    if command == "Add First":
        [first_set.add(int(el)) for el in data]
    elif command == "Add Second":
        [second_set.add(int(el)) for el in data]
    elif command == "Remove First":
        [first_set.discard(int(el)) for el in data]
    elif command == "Remove Second":
        [second_set.discard(int(el)) for el in data]
    elif command == "Check Subset":
        print(first_set.issubset(second_set) or second_set.issubset(first_set))
        
 
print(*sorted(first_set), sep=", ")        
print(*sorted(second_set), sep=", ")        

# Second way from the lecture

functions = {
    "Add First": lambda x: [first_set.add(int(el)) for el in x],
    "Add Second": lambda x: [second_set.add(int(el)) for el in x],
    "Remove First": lambda x: [first_set.discard(int(el)) for el in x],
    "remove Second": lambda x: [second_set.discard(int(el)) for el in x],
    "Check Subset": print(first_set.issubset(second_set) or second_set.issubset(first_set))
}





# Second task from me

