def print_up(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(i):
            print(f"* ", end="")
        print()


def print_bottom(n):
    for i in range(1, n):
        print(" " * i, end="")
        for j in range(n - i, 0, -1):
            print(f"* ", end="")
        print()


def print_rhombus(n):
    print_up(n)
    print_bottom(n)


m = int(input())
print_rhombus(m)
