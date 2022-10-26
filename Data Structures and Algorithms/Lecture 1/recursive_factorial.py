def recursive_factorial(number, iterations, n):
    if number == iterations:
        return n
    iterations += 1
    return recursive_factorial(number, iterations, n * iterations)


num = int(input())
print(recursive_factorial(num, 0, 1))

