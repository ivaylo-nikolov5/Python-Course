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


# ---------------------------------------------------------------------

# That's a solution with swapping letters and finding the quickest way to equalize the words:

first = [el for el in input()]
second = [el for el in input()]

insertions_and_deletions = 0

for first_idx in range(len(first)):
    if second[first_idx] == first[first_idx]:
        continue

    for sec_idx in range(len(second)):
        if second[sec_idx] == first[first_idx]:
            second[sec_idx], second[first_idx] = second[first_idx], second[sec_idx]
            insertions_and_deletions += 2


while len(first) != len(second):
    if len(first) < len(second):
        insertions_and_deletions += len(second) - len(first)
        first.extend(second[len(first):])
    else:
        insertions_and_deletions += len(first) - len(second)
        second.extend(first[len(second):])


for idx in range(len(first)):
    if first == second:
        break
    elif first[idx] == second[idx]:
        continue

    first[idx] = second[idx]
    insertions_and_deletions += 2

print(f"Deletions and Insertions: " + str(insertions_and_deletions))