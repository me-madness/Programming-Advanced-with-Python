# First task from the lecture

row_count = int(input())

matrix = []

for i in range(row_count):
    data = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(data)

print(matrix)

# even_matrix = []

# for row in matrix:
#     sub_list = []
#     for el in row:
#         if el % 2 == 0:
#             sub_list.append(el)
#     even_matrix.append(sub_list)
    
    
# print(even_matrix)
    
# Second task from me

