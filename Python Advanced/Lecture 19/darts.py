import re


def deduct(r, c, m):
    return (int(matrix[r][0]) + int(matrix[r][6]) + int(matrix[0][c]) + int(matrix[6][c])) * m


def is_inside(r, c, rs):
    return 0 <= r < rs and 0 <= c < rs


player_one, player_two = [el for el in input().split(", ")]
players = {
    player_one: [501, 0],
    player_two: [501, 0]
}

rows = 7
matrix = [[el for el in input().split()]for _ in range(rows)]

counter = 0

while True:
    player = player_one if counter % 2 == 0 else player_two

    throw = input()

    if not throw:
        break

    row, col = [el for el in eval(throw)]

    players[player][1] += 1

    if not is_inside(row, col, rows):
        counter += 1
        continue

    current_cell = matrix[row][col]

    if current_cell == "B":
        print(f"{player} won the game with {players[player][1]} throws!")
        break
    elif current_cell == "D":
        subtract = deduct(row, col, 2)
    elif current_cell == "T":
        subtract = deduct(row, col, 3)
    else:
        subtract = int(current_cell)

    players[player][0] -= subtract

    if players[player][0] <= 0:
        print(f"{player} won the game with {players[player][1]} throws!")
        break

    counter += 1

