def is_inside(row, col, rows, cols):
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return False
    return True


def find_all_paths(row, col, rows, cols, matrix, paths):
    if not is_inside(row, col, rows, cols):
        return 0
    elif row == rows - 1 and col == cols - 1:
        return 1

    paths += find_all_paths(row, col + 1, rows, cols, matrix, 0)
    paths += find_all_paths(row + 1, col, rows, cols, matrix, 0)

    return paths


rows = int(input())
cols = int(input())

matrix = []
[matrix.append(["-"] * cols) for _ in range(rows)]
paths = 0
print(find_all_paths(0, 0, rows, cols, matrix, paths))


