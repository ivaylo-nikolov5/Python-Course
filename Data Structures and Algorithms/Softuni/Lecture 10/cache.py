from collections import deque


def dfs(node, graph, visited, result):
    if node in visited:
        return

    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited, result)

    result.appendleft(node)

graph = {}

while True:
    command = input()
    if command == "End":
        break

    explode = command.split("->")
    node = explode[0].strip()
    children = [] if len(explode) == 1 else [x for x in explode[1].strip().split()]

    graph[node] = children

visited = set()
result = deque()

for node in graph:
    dfs(node, graph, visited, result)

print(*result)


# --------------------------------------------------------------------------------


from collections import deque

first = [int(x) for x in input().split()]
second = [int(x) for x in input().split()]

rows = len(first) + 1
cols = len(second) + 1

dp = []
[dp.append([0] * cols) for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

result = deque()

row = rows - 1
col = cols - 1

while row > 0 and col > 0:
    if first[row - 1] == second[col - 1]:
        result.appendleft(first[row - 1])
        row -= 1
        col -= 1
    elif dp[row - 1][col] > dp[row][col - 1]:
        row -= 1
    else:
        col -= 1

print(*result)
print(len(result))


# --------------------------------------------------------------------------------------------------


from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


def calc_damage(jumps, damage):
    for _ in range(jumps):
        damage //= 2

    return damage


def prim(node, graph, damage, damage_by_node):
    damage_by_node[node] += damage
    tree = {node}
    jumps = [0] * len(graph)

    pq = PriorityQueue()
    [pq.put(edge) for edge in graph[node]]

    while not pq.empty():
        min_node = pq.get()
        tree_node, non_tree_node = -1, -1

        if min_node.first in tree and min_node.second not in tree:
            non_tree_node = min_node.second
            tree_node = min_node.first
        elif min_node.first not in tree and min_node.second in tree:
            non_tree_node = min_node.first
            tree_node = min_node.second

        if non_tree_node == -1:
             continue

        tree.add(non_tree_node)

        for child in graph[non_tree_node]:
            pq.put(child)

        jumps[non_tree_node] = jumps[tree_node] + 1
        damage_by_node[non_tree_node] += calc_damage(jumps[non_tree_node], damage)


nodes = int(input())
edges = int(input())
lightnings = int(input())

graph = {node: [] for node in range(nodes)}

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split()]
    edge = Edge(first, second, weight)

    if edge not in graph[first]:
        graph[first].append(edge)
    if edge not in graph[second]:
        graph[second].append(edge)

damage_by_node = [0] * nodes

for _ in range(lightnings):
    node, damage = [int(x) for x in input().split()]
    prim(node, graph, damage, damage_by_node)

print(max(damage_by_node))


