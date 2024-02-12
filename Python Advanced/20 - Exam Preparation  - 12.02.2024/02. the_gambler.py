# First task is from the lecture

def is_in_boundaries(row_index, col_index, n):
    return 0 <= row_index < n and 0 <=col_index < n:






direction_maper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

n  = int(input())

board = []
player_position = None

for row_index in range(n):
    data = list(input())
    
    if "G" in data:
        col_index = data.index("G")
        player_position = [row_index, col_index]
    board.append(data)


direction = input()

while direction != "end":
    current_row_index, current_col_index = player_position
    row_movement, col_movement = direction_maper[direction]
    desired_row_index = current_row_index + row_movement
    desired_col_index = current_col_index + col_movement
    
    
    
    direction = input()






# Second task is from me



