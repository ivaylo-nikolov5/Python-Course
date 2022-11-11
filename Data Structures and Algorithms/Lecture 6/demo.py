from collections import deque

nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes + 1)]
parents = [None] * (edges + 1)

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start = int(input())
end = int(input())

visited = [False] * (nodes + 1)

queue = deque([start])

while queue:
    node = queue.popleft()
    if node == end:
        break

    for child in graph[node]:
        if visited[child]:
            continue

        visited[child] = True
        queue.appendleft(child)
        parents[child] = node

path = deque()

node = end

while node:
    path.appendleft(node)
    node = parents[node]

print(f"Shortest path length is: {len(path) - 1}")
print(*path, sep=" ")