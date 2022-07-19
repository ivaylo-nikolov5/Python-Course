from collections import deque

rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(rows)]

command = input()

while command != "END":
    command = deque(command.split())
    action = command[0]
    command.popleft()
    if action == "swap" and len(command) == 4:
        row1 = int(command[0])
        col1 = int(command[1])
        row2 = int(command[2])
        col2 = int(command[4])
        if 0 <= row1 < rows and 0 <= col1 < cols and 0 <= row2 < rows and 0 <= col2 < cols:
            first_num = matrix[row1][col1]
            second_num = matrix[row2][col2]
            matrix[row1][col1] = second_num
            matrix[row2][col2] = first_num
            for el in matrix:
                print(" ".join(str(x) for x in el))
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

    command = input()