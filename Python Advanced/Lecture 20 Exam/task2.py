def is_inside(r, c, ma):
    return 0 <= r < len(ma) and 0 <= c < len(ma)


def check_diagonals_white(r, c, ma):
    over = False
    if ma[r - 1][c - 1] != "-":
        over = True
        c -= 1
    elif ma[r - 1][c + 1] != "-":
        over = True
        c += 1
    return [over, c]


def check_diagonals_black(r, c, ma):
    over = False
    if ma[r + 1][c - 1] != "-":
        over = True
        c -= 1
    elif ma[r + 1][c + 1] != "-":
        over = True
        c += 1
    return [over, c]


rows = 8

players = {
    "White pawn": [0, 0],
    "Black pawn": [0, 0]
}

matrix = []

for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == "w":
            players["White pawn"][0] = row
            players["White pawn"][1] = col
        elif matrix[row][col] == "b":
            players["Black pawn"][0] = row
            players["Black pawn"][1] = col

counter = 0

while True:
    player = "White pawn" if counter % 2 == 0 else "Black pawn"
    row = players[player][0]
    col = players[player][1]
    if player == "White pawn" and row > 0 and 0 < col < len(matrix) and check_diagonals_white(players[player][0], players[player][1], matrix)[0]:
        col = check_diagonals_white(players[player][0], players[player][1], matrix)[1]
        print(f"Game over! {player.split()[0]} win, capture on {chr(97 + col)}{8}.")
        break
    elif player == "Black pawn" and 0 < row < len(matrix) and 0 < col < len(matrix) and check_diagonals_black(players[player][0], players[player][1], matrix)[0]:
        col = check_diagonals_black(players[player][0], players[player][1], matrix)[1]
        print(f"Game over! {player.split()[0]} win, capture on {chr(97 + col)}{1}.")
        break
    else:
        if player == "White pawn":
            if is_inside(row - 1, col, matrix):
                players[player][0] -= 1
            else:
                print(f"Game over! {player} is promoted to a queen at {chr(97 + col)}{8 - row}.")
                break
        else:
            if is_inside(row + 1, col, matrix):
                players[player][0] += 1
            else:
                print(f"Game over! {player} is promoted to a queen at {chr(97 + col)}{row + 1}.")
                break



    counter += 1


