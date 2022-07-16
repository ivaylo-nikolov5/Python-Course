rows = int(input())

matrix = [[j for j in input()] for i in range(rows)]
searched_symbol = input()
is_found = False

for row_index in range(rows):
    for col_index in range(rows):
        if matrix[row_index][col_index] == searched_symbol:
            is_found = True
            print(f"({row_index}, {col_index})")
            exit()


if not is_found:
    print(f"{searched_symbol} does not occur in the matrix")