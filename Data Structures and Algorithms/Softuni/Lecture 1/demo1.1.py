def recursive_lcm(n, m):
    if n % m == 0:
        return m
    elif m % n == 0:
        return n
    return m * n


number1 = int(input())
number2 = int(input())

print(recursive_lcm(number1, number2))