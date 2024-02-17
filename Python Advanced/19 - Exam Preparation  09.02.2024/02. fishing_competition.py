def get_next_position(position, direction_mapper, direction, matrix):
    current_row_index, current_col_index = position
    row_movement, col_movement = direction_mapper[direction]
    desired_row_index = current_row_index + row_movement
    desired_col_index = current_col_index + col_movement

    if 0 <= desired_row_index < len(matrix) and 0 <= desired_col_index < len(matrix):
        return desired_row_index, desired_col_index

    if desired_row_index < 0:
        desired_row_index = len(matrix) - 1
    elif desired_row_index >= len(matrix):
        desired_row_index = 0
        
    if desired_col_index < 0:
        desired_col_index = len(matrix) -1
    elif desired_col_index >= len(matrix):
        desired_col_index = 0
        
    return desired_row_index, desired_col_index            
            

n = int(input())

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

matrix = []
position = None

for row_index in range(n):
    data = list(input())
    
    if "S" in data:
        current_col = data.index("S")
        position = [row_index, current_col]
    matrix.append(data)    
    
command = input()

while command != "collect the nets":    
    next_row_index, next_col_index = get_next_position(position, direction_mapper, command, matrix)
    
    command = input()