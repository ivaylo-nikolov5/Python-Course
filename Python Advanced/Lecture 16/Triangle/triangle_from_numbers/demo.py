def print_up(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def print_bottom(n):
    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def print_triangle(n):
    print_up(n)
    print_bottom(n)



if __name__ == "__main__":
    print_triangle(3)