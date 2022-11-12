class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


def find_root(parent, element):
    while element != parent[element]:
        element = parent[element]

    return element


edges = int(input())

graph = []

max_node = float("-inf")

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(", ")]
    graph.append(Edge(source, destination, weight))
    max_node = max(source, destination, max_node)

parent = [x for x in range(max_node + 1)]

forest = []

for edge in sorted(graph, key=lambda x: x.weight):
    first_root_node = find_root(parent, edge.source)
    second_root_node = find_root(parent, edge.destination)

    if first_root_node != second_root_node:
        parent[first_root_node] = second_root_node
        forest.append(edge)

for edge in forest:
    print(f"{edge.source} - {edge.destination}")

