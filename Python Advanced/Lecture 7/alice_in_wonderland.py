def is_outside(row, col, rows):
    return 0 > row or 0 > col or row >= rows or col >= rows

def move_func(row, col, command):
    if command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col
    elif command == "left":
        return row, col - 1
    else:
        return row, col + 1


rows = int(input())

matrix = []
alice_row = 0
alice_col = 0
rabbit_row = 0
rabbit_col = 0
tea_bags = 0
failed = False
felt = False


for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == "A":
            alice_row = row
            alice_col = col
        elif matrix[row][col] == "R":
            rabbit_row = row
            rabbit_col = col

command = input()
matrix[alice_row][alice_col] = "*"

while True:
    if not command:
        break

    alice_row, alice_col = move_func(alice_row, alice_col, command)

    if is_outside(alice_row, alice_col, rows):
        failed = True
        break

    elif alice_row == rabbit_row and alice_col == rabbit_col:
        matrix[rabbit_row][rabbit_col] = "*"
        felt = True
        break

    else:
        if matrix[alice_row][alice_col].isdigit():
            tea_bags += int(matrix[alice_row][alice_col])
        matrix[alice_row][alice_col] = "*"

        if tea_bags >= 10:
            break

    command = input()

if failed or felt:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for row in matrix:
    print(*row, sep=" ")