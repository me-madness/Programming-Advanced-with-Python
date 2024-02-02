ROWS = 6
COLS = 7

def print_board(board_map):
    for row in board_map:
        print(row)


board_map = []


for _ in range(ROWS):
    board_map.append([0 for _ in range(COLS)])
    
turns = 1

while True:
    player = 2 if turns % 2 == 0 else 1
    column = input(f"Player {player}, place chose a column")
    column_index = int(column) - 1
    
    
    turns += 1    
    
    
    
print_board(board_map)    









# board_map = {
#     [0, 0, 0, 0, 0 ,0, 0, 0]
#     [0, 0, 0, 0, 0 ,0, 0, 0]
#     [0, 0, 0, 0, 0 ,0, 0, 0]
#     [0, 0, 0, 0, 0 ,0, 0, 0]
#     [0, 0, 0, 0, 0 ,0, 0, 0]
#     [0, 0, 0, 0, 0 ,0, 0, 0]
# }