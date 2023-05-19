from collections import deque


def dfs(node, graph, visited, result):
    if node in visited:
        return node

    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, result)

    result.appendleft(node)
    return result

graph = {}

command = input()

while command != "End":
    explode = command.split("->")
    node = explode[0].strip()
    children = [] if not explode[1] else explode[1].strip().split()
    graph[node] = children

    command = input()

result = deque()
visited = set()

for node in graph:
    dfs(node, graph, visited, result)

print(*result)