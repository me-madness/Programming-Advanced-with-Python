# First task from the lecture
# [[0, 0], [0, 0], [0, 0]] -> Output

matrix = []

for i in range(0, 3):
    sub_list = []
    for j in range(0, 2):
        sub_list.append(0)
    matrix.append(sub_list)
    
print(matrix)    

# One line List Comprehensions 

matrix = [[0 for j in range(2)] for i in range(3)]

# Second way from SoftUni
# [[0, 0], [0, 0], [0, 0]] -> Output

matrix = []
for i in range(3):
    sub_list = []
    for j in range(2):
        matrix[i].append(0) 
        
        
print(matrix)    

# Same task another output
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]] -> Output 
 
matrix = []
for i in range(3):
    matrix.append([])
    for j in range(1, 4):
        sub_list.append(j) 
    matrix.append(sub_list)
    
print(matrix)  

# One line List Comprehensions 

matrix = [[j for j in range(1, 4) for i in range(3)]]