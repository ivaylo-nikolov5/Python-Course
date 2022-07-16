def sum_matrix_els(rows):
    matrix = [[int(el) for el in input().split(", ")] for _ in range(rows)]
    matrix_sum = 0
    for row in matrix:
        matrix_sum += sum(row)

    print(matrix_sum)
    print(matrix)


rows, cols = [int(x) for x in input().split(", ")]
sum_matrix_els(rows)