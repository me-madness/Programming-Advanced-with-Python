ROWS = 6
COLS = 7

def print_board(board_map):
    for row in board_map:
        print(row)


board_map = []


for _ in range(ROWS):
    board_map.append([0 for _ in range(COLS)])
    
print_board()    









# board_map = {
#     [0, 0, 0, 0, 0 ,0, 0, 0]
#     [0, 0, 0, 0, 0 ,0, 0, 0]
#     [0, 0, 0, 0, 0 ,0, 0, 0]
#     [0, 0, 0, 0, 0 ,0, 0, 0]
#     [0, 0, 0, 0, 0 ,0, 0, 0]
#     [0, 0, 0, 0, 0 ,0, 0, 0]
# }