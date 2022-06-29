n = int(input())
current = 1
is_done = False
for i in range(1, n+1):
    for j in range(1, i+1):
        print(f"{current} ", end="")
        current += 1
        if current > n:
            exit(i)
    print()


