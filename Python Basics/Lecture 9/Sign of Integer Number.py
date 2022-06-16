n = int(input())


def print_sign(num):
    if num > 0:
        print(f"The number {num} is positive.")
    elif num == 0:
        print(f"The number {num} is zero.")
    else:
        print(f"The number {num} is negative.")


print_sign(n)
