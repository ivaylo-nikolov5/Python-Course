def get_next_pos(player_row, player_col, steps, direction):
    if direction == "up":
        return player_row - steps, player_col
    elif direction == "down":
        return player_row + steps, player_col
    elif direction == "right":
        return player_row, player_col + steps
    else:
        return player_row, player_col - steps


def is_outside(row, col, rows):
    return row < 0 or col < 0 or col >= rows or row >= rows


rows = 5

matrix = []
player_row = 0
player_col = 0
targets = 0

hit_targets = []

for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == "A":
            player_row = row
            player_col = col
        elif matrix[row][col] == "x":
            targets += 1

targets_left = targets
commands = int(input())

for _ in range(commands):
    command = input().split()
    action = command[0]
    direction = command[1]
    if action == "move":
        steps = int(command[2])
        next_row, next_col = get_next_pos(player_row, player_col, steps, direction)

        if is_outside(next_row, next_col, rows) or matrix[next_row][next_col] != ".":
            continue

        matrix[player_row][player_col] = "."
        player_row = next_row
        player_col = next_col
        matrix[player_row][player_col] = "A"
    else:
        bullet_row, bullet_col = player_row, player_col
        while True:
            bullet_row, bullet_col = get_next_pos(bullet_row, bullet_col, 1, direction)
            if is_outside(bullet_row, bullet_col, rows):
                break

            if matrix[bullet_row][bullet_col] == "x":
                hit_targets.append([bullet_row, bullet_col])
                matrix[bullet_row][bullet_col] = "."
                targets_left -= 1
                break

        if targets_left == 0:
            break

if targets_left == 0:
    print(f"Training completed! All {targets} targets hit.")
else:
    print(f"Training not completed! {targets_left} targets left.")

for target in hit_targets:
    print(target)
