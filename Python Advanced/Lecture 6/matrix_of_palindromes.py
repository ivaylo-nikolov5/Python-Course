def matrix_of_palindromes(r, c):
    for row in range(r):
        for col in range(c):
            print(f"{chr(97 + row)}{chr(97 + row + col)}{chr(97 + row)}", end=" ")
        print()


rows, cols = [int(x) for x in input().split()]
matrix_of_palindromes(rows, cols)

