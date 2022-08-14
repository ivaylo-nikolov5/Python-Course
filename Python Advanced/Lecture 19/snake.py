def is_inside(r, c, rs):
    return 0 <= r < rs and 0 <= c < rs


def find_next_b(ma):
    for r in range(len(ma)):
        if "B" in ma[r]:
            return r, ma[r].index("B")


def move_left(r, c, rs):
    return r, c - 1


def move_right(r, c, rs):
    return r, c + 1


def move_up(r, c, rs):
    return r - 1, c


def move_down(r, c, rs):
    return r + 1, c


matrix_size = int(input())

matrix = []
snake_row = 0
snake_col = 0
eaten_food = 0
won = False

directions = {
    "left": move_left,
    "right": move_right,
    "up": move_up,
    "down": move_down
}


for row in range(matrix_size):
    matrix.append([x for x in input()])
    for col in range(matrix_size):
        if matrix[row][col] == "S":
            snake_row, snake_col = row, col

while True:
    command = input()

    if not command:
        break

    next_row, next_col = directions[command](snake_row, snake_col, matrix_size)

    matrix[snake_row][snake_col] = "."

    if not is_inside(next_row, next_col, matrix_size):
        break

    snake_row, snake_col = next_row, next_col

    cell = matrix[snake_row][snake_col]

    if cell == "B":
        matrix[snake_row][snake_col] = "."
        snake_row, snake_col = find_next_b(matrix)
    elif cell == "*":
        eaten_food += 1

    matrix[snake_row][snake_col] = "S"

    if eaten_food == 10:
        won = True
        break

if not won:
    print("Game over!")
else:
    print("You won! You fed the snake.")

print(f"Food eaten: {eaten_food}")

for row in matrix:
    print(*row, sep="")