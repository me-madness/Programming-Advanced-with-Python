# First task from the lecture

names_count = int(input())
names = set()

for _ in range(names_count):
    names.add(input())
    
print(*names, sep="\n")    


# Second way from the lecture

print(*{input() for _ in range(int(input()))}, sep="\n")

# Second task from me

