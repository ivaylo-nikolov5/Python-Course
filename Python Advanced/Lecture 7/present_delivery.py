def get_next_pos(row, col, direction):
    if direction == "right":
        return row, col + 1
    elif direction == "left":
        return row, col - 1
    elif direction == "up":
        return row - 1, col
    else:
        return row + 1, col

presents = int(input())
rows = int(input())

matrix = []
santa_row = 0
santa_col = 0
total_good_kids = 0
delivered_presents = 0

for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == "S":
            santa_row = row
            santa_col = col
        elif matrix[row][col] == "V":
            total_good_kids += 1

while True:
    command = input()
    if command == "Christmas morning":
        break
    matrix[santa_row][santa_col] = "-"
    santa_row, santa_col = get_next_pos(santa_row, santa_col, command)

    if matrix[santa_row][santa_col] == "V":
        presents -= 1
        delivered_presents += 1

    elif matrix[santa_row][santa_col] == "C":

        if matrix[santa_row][santa_col - 1] == "V" and presents:
            delivered_presents += 1
            presents -= 1
            matrix[santa_row][santa_col - 1] = "-"
        elif matrix[santa_row][santa_col - 1] == "X" and presents:
            presents -= 1
            matrix[santa_row][santa_col - 1] = "-"

        if matrix[santa_row][santa_col + 1] == "V" and presents:
            delivered_presents += 1
            presents -= 1
            matrix[santa_row][santa_col + 1] = "-"
        elif matrix[santa_row][santa_col + 1] == "X" and presents:
            presents -= 1
            matrix[santa_row][santa_col + 1] = "-"

        if matrix[santa_row - 1][santa_col] == "V" and presents:
            delivered_presents += 1
            presents -= 1
            matrix[santa_row - 1][santa_col] = "-"

        elif matrix[santa_row - 1][santa_col] == "X" and presents:
            presents -= 1
            matrix[santa_row - 1][santa_col] = "-"

        if matrix[santa_row + 1][santa_col] == "V" and presents:
            delivered_presents += 1
            presents -= 1
            matrix[santa_row + 1][santa_col] = "-"
        elif matrix[santa_row + 1][santa_col] == "X" and presents:
            presents -= 1
            matrix[santa_row + 1][santa_col] = "-"

    matrix[santa_row][santa_col] = "S"

    if presents == 0 or delivered_presents == total_good_kids:
        break

if presents == 0 and delivered_presents < total_good_kids:
    print(f"Santa ran out of presents!")

for row in matrix:
    print(*row, sep=" ")

if delivered_presents == total_good_kids:
    print(f"Good job, Santa! {total_good_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_good_kids - delivered_presents} nice kid/s.")