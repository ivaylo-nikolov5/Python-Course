def diagonals(n):
    matrix = [[int(x) for x in input().split(" ")] for _ in range(rows)]

    primary_diagonal = []
    secondary_diagonal = []

    for row in range(rows):
        primary_diagonal.append(matrix[row][row])
        secondary_diagonal.append(matrix[row][n - 1 - row])

    diff = abs(sum(primary_diagonal) - sum(secondary_diagonal))

    print(diff)


rows = int(input())
diagonals(rows)
