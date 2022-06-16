n = int(input())

if n == 1:
    print("*")
else:
    print(" " * (n-1)+"*")

    for i in range (1, n):
        print(" "*(n-(i+1))+"*"+("-*" * i))

    for j in range(2, n):
        print(" "*(j-1) + "*"+"-*"*(n-j))

    print(" " * (n-1)+"*")
