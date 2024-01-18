# First task from the lecture

row = int(input())

flatten = []

for i in range(row):
    data = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    flatten.extend(data)
print(flatten)

# flatten = []

# for row in matrix:
#     for el in row:
#         flatten.append(el)
      
# print(flatten)

# Second task from me

