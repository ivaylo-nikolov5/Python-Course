def is_inside(row, col, rows, cols):
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return False
    return True


def find_paths(row, col, rows, cols, matrix, path, direction):
    if not is_inside(row, col, rows, cols):
        return
    elif matrix[row][col] == "*" or matrix[row][col] == "v":
        return
    elif matrix[row][col] == "e":
        path.append(direction)
        print(*path, sep="")
        path.pop()
        return

    path.append(direction)
    matrix[row][col] = "v"

    find_paths(row, col + 1, rows, cols, matrix, path, "R")
    find_paths(row + 1, col, rows, cols, matrix, path, "D")
    find_paths(row, col - 1, rows, cols, matrix, path, "L")
    find_paths(row - 1, col, rows, cols, matrix, path, "U")

    matrix[row][col] = "-"
    path.pop()


rows = int(input())
cols = int(input())

matrix = []
for _ in range(rows):
    row = input()
    matrix.append([x for x in row])

find_paths(0, 0, rows, cols, matrix, [], "")
