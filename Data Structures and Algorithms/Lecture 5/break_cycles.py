def dfs(node, graph, destination, visited):
    if node in visited:
        return

    visited.add(node)
    if node == destination:
        return

    for child in graph[node]:
        dfs(child, graph, destination, visited)


def path_exists(source, destination, graph):
    visited = set()

    dfs(source, graph, destination, visited)

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


for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination in graph[source] and source in graph[destination]:
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