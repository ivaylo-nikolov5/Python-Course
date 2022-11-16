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
