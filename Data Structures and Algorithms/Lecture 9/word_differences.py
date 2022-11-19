first = input()
second = input()

rows = len(second) + 1
cols = len(first) + 1

dp = [[0] * cols for _ in range(rows)]

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