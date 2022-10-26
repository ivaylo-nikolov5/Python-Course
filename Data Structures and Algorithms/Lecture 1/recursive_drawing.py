def recursive_drawing(start, stop, symbol):
    if symbol == "*":
        for i in range(start, stop, -1):
            print(symbol * i)

        return recursive_drawing(1, start, "#")

    for i in range(start, stop + 1):
        print(symbol * i)


rows = int(input())
recursive_drawing(rows, 0, "*")