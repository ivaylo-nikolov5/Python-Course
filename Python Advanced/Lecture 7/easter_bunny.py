def right_func(row, col, matrix):
    total = 0
    moves = 0
    while col < rows - 1:
        col += 1
        if matrix[row][col].isdigit():
            total += int(matrix[row][col])
            moves += 1
        else:
            return total, moves

    return total, moves


def left_func(row, col, matrix):
    total = 0
    moves = 0
    while col > 0:
        col -= 1
        if matrix[row][col].isdigit():
            total += int(matrix[row][col])
            moves += 1
        else:
            return total, moves

    return total, moves


def up_func(row, col, matrix):
    total = 0
    moves = 0
    while row > 0:
        row -= 1
        if matrix[row][col].isdigit():
            total += int(matrix[row][col])
            moves += 1
        else:
            return total, moves

    return total, moves


def down_func(row, col, matrix):
    total = 0
    moves = 0
    while row < rows - 1:
        row += 1
        if matrix[row][col].isdigit():
            total += int(matrix[row][col])
            moves += 1
        else:
            return total, moves

    return total, moves


rows = int(input())

matrix = [[x for x in input().split()] for _ in range(rows)]

bunny_row = 0
bunny_col = 0

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "B":
            bunny_row, bunny_col = row, col
            break

right_sum, right_moves = right_func(bunny_row, bunny_col, matrix)
left_sum, left_moves = left_func(bunny_row, bunny_col, matrix)
up_sum, up_moves = up_func(bunny_row, bunny_col, matrix)
down_sum, down_moves = down_func(bunny_row, bunny_col, matrix)

max_sum = (max(right_sum, left_sum, up_sum, down_sum))

if right_sum == max_sum:
    print("right")
    for row in range(right_moves):
        bunny_col += 1
        print(f"[{bunny_row}, {bunny_col}]")
    print(right_sum)

elif left_sum == max_sum:
    print("left")
    for row in range(left_moves):
        bunny_col -= 1
        print(f"[{bunny_row}, {bunny_col}]")
    print(left_sum)
elif down_sum == max_sum:
    print("down")
    for row in range(down_moves):
        bunny_row += 1
        print(f"[{bunny_row}, {bunny_col}]")
    print(down_sum)

elif up_sum == max_sum:
    print("up")
    for row in range(up_moves):
        bunny_row -= 1
        print(f"[{bunny_row}, {bunny_col}]")
    print(up_sum)

