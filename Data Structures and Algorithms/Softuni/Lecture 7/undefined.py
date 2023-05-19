from collections import deque


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split()]
    graph.append(Edge(first, second, weight))


start_node = int(input())
end_node = int(input())

distance = [float("inf")] * (nodes + 1)
distance[start_node] = 0

parent = [None] * (nodes + 1)

for _ in range(nodes - 1):
    updated = False
    for edge in graph:
        if distance[edge.first] == float("inf"):
            continue
        new_distance = distance[edge.first] + edge.weight
        if new_distance < distance[edge.second]:
            distance[edge.second] = new_distance
            parent[edge.second] = edge.first
            updated = True

    if not updated:
        break

for edge in graph:
    new_distance = distance[edge.first] + edge.weight
    if new_distance < distance[edge.second]:
        print("Undefined")
        break
else:
    path = deque()
    node = end_node
    while node:
        path.appendleft(node)
        node = parent[node]

    print(*path, sep=" ")
    print(distance[end_node])
