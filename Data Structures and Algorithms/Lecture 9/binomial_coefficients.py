def calc_binomial(n, k, cache):
    key = f"{n} {k}"

    if key in cache:
        return cache[key]

    if k == 0 or n == 0 or k == n:
        return 1

    result = calc_binomial(n - 1, k - 1, cache) + calc_binomial(n - 1, k, cache)
    cache[key] = result

    return result


n = int(input())
k = int(input())
cache = {}

print(calc_binomial(n, k, cache))