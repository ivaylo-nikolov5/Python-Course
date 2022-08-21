def print_upper_part(row, col):
    rows = row // 2
    hyphens = (col - 3) // 2
    for r in range(1, rows + 1):
        print(f"{'-'*hyphens}{'.|.'*(r * 2 - 1)}{'-'*hyphens}")
        hyphens -= 3


def print_welcome_part(col):
    hyphens = (col - 7) // 2
    print(f"{'-' * hyphens}WELCOME{'-' * hyphens}")


def print_bottom_part(row, col):
    rows = row // 2
    hyphens = 3
    for r in range(rows, 0, -1):
        print(f"{'-' * hyphens}{'.|.' * (r * 2 - 1)}{'-' * hyphens}")
        hyphens += 3


size = [int(x) for x in input().split()]
rows, cols = size[0], size[1]

print_upper_part(rows, cols)
print_welcome_part(cols)
print_bottom_part(rows, cols)

