def find_nodes_with_edges(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child in result:
                result[child] += 1
            else:
                result[child] = 1

    return result


def find_nodes_dependencies(nodes_with_dependencies):
    for node, dependencies in nodes_with_dependencies.items():
        if dependencies == 0:
            return node

    return None


lines = int(input())

graph = {}

for _ in range(lines):
    line = input().split("->")
    node = line[0].strip()
    children = [] if not line[1].strip() else [x for x in line[1].strip().split(", ")]
    graph[node] = children

nodes_with_edges = find_nodes_with_edges(graph)
sorted_nodes = []
has_cycles = False

while nodes_with_edges:
    node_to_remove = find_nodes_dependencies(nodes_with_edges)
    if node_to_remove is None:
        has_cycles = True
        break

    sorted_nodes.append(node_to_remove)
    nodes_with_edges.pop(node_to_remove)
    for child in graph[node_to_remove]:
        nodes_with_edges[child] -= 1


if has_cycles:
    print("Invalid topological sorting")
else:
    print(f"Topological sorting: {', '.join(str(x) for x in sorted_nodes)}")