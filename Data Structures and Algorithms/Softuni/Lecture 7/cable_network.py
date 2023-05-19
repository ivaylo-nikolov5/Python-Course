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
    line = input().split()
    first, second, weight = int(line[0]), int(line[1]), int(line[2])

    edge = Edge(first, second, weight)

    graph[first].append(edge)
    graph[second].append(edge)

    if len(line) == 4:
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

    budget_used += min_edge.weight
    tree.add(non_tree_node)
    for edge in graph[non_tree_node]:
        pq.put(edge)


print(f"Budget used: {budget_used}")

