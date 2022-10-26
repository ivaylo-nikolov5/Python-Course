def draw_recursion(n):
    if n == 0:
        return

    print("*" * n)
    draw_recursion(n - 1)
    print("#" * n)

a = int(input())
draw_recursion(a)