def recursive_drawing(n):
    if n == 0:
        return

    print("*" * n)
    recursive_drawing(n - 1)
    print("#" * n)


lines = int(input())
recursive_drawing(lines)