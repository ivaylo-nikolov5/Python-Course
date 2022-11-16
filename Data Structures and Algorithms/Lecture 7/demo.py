from collections import deque

nodes = int(input())
pairs = int(input())

graph = {}

for _ in range(nodes):
    line = input().split(":")
    source, destination = int(line[0]), [x for x in line[1].split()]

    if source not in graph:
        graph[source] = []

    [graph[source].append(int(x)) for x in destination]

max_num = max(graph.keys())

for _ in range(pairs):
    source, destination = [int(x) for x in input().split("-")]
    parent = [None] * (max_num + 1)
    visited = [False] * (max_num + 1)

    queue = deque([source])
    visited[source] = True

    while queue:
        node = queue.popleft()

        if node == destination:
            break

        visited[node] = True
        for child in graph[node]:
            if visited[child]:
                continue
            visited[child] = True
            parent[child] = node
            queue.appendleft(child)

    counter = -1

    node = destination
    while node:
        counter += 1
        node = parent[node]

    if counter == 0:
        counter = -1

    print("{" + f"{source}, {destination}" + "}" + f" -> {counter}")
