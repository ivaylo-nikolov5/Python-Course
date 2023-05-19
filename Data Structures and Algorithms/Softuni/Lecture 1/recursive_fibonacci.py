def iterative_fibonacci(n):
    fib0 = 1
    fib1 = 1
    result = 0
    for num in range(n - 1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result
    return result

def recursive_fibonacci(n):
    if n <= 1:
        return 1
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


number = int(input())
print(recursive_fibonacci(number))

number = int(input())
print(iterative_fibonacci(number))