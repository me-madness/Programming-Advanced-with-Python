class FullColumnError(Exception):
    pass


ROWS = 6
COLS = 7

def print_board(board_map):
    for row in board_map:
        print(row)

def place_player_choice(col_index, player_num, board_map):
    for row_index in range(ROWS - 1, -1, -1):
        if board_map[row_index][col_index] == 0:
            board_map[row_index][col_index] = player_num
            break
        else:
            raise FullColumnError("This column is full, please select another one")
     
        
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