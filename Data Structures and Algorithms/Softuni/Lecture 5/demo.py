buildings = int(input())
streets = int(input())

print("Important streets:")
graph = [None] * buildings


for _ in range(streets):
    line = input().split(" - ")
    building = int(line[0])
    connected_building = int(line[1])
    if not graph[building]:
        graph[building] = []

    graph[building].append()


