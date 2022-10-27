def find_all_paths_in_labyrinth(row, col, matrix, direction, path):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return

    if matrix[row][col] == "*":
        return
    if matrix[row][col] == "v":
        return

    path.append(direction)
    if matrix[row][col] == "e":
        print("".join(path))
    else:
        matrix[row][col] = "v"
        find_all_paths_in_labyrinth(row, col + 1, matrix, "R", path)
        find_all_paths_in_labyrinth(row, col - 1, matrix, "L", path)
        find_all_paths_in_labyrinth(row + 1, col, matrix, "D", path)
        find_all_paths_in_labyrinth(row - 1, col, matrix, "U", path)
        matrix[row][col] = "-"

    path.pop()


rows = int(input())
cols = int(input())

labyrinth = [list(input()) for _ in range(rows)]

find_all_paths_in_labyrinth(0, 0, labyrinth, "", [])