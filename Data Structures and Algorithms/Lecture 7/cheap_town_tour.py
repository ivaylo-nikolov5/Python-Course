from collections import deque


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


towns = int(input())
streets = int(input())

graph = []
total_cost = 0

for _ in range(streets):
    source, destination, weight = [int(x) for x in input().split(" - ")]
    graph.append((source, destination, weight))

parent = [x for x in range(towns)]

for first, second, weight in sorted(graph, key=lambda x: x[2]):
    first_node_root = find_root(parent, first)
    second_node_root = find_root(parent, second)

    if first_node_root == second_node_root:
        continue

    parent[first_node_root] = second_node_root
    total_cost += weight

print(f"Total cost: {total_cost}")