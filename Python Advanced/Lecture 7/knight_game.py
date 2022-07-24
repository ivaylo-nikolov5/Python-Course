def calc_collisions(matrix, row, col, rows, horses):
    if is_inside(row - 2, col - 1, rows) and matrix[row - 2][col - 1] == "K":
        horses[horse] += 1

    if is_inside(row - 2, col + 1, rows) and matrix[row - 2][col + 1] == "K":
        horses[horse] += 1

    if is_inside(row - 1, col - 2, rows) and matrix[row - 1][col - 2] == "K":
        horses[horse] += 1

    if is_inside(row - 1, col + 2, rows) and matrix[row - 1][col + 2] == "K":
        horses[horse] += 1

    if is_inside(row + 2, col - 1, rows) and matrix[row + 2][col - 1] == "K":
        horses[horse] += 1

    if is_inside(row + 2, col + 1, rows) and matrix[row + 2][col + 1] == "K":
        horses[horse] += 1

    if is_inside(row + 1, col - 2, rows) and matrix[row + 1][col - 2] == "K":
        horses[horse] += 1

    if is_inside(row + 1, col + 2, rows) and matrix[row + 1][col + 2] == "K":
        horses[horse] += 1

    return horses


def is_inside(row, col, rows):
    return 0 <= row < rows and 0 <= col < rows


rows = int(input())
matrix = [[x for x in input()] for _ in range(rows)]
removed_horses = 0

horses = {}
while True:

    for row in range(rows):
        for col in range(rows):
            if not matrix[row][col] == "K":
                continue
            horses[f"{row} {col}"] = 0

    for horse in horses:
        row, col = [int(x) for x in horse.split()]

        horses = calc_collisions(matrix, row, col, rows, horses)

    max_horse = ""
    max_collisions = 0

    for horse in horses:
        if horses[horse] > max_collisions:
            max_horse = horse
            max_collisions = horses[horse]

    if max_collisions > 0:
        row, col = [int(x) for x in max_horse.split()]
        removed_horses += 1
        del horses[max_horse]
        matrix[row][col] = "0"
        continue

    break

print(removed_horses)