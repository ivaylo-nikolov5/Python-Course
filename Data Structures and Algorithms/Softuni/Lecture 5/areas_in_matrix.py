def dfs(row, col, matrix, visited, key):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return
    elif matrix[row][col] != key:
        return
    elif visited[row][col]:
        return

    visited[row][col] = True

    dfs(row, col + 1, matrix, visited, key)
    dfs(row + 1, col, matrix, visited, key)
    dfs(row - 1, col, matrix, visited, key)
    dfs(row, col - 1, matrix, visited, key)


rows = int(input())
cols = int(input())

matrix = []
visited = []

for _ in range(rows):
    line = [x for x in input()]
    matrix.append(line)
    visited.append([False] * cols)

areas = {}
total_areas = 0

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        key = matrix[row][col]
        dfs(row, col, matrix, visited, key)

        total_areas += 1

        if key not in areas:
            areas[key] = 0

        areas[key] += 1

areas = dict(sorted(areas.items(), key=lambda x: x[0]))

print(f"Areas: {total_areas}")
for letter, area in areas.items():
    print(f"Letter '{letter}' -> {area}")

