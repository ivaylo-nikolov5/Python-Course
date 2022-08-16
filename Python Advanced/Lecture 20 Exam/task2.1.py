def is_inside(r, c, sz):
    return 0 <= r < sz and 0 <= c < sz


def move_left(r, c, sz):
    if is_inside(r, c - 1, sz):
        return r, c - 1
    return r, sz - 1


def move_up(r, c, sz):
    if is_inside(r - 1, c, sz):
        return r - 1, c
    return sz - 1, c


def move_right(r, c, sz):
    if is_inside(r, c + 1, sz):
        return r, c + 1
    return r, 0


def move_down(r, c, sz):
    if is_inside(r + 1, c, sz):
        return r + 1, c
    return 0, c


directions = {
    "left": move_left,
    "up": move_up,
    "right": move_right,
    "down": move_down
}

size = 6

rover_row = 0
rover_col = 0
water_deposit = 0
metal_deposit = 0
concrete_deposit = 0
broken = False

matrix = []

for row in range(size):
    matrix.append([x for x in input().split()])
    if "E" in matrix[row]:
        rover_row = row
        rover_col = matrix[row].index("E")


commands = input()
commands = commands.split(", ")

for command in commands:
    next_row, next_col = directions[command](rover_row, rover_col, size)
    rover_row, rover_col = next_row, next_col
    current_position = matrix[rover_row][rover_col]

    if current_position == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        broken = True
        break
    elif current_position == "W":
        print(f"Water deposit found at ({rover_row}, {rover_col})")
        water_deposit += 1
    elif current_position == "M":
        print(f"Metal deposit found at ({rover_row}, {rover_col})")
        metal_deposit += 1
    elif current_position == "C":
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")
        concrete_deposit += 1


if metal_deposit >= 1 and water_deposit >= 1 and concrete_deposit >= 1:
    print("Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")


