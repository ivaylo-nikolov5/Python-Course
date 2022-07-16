def even_matrix(rows):
    matrix = []

    for _ in range(rows):
        nums = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
        matrix.append(nums)

    print(matrix)


rows = int(input())
even_matrix(rows)