def is_inside(row, col):
    return 0 <= row < rows and 0 <= col < rows


rows = int(input())

matrix = [[x for x in input()] for _ in range(rows)]

horses = dict()
removed_knights = 0

while True:
    for row in range(rows):
        for col in range(rows):
            if matrix[row][col] == "K":
                horses[f"{row} {col}"] = 0

    for horse in horses:
        row, col = [int(x) for x in horse.split()]

        if is_inside(row - 2, col - 1) and matrix[row - 2][col - 1] == "K":
            horses[horse] += 1

        if is_inside(row - 2, col + 1) and matrix[row - 2][col + 1] == "K":
            horses[horse] += 1

        if is_inside(row - 1, col - 2) and matrix[row - 1][col - 2] == "K":
            horses[horse] += 1

        if is_inside(row - 1, col + 2) and matrix[row - 1][col + 2] == "K":
            horses[horse] += 1

        if is_inside(row + 2, col - 1) and matrix[row + 2][col - 1] == "K":
            horses[horse] += 1

        if is_inside(row + 2, col + 1) and matrix[row + 2][col + 1] == "K":
            horses[horse] += 1

        if is_inside(row + 1, col - 2) and matrix[row + 1][col - 2] == "K":
            horses[horse] += 1

        if is_inside(row + 1, col + 2) and matrix[row + 1][col + 2] == "K":
            horses[horse] += 1

    biggest = 0
    biggest_horse = ""
    for horse in horses:
        if horses[horse] > biggest:
            biggest = horses[horse]
            biggest_horse = horse

    if biggest > 0:
        del horses[biggest_horse]
        removed_knights += 1
        row, col = [int(x) for x in biggest_horse.split()]
        matrix[row][col] = "0"
    else:
        break

print(removed_knights)