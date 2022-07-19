rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = [-9999999999]

for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        square = [matrix[row_index][col_index], matrix[row_index][col_index + 1], matrix[row_index][col_index + 2],
                  matrix[row_index + 1][col_index], matrix[row_index + 1][col_index + 1], matrix[row_index + 1][col_index + 2],
                  matrix[row_index + 2][col_index], matrix[row_index + 2][col_index + 1], matrix[row_index + 2][col_index + 2]]

        if sum(max_sum) < sum(square):
            max_sum = square

print(f"Sum = {sum(max_sum)}")
print(max_sum[0], max_sum[1], max_sum[2])
print(max_sum[3], max_sum[4], max_sum[5])
print(max_sum[6], max_sum[7], max_sum[8])