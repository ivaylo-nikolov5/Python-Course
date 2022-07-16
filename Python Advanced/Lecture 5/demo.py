def square_with_maximum_sum(rows, cols):
    matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
    max_sum = [-99999999999999999]

    for row_index in range(rows - 1):
        for col_index in range(cols - 1):
            nums = [matrix[row_index][col_index], matrix[row_index][col_index + 1],
                    matrix[row_index + 1][col_index], matrix[row_index + 1][col_index + 1]]

            if sum(nums) > sum(max_sum):
                max_sum = nums

    print(max_sum[0], max_sum[1])
    print(max_sum[2], max_sum[3])
    print(sum(max_sum))


rows, columns = [int(x) for x in input().split(", ")]
square_with_maximum_sum(rows, columns)
