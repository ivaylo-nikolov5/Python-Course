from collections import deque


def bfs(node, graph, visited):
    if node in visited:
        return

    queue.appendleft(node)
    visited.add(node)

    while queue:
        n = queue.popleft()
        print(n, end=" ")
        for child in graph[n]:
            if child not in visited:
                print(child, end=" ")
                visited.add(child)

    return visited

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

queue = deque()
visited = set()

for node in graph:
    bfs(node, graph, visited)