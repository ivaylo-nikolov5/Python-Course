def calc_binom(n, k, cache):
    key = f"{n} {k}"
    if key in cache:
        return cache[key]

    if n == 0 or k == 0 or n == k:
        return 1

    result = calc_binom(n - 1, k - 1, cache) + calc_binom(n - 1, k, cache)

    cache[key] = result

    return result


n = int(input())
k = int(input())
cache = {}

print(calc_binom(n, k, cache))


# -------------------------------------------------------------------------------------------------------


first = input()
second = input()

rows = len(first) + 1
cols = len(second) + 1

dp = []
[dp.append([0] * cols) for _ in range(rows)]

for col in range(1, cols):
    dp[0][col] = col

for row in range(1, rows):
    dp[row][0] = row


for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            dp[row][col] = dp[row - 1][col - 1]
        else:
            dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + 1


result = dp[rows - 1][cols - 1]
print(f"Deletions and Insertions: {result}")


# -----------------------------------------------------------------------------------------------


first = [int(x) for x in input().split()]
second = [num for num in range(1, len(first) + 1)]

rows = len(first) + 1
cols = len(second) + 1

dp = []
[dp.append([0] * cols) for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
             dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

result = dp[rows - 1][cols - 1]
print(f"Maximum pairs connected: {result}")


# -----------------------------------------------------------------------------------------------------


