def symbol_in_matrix(rows):
    matrix = [[x for x in input()] for _ in range(rows)]
    result = None
    special_symbol = input()
    for row in matrix:
        if special_symbol in row:
            result = (matrix.index(row), row.index(special_symbol))
            break

    if result:
        print(result)
    else:
        print(f"{special_symbol} does not occur in the matrix")


rows = int(input())
symbol_in_matrix(rows)
