def draw_rocket(n):
    x = ((n + 4) // 2)
    print("_" * x + "^" + "_" * x)
    print("_" * (x - 1) + "/|\\" + "_" * (x - 1))
    print("_" * (x - 2) + "/|||\\" + "_" * (x - 2))

    j = 1
    for i in range(n // 2 - 1, -1, -1):
        print("_" * i + "/" + "." * j + "|||" + "." * j + "\\" + "_" * i)
        j += 1

    print("_/" + "." * ((n // 2) - 1) + "|||" + "." * ((n // 2) - 1) + "\\_")

    j = (n // 2) + 1
    sym = "|||"
    for i in range(n + 1):
        if i == n:
            sym = "~~~"
        print("_" * j + sym + "_" * j)

    j = n // 2
    for i in range(n // 2):
        print("_" * j + "//" + "." * i + "!" + "." * i + "\\\\" + "_" * j)
        j -= 1

n = int(input())
draw_rocket(n)