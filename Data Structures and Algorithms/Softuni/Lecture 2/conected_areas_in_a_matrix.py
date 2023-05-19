def connected_areas(row, col, ma):
    if row < 0 or col < 0 or row >= len(ma) or col >= len(ma[0]):
        return 0
    elif ma[row][col] != "-":
        return 0

    ma[row][col] = "v"

    result = 1
    result += connected_areas(row, col + 1, ma)
    result += connected_areas(row, col - 1, ma)
    result += connected_areas(row + 1, col, ma)
    result += connected_areas(row - 1, col, ma)

    return result


rows = int(input())
cols = int(input())

matrix = [[x for x in input()] for _ in range(rows)]

areas_found = 0
area = 1
result = []

for row in range(rows):
    for col in range(cols):
        res = connected_areas(row, col, matrix)
        if res > 0:
            areas_found += 1
            result.append(f"Area #{area} at ({row}, {col}), size: {res}")
            area += 1

result.insert(0, f"Total areas found: {areas_found}")

print(result[0])

result = list(sorted(result[1:], key=lambda x: -int(x.split()[-1])))
area = 1
new_result = []
for res in result:
    ex = res.split()
    ex[1] = f"#{area}"
    area += 1
    new_result.append(" ".join(ex))

print(*new_result, sep="\n")

