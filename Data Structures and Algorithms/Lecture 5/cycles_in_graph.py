graph = {}
acyclic = "Yes"

command = input()
while command != "End":
    node, child = command.split("-")
    if child in graph:
        acyclic = "No"
        break

    graph[node] = child
    command = input()

print(f"Acyclic: {acyclic}")