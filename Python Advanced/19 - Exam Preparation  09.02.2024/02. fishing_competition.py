n = int(input())

matrix = []

for row_index in range(n):
    data = list(input())
    
    if "S" in data:
        current_col = data.index("S")
        position = [row_index, current_col]
    matrix.append(data)    