# First task is from the lecture

def is_in_boundaries(row_index, col_index, n):
    if 0 <= row_index < n and 0 <






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








# Second task is from me



