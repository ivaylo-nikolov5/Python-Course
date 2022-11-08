def dfs(node, graph, salaries):
    result = 0

    if salaries[node]:
        return salaries[node]
    if not graph[node]:
        return 1

    for child in graph[node]:
        result += dfs(child, graph, salaries)

    salaries[node] = result
    return result


lines = int(input())

graph = []
salaries = [None] * lines

for _ in range(lines):
    line = [x for x in input()]
    children = []
    for x in range(len(line)):
        if line[x] == "Y":
            children.append(x)

    graph.append(children)

total_salary = 0

for node in range(len(graph)):
    result = dfs(node, graph, salaries)
    total_salary += result

print(total_salary)