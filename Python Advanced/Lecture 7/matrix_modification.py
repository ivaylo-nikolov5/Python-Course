def is_inside(row: int, col: int, rows):
    return 0 <= row < rows and 0 <= col < rows


rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

command = input()
while command != "END":
    action, row, col, value = command.split()
    if action == "Add":
        if is_inside(int(row), int(col), rows):
            matrix[int(row)][int(col)] += int(value)
        else:
            print("Invalid coordinates")
    else:
        if is_inside(int(row), int(col), rows):
            matrix[int(row)][int(col)] -= int(value)
        else:
            print("Invalid coordinates")

    command = input()

for row in matrix:
    print(*row, sep=" ")