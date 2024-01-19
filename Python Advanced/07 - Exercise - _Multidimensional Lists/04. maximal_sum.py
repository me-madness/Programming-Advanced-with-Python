# First task from the lecture

rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)] 


max_sum = float("-inf")
biggest_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first_row = matrix[row][col:col + 3]
        second_row = matrix[row][col:col + 3]
        third_row = matrix[row][col:col + 3]



# Second task from me

