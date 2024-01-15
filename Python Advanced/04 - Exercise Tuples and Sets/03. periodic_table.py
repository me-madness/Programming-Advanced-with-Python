# First task from the lecture

table = set()

for _ in range(int(input)):
    for el in input().split():
        table.add(el)

print(*table, sep="\n")

# Second way from he lecture

print(*{el  for _ in range(int(input())) for el in input().split()}, sep="\n")

# Second task from me

