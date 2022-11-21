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


replacement_cost = int(input())
insert_cost = int(input())
delete_cost = int(input())

first = input()
second = input()

rows = len(first) + 1
cols = len(second) + 1

dp = []
for _ in range(rows):
    dp.append([0] * cols)

for col in range(1, cols):
    dp[0][col] = dp[0][col - 1] + insert_cost

for row in range(1, rows):
    dp[row][0] = dp[row - 1][0] + delete_cost


for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            dp[row][col] = dp[row - 1][col - 1]
            continue
        dp[row][col] = min(dp[row][col - 1] + insert_cost, dp[row - 1][col] + delete_cost,
                           dp[row - 1][col - 1] + replacement_cost)


result = dp[rows - 1][cols - 1]

print(f"Minimum edit distance: {result}")


# -----------------------------------------------------------------------------------------------


from collections import deque

words = input().split()

size = [0] * len(words)
size[0] = 1
parent = [None] * len(words)
best_idx = 0
best_size = 0

for idx in range(1, len(words)):
    current_word = words[idx]
    current_best_size = 0
    current_parent = None
    for prev in range(idx - 1, -1 , -1):
        prev_word = words[prev]
        if len(prev_word) >= len(current_word):
            continue

        if size[prev] + 1 >= current_best_size:
            current_best_size = size[prev] + 1
            current_parent = prev

    size[idx] = current_best_size
    parent[idx] = current_parent

    if current_best_size > best_size:
        best_size = current_best_size
        best_idx = idx


result = deque()

while best_idx is not None:
    result.appendleft(words[best_idx])
    best_idx = parent[best_idx]

print(*result)


# ------------------------------------------------------------------------------------------------



