def two_by_two_square(r, c):
    matrix = [[x for x in input().split(" ")] for _ in range(rows)]

    squares = 0

    for row in range(r - 1):
        for col in range(c - 1):
            square = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col]
                      , matrix[row + 1][col + 1]]
            if square.count(square[0]) == 4:
                squares += 1

    print(squares)

rows, cols = [int(x) for x in input().split()]
two_by_two_square(rows, cols)
