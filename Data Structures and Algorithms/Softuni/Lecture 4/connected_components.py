def dfs(node, graph, visited, components):
    if visited[node]:
        return components

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, components)

    components.append(node)

    return components

lines = int(input())

graph = []

for _ in range(lines):
    line = input()
    node = [] if not line else [int(x) for x in line.split()]
    graph.append(node)

visited = [False] * lines

for node in range(lines):
    result = dfs(node, graph, visited, [])
    if not result:
        continue
    print(f"Connected component: {' '.join(str(x) for x in result)}")