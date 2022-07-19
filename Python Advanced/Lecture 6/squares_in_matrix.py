rows, cols = [int(x) for x in input().split()]

matrix = [[el for el in input().split()] for _ in range(rows)]

squares = 0

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        square = [matrix[row_index][col_index], matrix[row_index][col_index + 1],
                  matrix[row_index + 1][col_index], matrix[row_index + 1][col_index + 1]]

        if square.count(square[0]) == 4:
            squares += 1

print(squares)

