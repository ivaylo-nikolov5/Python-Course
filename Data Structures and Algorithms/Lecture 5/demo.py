def dfs(node, destination, graph, visited):
    if node in visited:
        return

    visited.add(node)

    if node == destination:
        return

    for child in graph[node]:
        dfs(child, destination, graph, visited)


def path_exists(source, destination, graph):
    visited = set()

    dfs(source, destination, graph, visited)

    return destination in visited


lines = int(input())

graph = {}
edges = []
edges_to_remove = []

for _ in range(lines):
    line = input().split(" -> ")
    node = line[0]
    children = [x for x in line[1].split()]
    graph[node] = children
    for child in children:
        edges.append((node, child))

for source, destination in list(sorted(edges, key=lambda x: (x[0], x[1]))):
    if source not in graph[destination] or destination not in graph[source]:
        continue

    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exists(source, destination, graph):
        edges_to_remove.append((source, destination))
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f"Edges to remove: {len(edges_to_remove)}")

for x, y in edges_to_remove:
    print(f"{x} - {y}")
