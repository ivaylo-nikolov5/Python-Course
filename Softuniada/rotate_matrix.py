def rotate_matrix(m):
    new_m = []

    for i in range(len(m)):
        j = len(m) - 1
        current_row = []
        for _ in range(len(m)):
            current_row.append(m[j][i])
            j -= 1
        new_m.append(current_row)

    return new_m


matrix = []
rows = int(input())

[matrix.append([int(x) for x in input().split(" ")]) for _ in range(rows)]

matrix = rotate_matrix(matrix)

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end=" ")
    print()
