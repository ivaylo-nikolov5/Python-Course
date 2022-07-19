def get_next_pos(row, col, command):
    if command == 'U':
        return row - 1, col
    if command == 'L':
        return row, col - 1
    if command == 'R':
        return row, col + 1
    if command == 'D':
        return row + 1, col


def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


rows, cols = [int(x) for x in input().split()]

matrix = []
player_row = 0
player_col = 0
bunnies = set()

for row in range(rows):
    row_elements = list(input())
    matrix.append(row_elements)

    for col in range(cols):
        if row_elements[col] == 'P':
            player_row = row
            player_col = col
        elif row_elements[col] == 'B':
            bunnies.add(f'{row} {col}')

won = False
dead = False

commands = input()

matrix[player_row][player_col] = '.'

for command in commands:
    next_row, next_col = get_next_pos(player_row, player_col, command)

    if is_outside(next_row, next_col, rows, cols):
        won = True
    elif matrix[next_row][next_col] == 'B':
        dead = True
        player_row, player_col = next_row, next_col
    else:
        player_row, player_col = next_row, next_col

    new_bunnies = set()
    for bunny in bunnies:
        bunny_row, bunny_col = [int(x) for x in bunny.split()]

        if not is_outside(bunny_row - 1, bunny_col, rows, cols):
            new_bunnies.add(f'{bunny_row - 1} {bunny_col}')
            matrix[bunny_row - 1][bunny_col] = 'B'
        if not is_outside(bunny_row + 1, bunny_col, rows, cols):
            new_bunnies.add(f'{bunny_row + 1} {bunny_col}')
            matrix[bunny_row + 1][bunny_col] = 'B'
        if not is_outside(bunny_row, bunny_col - 1, rows, cols):
            new_bunnies.add(f'{bunny_row} {bunny_col - 1}')
            matrix[bunny_row][bunny_col - 1] = 'B'
        if not is_outside(bunny_row, bunny_col + 1, rows, cols):
            new_bunnies.add(f'{bunny_row} {bunny_col + 1}')
            matrix[bunny_row][bunny_col + 1] = 'B'

    bunnies = bunnies.union(new_bunnies)

    if matrix[player_row][player_col] == 'B':
        dead = True

    if won or dead:
        break

for row in matrix:
    print(*row, sep='')

if won:
    print(f'won: {player_row} {player_col}')
else:
    print(f'dead: {player_row} {player_col}')