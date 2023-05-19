from collections import deque

nodes = int(input())
pairs = int(input())

graph = {}
max_num = float("-inf")

for _ in range(nodes):
    node = input().split(":")
    parent = int(node[0])
    children = [] if not node[1].strip() else [int(x) for x in node[1].split(" ")]
    graph[parent] = children

    if children:
        max_num = max(parent, max(children), max_num)
    else:
        max_num = max(parent, max_num)

for _ in range(pairs):
    parents = [None] * (max_num + 1)
    visited = [False] * (max_num + 1)
    source, destination = [int(x) for x in input().split("-")]

    visited[source] = True

    queue = deque([source])

    while queue:
        node = queue.popleft()
        if node == destination:
            break

        for child in graph[node]:
            if visited[child]:
                continue

            visited[child] = True
            parents[child] = node
            queue.append(child)

    length = 0
    node = destination

    while node:
        length += 1
        node = parents[node]

    length = length if length > 1 else 0
    print("{" + f"{source}, {destination}" + "}" + f" -> {length - 1}")