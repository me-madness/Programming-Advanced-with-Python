def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))

def is_valid_position(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

def find_jetfighter(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'J':
                return row, col

def jetfighter_battle(matrix, commands):
    armor = 300
    jetfighter_row, jetfighter_col = find_jetfighter(matrix)
    enemy_planes = sum(row.count('E') for row in matrix)

    for command in commands:
        matrix[jetfighter_row][jetfighter_col] = '-'

        if command == 'up':
            jetfighter_row -= 1
        elif command == 'down':
            jetfighter_row += 1
        elif command == 'left':
            jetfighter_col -= 1
        elif command == 'right':
            jetfighter_col += 1

        if not is_valid_position(matrix, jetfighter_row, jetfighter_col):
            continue

        current_position = matrix[jetfighter_row][jetfighter_col]

        if current_position == 'E':
            enemy_planes -= 1
            if enemy_planes == 0:
                print("Mission accomplished, you neutralized the aerial threat!")
                print_matrix(matrix)
                return
            else:
                armor -= 100
                if armor <= 0:
                    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{jetfighter_row}, {jetfighter_col}]!")
                    print_matrix(matrix)
                    return
                else:
                    matrix[jetfighter_row][jetfighter_col] = '-'

        elif current_position == 'R':
            armor = 300
            matrix[jetfighter_row][jetfighter_col] = '-'

    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{jetfighter_row}, {jetfighter_col}]!")
    print_matrix(matrix)

# Example usage:
n = int(input())
airspace = [list(input()) for _ in range(n)]

commands = [input() for _ in range(n)]

jetfighter_battle(airspace, commands)