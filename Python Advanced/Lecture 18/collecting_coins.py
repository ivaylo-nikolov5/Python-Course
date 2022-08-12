import math


def is_inside(r, c, rs):
    return 0 <= r < rs and 0 <= c < rs


def move_left(r, c):
    return r, c - 1


def move_right(r, c):
    return r, c + 1


def move_up(r, c):
    return r - 1, c


def move_down(r, c):
    return r + 1, c


coins = 0
player_row = 0
player_col = 0
game_over = False

directions = {
    "left": move_left,
    "right": move_right,
    "up": move_up,
    "down": move_down
}


rows = int(input())

matrix = []
path = []

for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == "P":
            player_row = row
            player_col = col
            path.append([player_row, player_col])

while coins < 100:
    command = input()

    if not command:
        break

    next_row, next_col = directions[command](player_row, player_col)

    if is_inside(next_row, next_col, rows):
        player_row, player_col = next_row, next_col

    else:
        if next_row > rows - 1:
            player_row = 0
        elif next_row < 0:
            player_row = rows - 1
        elif next_col > rows - 1:
            player_col = 0
        else:
            player_col = rows - 1

    path.append([player_row, player_col])
    cell = matrix[player_row][player_col]
    if cell == "X":
        game_over = True
        coins = math.floor(0.5 * coins)
        break
    elif cell != "P":
        coins += int(matrix[player_row][player_col])
        matrix[player_row][player_col] = 0


if not game_over:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print("Your path:")
for el in path:
    print(el)
