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


first = input()
second = input()

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

print(dp[rows - 1][cols - 1])

# ----------------------------------------------------------------------------------------------

first = input()
second = input()

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

print(dp[rows - 1][cols - 1])

# --------------------------------------------------------------------------------------------


from collections import deque

nums = [int(x) for x in input().split()]

size = [0] * len(nums)
size[0] = 1
parent = [None] * len(nums)
best_idx = 0
best_size = 1

for current in range(1, len(nums)):
    current_num = nums[current]
    current_best_size = 1
    current_parent = None

    for prev in range(current - 1, -1, -1):
        prev_number = nums[prev]
        if prev_number >= current_num:
            continue

        if size[prev] + 1 >= current_best_size:
            current_best_size = size[prev] + 1
            current_parent = prev

    size[current] = current_best_size
    parent[current] = current_parent

    if current_best_size > best_size:
        best_size = current_best_size
        best_idx = current

result = deque()

while best_idx is not None:
    result.appendleft(nums[best_idx])
    best_idx = parent[best_idx]

print(*result, sep=" ")