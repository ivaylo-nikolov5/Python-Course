def move_func(player_row, player_col, matrix, steps, rows, direction):
    if direction == "right":
        if is_inside(player_row, player_col + steps, rows) and matrix[player_row][player_col + steps] != "X":
            player_col += steps

    elif direction == "left":
        if is_inside(player_row, player_col - steps, rows) and matrix[player_row][player_col - steps] != "X":
            player_col -= steps
    elif direction == "down":
        if is_inside(player_row + steps, player_col, rows) and matrix[player_row + steps][player_col] != "X":
            player_row += steps

    else:
        if is_inside(player_row - steps, player_col, rows) and matrix[player_row - steps][player_col] != "X":
            player_row -= steps

    return player_row, player_col


def is_inside(row, col, rows):
    return 0 <= row < rows and 0 <= col < rows


rows = 5

matrix = []

player_row = 0
player_col = 0
targets = 0
shot_targets = []

for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == "A":
            player_row = row
            player_col = col
        elif matrix[row][col] == "x":
            targets += 1

commands = int(input())
for _ in range(commands):
    command = input().split()

    action = command[0]
    direction = command[1]

    if action == "move":
        steps = int(command[2])
        player_row, player_col = move_func(player_row, player_col, matrix, steps, rows, direction)
    else:
        bullet_row = player_row
        bullet_col = player_col
        if direction == "right":
            while bullet_col < rows - 1:
                bullet_col += 1
                if matrix[bullet_row][bullet_col] == "x":
                    shot_targets.append([bullet_row, bullet_col])
                    matrix[bullet_row][bullet_col] = "."
                    targets -= 1
                    break

        elif direction == "left":
            while bullet_col > 0:
                bullet_col -= 1
                if matrix[bullet_row][bullet_col] == "x":
                    shot_targets.append([bullet_row, bullet_col])
                    matrix[bullet_row][bullet_col] = "."
                    targets -= 1
                    break

        elif direction == "down":
            while bullet_row < rows - 1:
                bullet_row += 1
                if matrix[bullet_row][bullet_col] == "x":
                    shot_targets.append([bullet_row, bullet_col])
                    matrix[bullet_row][bullet_col] = "."
                    targets -= 1
                    break

        else:
            while bullet_row > 0:
                bullet_row -= 1
                if matrix[bullet_row][bullet_col] == "x":
                    shot_targets.append([bullet_row, bullet_col])
                    matrix[bullet_row][bullet_col] = "."
                    targets -= 1
                    break

            if targets == 0:
                break

if targets == 0:
    print(f"Training completed! All {len(shot_targets)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")

if shot_targets:
    for shot_target in shot_targets:
        print(shot_target)
