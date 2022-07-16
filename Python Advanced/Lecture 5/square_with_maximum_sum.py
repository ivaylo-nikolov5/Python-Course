rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(j) for j in input().split(", ")] for i in range(rows)]

sum_matrix = []

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        sub_matrix = [matrix[row_index][col_index], matrix[row_index][col_index + 1],
                      matrix[row_index + 1][col_index], matrix[row_index + 1][col_index + 1]]
        if sum(sub_matrix) > sum(sum_matrix):
            sum_matrix = sub_matrix

print(*sum_matrix[:2], sep=" ")
print(*sum_matrix[2:], sep=" ")
print(sum(sum_matrix))
