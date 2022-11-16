from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes)]
parent = [None] * nodes
distance = [float("-inf")] * nodes

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    edge = Edge(source, destination, weight)

    graph[source].append(edge)
    graph[destination].append(edge)

start_node = int(input())
end_node = int(input())

distance[start_node] = 100

pq = PriorityQueue()
pq.put((-100, start_node))

while not pq.empty():
    max_distance, node = pq.get()

    if node == end_node:
        break

    for edge in graph[node]:
        child = edge.destination if edge.source == node else edge.source
        new_distance = -max_distance * edge.weight / 100
        if new_distance > distance[child]:
            distance[child] = new_distance
            parent[child] = node
            pq.put((-new_distance, child))

print(f"Most reliable path reliability: {distance[end_node]:.2f}%")

path = deque()
node = end_node

while node:
    path.appendleft(node)
    node = parent[node]
path.appendleft(start_node)
print(*path, sep=" -> ")

