def calc_fib(number, cache):
    if number in cache:
        return cache[number]

    if number <= 2:
        return 1

    result = calc_fib(number - 1, cache) + calc_fib(number - 2, cache)
    cache[number] = result
    return result


number = int(input())
cache = {}

print(calc_fib(number, cache))


# -----------------------------------------------------------------------------


from collections import deque


def fill_dp(rows, cols, matrix, dp):
    for col in range(1, cols):
        dp[0][col] = matrix[0][col] + dp[0][col - 1]

    for row in range(1, rows):
        dp[row][0] = matrix[row][0] + dp[row - 1][0]

    for row in range(1, rows):
        for col in range(1, cols):
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1]) + matrix[row][col]

    return dp


rows = int(input())
cols = int(input())

matrix = []
dp = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
    dp.append([0] * cols)

dp[0][0] = matrix[0][0]
dp = fill_dp(rows, cols, matrix, dp)

row = rows - 1
col = cols - 1

path = deque()

while row > 0 and col > 0:
    path.appendleft([row, col])
    if dp[row - 1][col] > dp[row][col - 1]:
        row -= 1
    else:
        col -= 1

while col > 0:
    path.appendleft([row, col])
    col -= 1

while row > 0:
    path.appendleft([row, col])
    row -= 1


path.appendleft([0, 0])

print(*path, sep=" ")


# ------------------------------------------------------------------------------------


