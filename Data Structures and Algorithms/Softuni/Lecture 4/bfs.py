from collections import deque


def bfs(node, graph, visited):
    if node in visited:
        return

    queue = deque([node])
    visited.add(node)

    while queue:
        print(queue.popleft(), end=" ")
        for child in graph[node]:
            if child not in visited:
                queue.append(child)
                visited.add(child)

graph = {
    7: [19, 21, 14],
    19: [1, 12, 31, 21],
    1: [7],
    12: [],
    31: [21],
    21: [14],
    14: [6, 23],
    23: [21],
    6: []
}

visited = set()

for node in graph:
    bfs(node, graph, visited)
