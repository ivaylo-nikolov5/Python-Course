def is_outside(row, col, rows, matrix):
    return 0 <= row < rows and 0 <= col < rows

def explode_func(matrix, bomb):
    bomb_row, bomb_col = [int(x) for x in bomb.split(",")]
    value = matrix[bomb_row][bomb_col]
    if matrix[bomb_row][bomb_col] > 0:
        matrix[bomb_row][bomb_col] = 0
        if is_outside(bomb_row - 1, bomb_col - 1, rows, matrix) and matrix[bomb_row - 1][bomb_col - 1] > 0:
            matrix[bomb_row - 1][bomb_col - 1] -= value
        if is_outside(bomb_row - 1, bomb_col, rows, matrix) and matrix[bomb_row - 1][bomb_col] > 0:
            matrix[bomb_row - 1][bomb_col] -= value
        if is_outside(bomb_row - 1, bomb_col + 1, rows, matrix) and matrix[bomb_row - 1][bomb_col + 1] > 0:
            matrix[bomb_row - 1][bomb_col + 1] -= value
        if is_outside(bomb_row, bomb_col - 1, rows, matrix) and matrix[bomb_row][bomb_col - 1] > 0:
            matrix[bomb_row][bomb_col - 1] -= value
        if is_outside(bomb_row, bomb_col + 1, rows, matrix) and matrix[bomb_row][bomb_col + 1] > 0:
            matrix[bomb_row][bomb_col + 1] -= value
        if is_outside(bomb_row + 1, bomb_col - 1, rows, matrix) and matrix[bomb_row + 1][bomb_col - 1] > 0:
            matrix[bomb_row + 1][bomb_col - 1] -= value
        if is_outside(bomb_row + 1, bomb_col, rows, matrix) and matrix[bomb_row + 1][bomb_col] > 0:
            matrix[bomb_row + 1][bomb_col] -= value
        if is_outside(bomb_row + 1, bomb_col + 1, rows, matrix) and matrix[bomb_row + 1][bomb_col + 1] > 0:
            matrix[bomb_row + 1][bomb_col + 1] -= value

    return matrix

def bombs(r):
    matrix = [[int(x) for x in input().split()] for _ in range(r)]
    bombs_coordinates = input().split()

    for bomb in bombs_coordinates:
        matrix = explode_func(matrix, bomb)

    active_cells = 0
    active_cells_sum = 0
    for row in matrix:
        for col in row:
            if col > 0:
                active_cells += 1
                active_cells_sum += col

    print(f"Alive cells: {active_cells}")
    print(f"Sum: {active_cells_sum}")
    for row in matrix:
        print(*row, sep=" ")

rows = int(input())
bombs(rows)
