def calc_fib(n, cache):
    if n in cache:
        return cache[n]
    elif n <= 1:
        return 1

    result = calc_fib(n - 1, cache) + calc_fib(n - 2, cache)
    cache[n] = result

    return result


number = int(input())
cache = {}

print(calc_fib(number, cache))