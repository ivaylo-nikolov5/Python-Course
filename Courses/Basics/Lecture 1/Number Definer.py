n = float(input())

if n == 0:
    print("zero")
elif 1 <= n < 1000000:
    print("positive")
elif 0 < n < 1:
    print("small positive")
elif n > 1000000:
    print("large positive")
elif -1 >= n > -1000000:
    print("negative")
elif 0 > n > -1:
    print("small negative")
else:
    print("large negative")

