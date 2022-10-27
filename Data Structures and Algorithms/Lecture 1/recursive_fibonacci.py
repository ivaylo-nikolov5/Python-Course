def iterative_fibonacci(n):
    fib0 = 1
    fib1 = 1
    result = 0
    for num in range(n - 1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result
    return result

number = int(input())
print(iterative_fibonacci(number))