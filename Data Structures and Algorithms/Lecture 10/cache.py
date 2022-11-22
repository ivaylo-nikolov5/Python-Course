from collections import deque


def dfs(node, graph, visited, result):
    if node in visited:
        return

    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited, result)

    result.appendleft(node)

graph = {}

while True:
    command = input()
    if command == "End":
        break

    explode = command.split("->")
    node = explode[0].strip()
    children = [] if len(explode) == 1 else [x for x in explode[1].strip().split()]

    graph[node] = children

visited = set()
result = deque()

for node in graph:
    dfs(node, graph, visited, result)

print(*result)


# --------------------------------------------------------------------------------


from collections import deque

first = [int(x) for x in input().split()]
second = [int(x) for x in input().split()]

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

result = deque()

row = rows - 1
col = cols - 1

while row > 0 and col > 0:
    if first[row - 1] == second[col - 1]:
        result.appendleft(first[row - 1])
        row -= 1
        col -= 1
    elif dp[row - 1][col] > dp[row][col - 1]:
        row -= 1
    else:
        col -= 1

print(*result)
print(len(result))


# --------------------------------------------------------------------------------------------------




