def flattening_matrix(rows):
    matrix = []
    for _ in range(rows):
        nums = [int(x) for x in input().split(", ")]
        matrix.extend(nums)
    print(matrix)


rows = int(input())
flattening_matrix(rows)