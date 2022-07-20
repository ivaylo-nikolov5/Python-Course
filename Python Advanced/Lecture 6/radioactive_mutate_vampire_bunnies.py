def is_inside(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


def move_func(player_row, player_col, command, rows, cols):
    won = False
    if command == "L" and is_inside(player_row, player_col - 1, rows, cols):
        player_col -= 1
    elif command == "R" and is_inside(player_row, player_col + 1, rows, cols):
        player_col += 1
    elif command == "U" and is_inside(player_row - 1, player_col, rows, cols):
        player_row -= 1
    elif command == "D" and is_inside(player_row + 1, player_col, rows, cols):
        player_row += 1
    else:
        won = True

    return player_row, player_col, won


def vampire_bunnies(rows, cols):
    matrix = [[x for x in input()] for _ in range(rows)]
    commands = input()
    player_row = 0
    player_col = 0

    bunnies = set()
    won = False
    dead = False

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "P":
                player_row = row
                player_col = col

            elif matrix[row][col] == "B":
                bunnies.add(f"{row} {col}")
    matrix[player_row][player_col] = "."

    for command in commands:
        player_row, player_col, won = move_func(player_row, player_col, command, rows, cols)

        new_bunnies = set()
        for bunny in bunnies:
            bunny_row, bunny_col = [int(x) for x in bunny.split()]
            if is_inside(bunny_row - 1, bunny_col, rows, cols):
                new_bunnies.add(f"{bunny_row - 1} {bunny_col}")
                matrix[bunny_row - 1][bunny_col] = "B"

            if is_inside(bunny_row + 1, bunny_col, rows, cols):
                new_bunnies.add(f"{bunny_row + 1} {bunny_col}")
                matrix[bunny_row + 1][bunny_col] = "B"

            if is_inside(bunny_row, bunny_col + 1, rows, cols):
                new_bunnies.add(f"{bunny_row} {bunny_col + 1}")
                matrix[bunny_row][bunny_col + 1] = "B"

            if is_inside(bunny_row, bunny_col - 1, rows, cols):
                new_bunnies.add(f"{bunny_row} {bunny_col - 1}")
                matrix[bunny_row][bunny_col - 1] = "B"

        bunnies = bunnies.union(new_bunnies)

        if matrix[player_row][player_col] == "B":
            dead = True
            break

        if won or dead:
            break

    for row in matrix:
        print(*row, sep="")
    if won:
        print(f"won: {player_row} {player_col}")
    else:
        print(f"dead: {player_row} {player_col}")


rows, cols = [int(x) for x in input().split()]
vampire_bunnies(rows, cols)
