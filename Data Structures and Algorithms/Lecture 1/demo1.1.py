def recursive_factorial(n):
    if n == 0:
        return 1
    return n * recursive_factorial(n - 1)


number = int(input())
print(recursive_factorial(number))