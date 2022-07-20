def is_outside(miner_row, miner_col, rows):
    return 0 <= miner_row < rows and 0 <= miner_col < rows


def miner_next_pos(matrix, command, miner_row, miner_col, coal):

    if command == "right" and is_outside(miner_row, miner_col + 1, rows):
        miner_col += 1
        if matrix[miner_row][miner_col] == "c":
            coal -= 1
            matrix[miner_row][miner_col] = "*"

    elif command == "left" and is_outside(miner_row, miner_col - 1, rows):
        miner_col -= 1
        if matrix[miner_row][miner_col] == "c":
            coal -= 1
            matrix[miner_row][miner_col] = "*"

    elif command == "up" and is_outside(miner_row - 1, miner_col, rows):
        miner_row -= 1
        if matrix[miner_row][miner_col] == "c":
            coal -= 1
            matrix[miner_row][miner_col] = "*"

    elif command == "down" and is_outside(miner_row + 1, miner_col, rows):
        miner_row += 1
        if matrix[miner_row][miner_col] == "c":
            coal -= 1
            matrix[miner_row][miner_col] = "*"

    return miner_row, miner_col, matrix, coal


def miner(r):
    commands = input().split()
    matrix = [[x for x in input().split()] for _ in range(r)]

    miner_row = 0
    miner_col = 0
    coal = 0
    end_row = 0
    end_col = 0

    game_over = False

    matrix[miner_row][miner_col] = "*"

    for row in range(rows):

        for col in range(rows):
            if matrix[row][col] == "s":
                miner_row = row
                miner_col = col

            elif matrix[row][col] == "e":
                end_row = row
                end_col = col

            elif matrix[row][col] == "c":
                coal += 1

    for command in commands:
        miner_row, miner_col, matrix, coal = miner_next_pos(matrix, command, miner_row, miner_col, coal)

        if coal == 0:
            break

        if miner_row == end_row and miner_col == end_col:
            game_over = True
            break

    if game_over:
        print(f"Game over! ({miner_row}, {miner_col})")

    elif coal == 0:
        print(f"You collected all coal! ({miner_row}, {miner_col})")

    else:
        print(f"{coal} pieces of coal left. ({miner_row}, {miner_col})")


rows = int(input())
miner(rows)
