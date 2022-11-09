def dfs(row, col, graph, visited, key):
    if row < 0 or col < 0 or row >= len(graph) or col >= len(graph[0]):
        return
    elif visited[row][col]:
        return
    elif graph[row][col] != key:
        return

    visited[row][col] = True

    dfs(row, col + 1, graph, visited, key)
    dfs(row + 1, col, graph, visited, key)
    dfs(row, col - 1, graph, visited, key)
    dfs(row - 1, col, graph, visited, key)


rows = int(input())
cols = int(input())

graph = []
visited = []

for _ in range(rows):
    graph.append([x for x in input()])
    visited.append([None] * cols)


areas = 0
letters_with_areas = {}

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue

        key = graph[row][col]
        dfs(row, col, graph, visited, key)
        areas += 1

        if key not in letters_with_areas:
            letters_with_areas[key] = 0
        letters_with_areas[key] += 1

letters_with_areas = dict(sorted(letters_with_areas.items(), key=lambda x: x[0]))

print(f"Areas: {areas}")
for key, value in letters_with_areas.items():
    print(f"Letter '{key}' -> {value}")