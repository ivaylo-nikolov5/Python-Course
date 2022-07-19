size = int(input())

matrix = [[int(x) for x in input().split()]for _ in range(size)]

bombs_coordinates = input().split()

for bomb in bombs_coordinates:
    row, col = (int(x) for x in bomb.split(","))
    value = matrix[row][col]
    matrix[row][col] = 0
    if value > 0:
        if row - 1 >= 0 and col - 1 >= 0 and matrix[row - 1][col - 1] > 0:
            matrix[row - 1][col - 1] -= value

        if row - 1 >= 0 and matrix[row - 1][col] > 0:
            matrix[row - 1][col] -= value

        if row - 1 >= 0 and col + 1 < size and matrix[row - 1][col + 1] > 0:
            matrix[row - 1][col + 1] -= value

        if col - 1 >= 0 and matrix[row][col - 1] > 0:
            matrix[row][col - 1] -= value

        if col + 1 < size and matrix[row][col + 1] > 0:
            matrix[row][col + 1] -= value

        if row + 1 < size and col - 1 >= 0 and matrix[row + 1][col - 1] > 0:
            matrix[row + 1][col - 1] -= value

        if row + 1 < size and matrix[row + 1][col] > 0:
            matrix[row + 1][col] -= value

        if row + 1 < size and col + 1 < size and matrix[row + 1][col + 1] > 0:
            matrix[row + 1][col + 1] -= value

alive_cells = 0
sum_cells = 0

for x in matrix:
    for y in x:
        if y > 0:
            alive_cells += 1
            sum_cells += y

print(f"Alive cells: {alive_cells}\nSum: {sum_cells}")
for x in matrix:
    print(" ".join(str(el) for el in x))