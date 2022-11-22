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


