from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, percentage):
        self.source = source
        self.destination = destination
        self.percentage = percentage


nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes)]

for _ in range(edges):
    source, destination, percentage = [int(x) for x in input().split()]
    edge = Edge(source, destination, percentage)

    graph[source].append(edge)
    graph[destination].append(edge)

start = int(input())
end = int(input())
parent = [None] * len(graph)
percentages = [float("-inf")] * len(graph)

percentages[start] = 100
pq = PriorityQueue()
pq.put((-100, start))

while not pq.empty():
    max_percentage, node = pq.get()

    if node == end:
        break

    for edge in graph[node]:
        child = edge.destination if edge.source == node else edge.source
        new_percentage = -max_percentage * edge.percentage / 100
        if new_percentage > percentages[child]:
            percentages[child] = new_percentage
            parent[child] = node
            pq.put((-new_percentage, child))


path_reliability = percentages[end]
print(f"Most reliable path reliability: {path_reliability:.2f}%")

path = deque()
node = end
while node:
    path.appendleft(node)
    node = parent[node]
path.appendleft(start)
print(*path, sep=" -> ")


