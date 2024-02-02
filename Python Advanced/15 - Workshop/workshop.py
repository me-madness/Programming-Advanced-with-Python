class FullColumnError(Exception):
    pass

class InvalidColumnChoice(Exception):
    pass


ROWS = 6
COLS = 7


DIRECTION_MAPPER = {
    "left": (0, -1),
    "up": (-1, 0),
    "main_diagonal": (-1, -1),
    "other_diagonal": (-1, 1),
}


def travel_direction(coordinates, current_row, current_col, element, board_map):
    count = 0
    for _ in range(1, 4):
        row_direction, col_direction = coordinates
        next_element_row_index = current_row + row_direction    
        next_element_col_index = current_col + col_direction    

        try:
            if board_map[next_element_row_index][next_element_col_index] == element:
                count += 1
            else:
                return count
        except IndexError:
            return count
                

def is_winner(current_row_index, current_col_index, board_map):
    for direction, coords in DIRECTION_MAPPER.items():
        searched_element = board_map[current_row_index][current_col_index]
        travel_direction(coords,searched_element, board_map) 
    
    
def print_board(board_map):
    for row in board_map:
        print(row)


def validate_column_choice(col):
   if 1 <= col <= COLS:
       return True
   raise InvalidColumnChoice


def get_first_available_row(col_index, board_map):
    for row_index in range(ROWS - 1, -1, -1):
        if board_map[row_index][col_index] == 0:
            return row_index
        else:
            raise FullColumnError
     
        
board_map = []

for _ in range(ROWS):
    board_map.append([0 for _ in range(COLS)])
    
turns = 1

while True:
    player = 2 if turns % 2 == 0 else 1
    
    try:
        column = input(f"Player {player}, place chose a column")
        validate_column_choice(column)
        column_index = int(column) - 1
        row = get_first_available_row(column_index, board_map)
        board_map[row][column_index] = player
        if is_winner(row, column_index, board_map):
            break
    except FullColumnError as ex:
        print("This column is full, please select another one")    
        continue
    except (InvalidColumnChoice, ValueError):
        print(f"This column is invalid, please select a number between 1 and {COLS}")  
        continue
    
      
    print_board(board_map)        
    turns += 1    
    
print(f"WINNER is player {player}")      
print_board(board_map)   









# board_map = {
#     [0, 0, 0, 0, 0 ,0, 0, 0]
#     [0, 0, 0, 0, 0 ,0, 0, 0]
#     [0, 0, 0, 0, 0 ,0, 0, 0]
#     [0, 0, 0, 0, 0 ,0, 0, 0]
#     [0, 0, 0, 0, 0 ,0, 0, 0]
#     [0, 0, 0, 0, 0 ,0, 0, 0]
# }