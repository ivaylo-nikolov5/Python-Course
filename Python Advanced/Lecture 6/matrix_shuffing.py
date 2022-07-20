def matrix_shuffling(r, c):
    matrix = [[x for x in input().split()] for _ in range(rows)]
    command = input()
    while command != "END":
        command = command.split()
        action = command[0]

        if action == "swap" and len(command) == 5:
            r1 = int(command[1])
            c1 = int(command[2])
            r2 = int(command[3])
            c2 = int(command[4])

            if r > r1 >= 0 and c > c1 >= 0 and r > r2 >= 0 and c > c2 >= 0:
                matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]

                for row in matrix:
                    print(*row, sep=" ")
            else:
                print("Invalid input!")
        else:
            print("Invalid input!")

        command = input()


rows, cols = [int(x) for x in input().split()]
matrix_shuffling(rows, cols)
