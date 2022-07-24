def right(row, col, matrix, rows):
    steps = 0
    current_sum = 0
    while col < rows - 1:
        col += 1

        if matrix[row][col] == "X":
            return current_sum, steps
        current_sum += int(matrix[row][col])
        steps += 1
    return current_sum, steps


def left(row, col, matrix, rows):
    steps = 0
    current_sum = 0
    while col > 0:
        col -= 1

        if matrix[row][col] == "X":
            return current_sum, steps
        current_sum += int(matrix[row][col])
        steps += 1
    return current_sum, steps


def down(row, col, matrix, rows):
    steps = 0
    current_sum = 0
    while row < rows - 1:
        row += 1

        if matrix[row][col] == "X":
            return current_sum, steps
        current_sum += int(matrix[row][col])
        steps += 1
    return current_sum, steps


def up(row, col, matrix, rows):
    steps = 0
    current_sum = 0
    while row > 0:
        row -= 1

        if matrix[row][col] == "X":
            return current_sum, steps
        current_sum += int(matrix[row][col])
        steps += 1
    return current_sum, steps


rows = int(input())

matrix = []


bunny_row = 0
bunny_col = 0

for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == "B":
            bunny_row = row
            bunny_col = col

right_sum, right_steps = right(bunny_row, bunny_col, matrix, rows)
left_sum, left_steps = left(bunny_row, bunny_col, matrix, rows)
down_sum, down_steps = down(bunny_row, bunny_col, matrix, rows)
up_sum, up_steps = up(bunny_row, bunny_col, matrix, rows)

max_sum = max(right_sum, left_sum, down_sum, up_sum)

if max_sum == right_sum:
    print("right")
    for step in range(right_steps):
        bunny_col += 1
        print(f"[{bunny_row}, {bunny_col}]")


elif max_sum == left_sum:
    print("left")
    for step in range(left_steps):
        bunny_col -= 1
        print(f"[{bunny_row}, {bunny_col}]")

elif max_sum == down_sum:
    print("down")
    for step in range(down_steps):
        bunny_row += 1
        print(f"[{bunny_row}, {bunny_col}]")

else:
    print("up")
    for step in range(up_steps):
        bunny_row -= 1
        print(f"[{bunny_row}, {bunny_col}]")

print(max_sum)
