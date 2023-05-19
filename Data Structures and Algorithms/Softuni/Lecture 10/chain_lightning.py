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


def prim(node, damage, damage_by_node, graph):
    damage_by_node[node] += damage
    tree = {node}
    jumps = [0] * len(graph)

    pq = PriorityQueue()
    [pq.put(edge) for edge in graph[node]]

    while not pq.empty():
        min_edge = pq.get()
        tree_node, not_tree_node = -1, -1

        if min_edge.first in tree and min_edge.second not in tree:
            tree_node, not_tree_node = min_edge.first, min_edge.second
        elif min_edge.first not in tree and min_edge.second in tree:
            tree_node, not_tree_node = min_edge.second, min_edge.first

        if not_tree_node == -1:
            continue

        tree.add(not_tree_node)
        [pq.put(edge) for edge in graph[not_tree_node]]

        jumps[not_tree_node] = jumps[tree_node] + 1
        damage_by_node[not_tree_node] += calc_damage(jumps[not_tree_node], damage)

nodes = int(input())
edges = int(input())
lightnings = int(input())

graph = {node: [] for node in range(nodes)}

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    edge = Edge(source, destination, weight)

    if edge not in graph[source]:
        graph[source].append(edge)
    if edge not in graph[destination]:
        graph[destination].append(edge)

damage_by_node = [0] * nodes

for _ in range(lightnings):
    node, damage = [int(x) for x in input().split()]
    prim(node, damage, damage_by_node, graph)


print(max(damage_by_node))