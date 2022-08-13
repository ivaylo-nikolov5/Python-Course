def check_bombs_around(r, c, ma, sz):
    bombs_around = 0
    # up
    if is_inside(r - 1, c, sz) and matrix[r - 1][c] == "*":
        bombs_around += 1
    # up right
    if is_inside(r - 1, c + 1, sz) and matrix[r - 1][c + 1] == "*":
        bombs_around += 1
    # right
    if is_inside(r, c + 1, sz) and matrix[r][c + 1] == "*":
        bombs_around += 1
    # down right
    if is_inside(r + 1, c + 1, sz) and matrix[r + 1][c + 1] == "*":
        bombs_around += 1
    # down
    if is_inside(r + 1, c, sz) and matrix[r + 1][c] == "*":
        bombs_around += 1
    # down left
    if is_inside(r + 1, c - 1, sz) and matrix[r + 1][c - 1] == "*":
        bombs_around += 1
    # left
    if is_inside(r, c - 1, sz) and matrix[r][c - 1] == "*":
        bombs_around += 1
    # left up
    if is_inside(r - 1, c - 1, sz) and matrix[r - 1][c - 1] == "*":
        bombs_around += 1

    return bombs_around


def is_inside(r, c, sz):
    return 0 <= r < sz and 0 <= c < sz


size = int(input())
bombs = int(input())

matrix = [[0 for _ in range(size)] for _ in range(size)]

for bomb in range(bombs):
    row, col = [el for el in eval(input())]
    if is_inside(row, col, size):
        matrix[row][col] = "*"

for row in range(size):
    for col in range(size):
        if matrix[row][col] != "*":
            num = check_bombs_around(row, col, matrix, size)
            matrix[row][col] = num

for row in matrix:
    print(*row, sep=" ")