def print_board(board):
    for row in board:
        print(*row, sep=" ")
    print()


def can_place(row, col, rows, cols, left_diagonals, right_diagonals):
    if row in rows or col in cols:
        return False
    elif (row - col) in left_diagonals:
        return False
    elif (row + col) in right_diagonals:
        return False
    return True


def place_queen(board, row, col, rows, cols, left_diagonals, right_diagonals):
    board[row][col] = "*"
    rows.add(row)
    cols.add(col)
    left_diagonals.add(row - col)
    right_diagonals.add(row + col)


def remove_queen(board, row, col, rows, cols, left_diagonals, right_diagonals):
    board[row][col] = "-"
    rows.remove(row)
    cols.remove(col)
    left_diagonals.remove(row - col)
    right_diagonals.remove(row + col)


def place_queens(row, board, rows, cols, left_diagonals, right_diagonals):
    if row == 8:
        print_board(board)
        return

    for col in range(8):
        if can_place(row, col, rows, cols, left_diagonals, right_diagonals):
            place_queen(board, row, col, rows, cols, left_diagonals, right_diagonals)
            place_queens(row + 1, board, rows, cols, left_diagonals, right_diagonals)
            remove_queen(board, row, col, rows, cols, left_diagonals, right_diagonals)


rows = 8
matrix = [["-" for _ in range(rows)] for _ in range(rows)]
place_queens(0, matrix, set(), set(), set(), set())