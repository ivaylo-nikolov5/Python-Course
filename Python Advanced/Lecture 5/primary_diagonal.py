def primary_diagonal(rows):
    matrix = [[int(x) for x in input().split()] for _ in range(rows)]
    result = 0
    for row in range(rows):
        result += matrix[row][row]

    print(result)


rows = int(input())
primary_diagonal(rows)