coal = 0

def right_command(matrix, s, coal):
    row = s[0]
    col = s[1]
    if col + 1 < rows:
        matrix[row][col] = "*"
        s = [row, col + 1]
        if matrix[row][col + 1] == "c":
            coal -= 1
        matrix[row][col + 1] = "s"
    return s, coal


def left_command(matrix, s, coal):
    row = s[0]
    col = s[1]
    if col - 1 >= 0:
        matrix[row][col] = "*"
        s = [row, col - 1]
        if matrix[row][col - 1] == "c":
            coal -= 1
        matrix[row][col - 1] = "s"
    return s, coal


def up_command(matrix, s, coal):
    row = s[0]
    col = s[1]
    if row - 1 >= 0:
        matrix[row][col] = "*"
        s = [row - 1, col]
        if matrix[row - 1][col] == "c":
            coal -= 1
        matrix[row - 1][col] = "s"
    return s, coal

def down_command(matrix, s, coal):
    row = s[0]
    col = s[1]
    if row + 1 < rows:
        matrix[row][col] = "*"
        s = [row + 1, col]
        if matrix[row + 1][col] == "c":
            coal -= 1
        matrix[row + 1][col] = "s"
    return s, coal


rows = int(input())
commands = input().split()
matrix = [[x for x in input().split()] for _ in range(rows)]
s = 0
e = 0
over = False

for row in matrix:
    if "s" in row:
        col = row.index("s")

        s = [matrix.index(row), col]
    if "e" in row:
        column = row.index("e")
        e = [matrix.index(row), column]
    if "c" in row:
        coal += row.count("c")
for command in commands:
    if command == "right":
        s, coal = right_command(matrix, s, coal)
    elif command == "left":
        s, coal = left_command(matrix, s, coal)
    elif command == "up":
        s, coal = up_command(matrix, s, coal)
    elif command == "down":
        s, coal = down_command(matrix, s, coal)

    if e == s:
        over = True
        break
    if coal == 0:
        break


if over:
    print(f"Game over! ({s[0]}, {s[1]})")
else:
    if coal == 0:
        print(f"You collected all coal! ({s[0]}, {s[1]})")
    else:
        print(f"{coal} pieces of coal left. ({s[0]}, {s[1]})")