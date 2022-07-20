def snake_moves(r, c):
    word = input()
    idx = 0

    for row in range(r):
        row_elements = []
        for col in range(c):
            row_elements.append(word[idx % len(word)])
            idx += 1

        if row % 2 == 0:
            print(*row_elements, sep="")
        else:
            print(*list(reversed(row_elements)), sep="")

rows, cols = [int(x) for x in input().split()]
snake_moves(rows, cols)
