def maximal_sum(r, c):
    matrix = [[int(x) for x in input().split(" ")] for _ in range(rows)]

    max_sum = [-999999999999]

    for row in range(r - 2):
        for col in range(c - 2):
            square = [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]
                      , matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]
                      , matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]

            if sum(square) > sum(max_sum):
                max_sum = square

    print(f"Sum = {sum(max_sum)}")
    print(max_sum[0], max_sum[1], max_sum[2])
    print(max_sum[3], max_sum[4], max_sum[5])
    print(max_sum[6], max_sum[7], max_sum[8])


rows, cols = [int(x) for x in input().split()]
maximal_sum(rows, cols)
