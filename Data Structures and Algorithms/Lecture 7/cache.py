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


def find_root(node, parent):
    while node != parent[node]:
        node = parent[node]

    return node


nodes = int(input())
edges = int(input())

graph = []
max_num = float("-inf")

for _ in range(edges):
    first, second, weight = [int(num) for num in input().split(" - ")]
    graph.append((first, second, weight))
    max_num = max(first, second, max_num)

parent = [num for num in range(max_num + 1)]
total_cost = 0

for first, second, weight in sorted(graph, key=lambda x: x[2]):
    first_root_node = find_root(first, parent)
    second_root_node = find_root(second, parent)

    if first_root_node != second_root_node:
        parent[first_root_node] = second_root_node
        total_cost += weight

print(f"Total cost: {total_cost}")

from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append(Edge(source, destination, weight))

start_node = int(input())
end_node = int(input())

parent = [None] * (nodes + 1)
distance = [float("inf")] * (nodes + 1)
distance[start_node] = 0

for _ in range(nodes - 1):
    updated = False
    for edge in graph:
        if distance[edge.source] == float("inf"):
            continue
        new_distance = distance[edge.source] + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source
            updated = True

    if not updated:
        break

for edge in graph:
    new_distance = distance[edge.source] + edge.weight
    if new_distance < distance[edge.destination]:
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


from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


budget = int(input())
nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes)]
tree = set()

for _ in range(edges):
    edge_data = input().split()
    first, second, weight = int(edge_data[0]), int(edge_data[1]), int(edge_data[2])

    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

    if len(edge_data) == 4:
        tree.add(first)
        tree.add(second)

pq = PriorityQueue()
budget_used = 0

for node in tree:
    for edge in graph[node]:
        pq.put(edge)


while not pq.empty():
    min_edge = pq.get()
    non_tree_node = None

    if min_edge.first in tree and min_edge.second not in tree:
        non_tree_node = min_edge.second
    elif min_edge.first not in tree and min_edge.second in tree:
        non_tree_node = min_edge.first

    if non_tree_node is None:
        continue
    if budget_used + min_edge.weight > budget:
        break

    tree.add(non_tree_node)
    budget_used += min_edge.weight
    for edge in graph[non_tree_node]:
        pq.put(edge)

print(f"Budget used: {budget_used}")
