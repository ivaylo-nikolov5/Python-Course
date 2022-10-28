def recursive_number_power(n, p):
    if p == 1:
        return n
    return n * recursive_number_power(n, p - 1)


number = int(input())
power = int(input())
print(recursive_number_power(number, power))

