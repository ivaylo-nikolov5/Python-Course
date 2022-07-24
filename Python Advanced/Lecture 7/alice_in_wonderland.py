def is_outside(row, col, rows):
    return row < 0 or col < 0 or row >= rows or col >= rows

rows = int(input())

matrix = []
alice_row = 0
alice_col = 0
failed = False


for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == "A":
            alice_row = row
            alice_col = col

matrix[alice_row][alice_col] = "*"
tea_bags = 0


while True:
    command = input()

    if not command:
        break

    if command == "right":
        alice_col += 1
    elif command == "left":
        alice_col -= 1
    elif command == "down":
        alice_row += 1
    else:
        alice_row -= 1

    if is_outside(alice_row, alice_col, rows):
        failed = True
    elif matrix[alice_row][alice_col] == "R":
        matrix[alice_row][alice_col] = "*"
        failed = True

    if failed:
        break

    if not matrix[alice_row][alice_col].isdigit():
        matrix[alice_row][alice_col] = "*"
        continue

    tea_bags += int(matrix[alice_row][alice_col])
    matrix[alice_row][alice_col] = "*"

    if tea_bags >= 10:
        break

if not failed:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row, sep=" ")