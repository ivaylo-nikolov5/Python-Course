def diagonals(n):
    matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]

    primary_diagonal = []
    secondary_diagonal = []

    for row in range(rows):
        primary_diagonal.append(matrix[row][row])
        secondary_diagonal.append(matrix[row][n - 1 - row])

    print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
    print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")


rows = int(input())
diagonals(rows)
