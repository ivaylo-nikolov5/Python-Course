n = int(input())
a = 2*n

if n ==2:
    print("%" * a)
    print("%" + "**" + "%")
    print("%" * a)
else:

    print("%"*a)

    num_rows = n

    if n % 2 == 0:
        num_rows -=1

    for i in range(0, num_rows-1):
        print("%"+ " "* (a-2)+ "%")

        if i == num_rows//2 -1:
            print("%"+ " "*(n-2)+"**"+ " "*(n-2)+ "%")

    print("%"*a)