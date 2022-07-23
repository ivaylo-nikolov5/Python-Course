rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

command = input()

while command != "END":
    command = command.split()
    action = command[0]
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])

    if action == "Add":
        if 0 <= row < rows and 0 <= col < rows:
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    elif action == "Subtract":
        if 0 <= row < rows and 0 <= col < rows:
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")

    command = input()

for row in matrix:
    print(*row, sep=" ")