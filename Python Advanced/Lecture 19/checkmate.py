def check_left(row, col, ma):
    while True:
        col -= 1
        if col < 0:
            break
        if ma[row][col] == "Q":
            return [row, col]
    return False


def check_up(row, col, ma):
    while True:
        row -= 1
        if row < 0:
            break
        if ma[row][col] == "Q":
            return [row, col]
    return False


def check_right(row, col, ma):
    while True:
        col += 1
        if col >= len(ma):
            break
        if ma[row][col] == "Q":
            return [row, col]
    return False


def check_down(row, col, ma):
    while True:
        row += 1
        if row >= len(ma):
            break
        if ma[row][col] == "Q":
            return [row, col]

    return False


def check_left_up(row, col, ma):
    while True:
        row -= 1
        col -= 1
        if row < 0 or col < 0:
            break
        if ma[row][col] == "Q":
            return [row, col]

    return False


def check_right_up(row, col, ma):
    while col < len(ma) and row > 0:
        row -= 1
        col += 1
        if row < 0 or col >= len(ma):
            break
        if ma[row][col] == "Q":
            return [row, col]

    return False


def check_right_down(row, col, ma):
    while col < len(ma) and row < len(ma):
        row += 1
        col += 1
        if row >= len(ma) or col >= len(ma):
            break
        if ma[row][col] == "Q":
            return [row, col]

    return False


def check_left_down(row, col, ma):
    while True:
        row += 1
        col -= 1
        if row >= len(ma) or col < 0:
            break
        if ma[row][col] == "Q":
            return [row, col]

    return False


def check_capture(row, col, ma, queens: list):
    # check left
    if check_left(row, col, ma):
        queens.append(check_left(row, col, ma))
    # check up
    if check_up(row, col, ma):
        queens.append(check_up(row, col, ma))
    # check right
    if check_right(row, col, ma):
        queens.append(check_right(row, col, ma))
    # check down
    if check_down(row, col, ma):
        queens.append(check_down(row, col, ma))
    # check left up
    if check_left_up(row, col, ma):
        queens.append(check_left_up(row, col, ma))
    # check right up
    if check_right_up(row, col, ma):
        queens.append(check_right_up(row, col, ma))
    # check right down
    if check_right_down(row, col, ma):
        queens.append(check_right_down(row, col, ma))
    # check left down
    if check_left_down(row, col, ma):
        queens.append(check_left_down(row, col, ma))

    if queens:
        return queens

    return False


board_size = 8

king_row = 0
king_col = 0

matrix = []
queens = []

for row in range(board_size):
    matrix.append([x for x in input().split()])
    if "K" not in matrix[row]:
        continue
    king_row, king_col = row, matrix[row].index("K")

queens = check_capture(king_row, king_col, matrix, queens)

if queens:
    for queen in queens:
        print(queen)
else:
    print("The king is safe!")