def dfs(node, graph, visited, components):
    if visited[node]:
        return

    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited, components)

    components.append(node)

    return components


lines = int(input())

graph = []

for _ in range(lines):
    line = input()
    children = [] if not line else [int(x) for x in line.split()]
    graph.append(children)

visited = [False] * lines

for node in range(len(graph)):
    result = dfs(node, graph, visited, [])
    if result:
        print(f"Connected component: {' '.join(str(x) for x in result)}")