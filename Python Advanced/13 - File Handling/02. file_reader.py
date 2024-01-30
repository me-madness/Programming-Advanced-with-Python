# First task from the lecture

file = open("my_example.txt")

print(file.read(2))
print(file.read(2))
print(file.read(5))
lines = file.readline()
for line in lines:
    print(line)

[print(line, end="") for line in lines]

# Second task from me



