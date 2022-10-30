class Result:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def connected_areas(r, c, ma):
    if r < 0 or c < 0 or r >= len(ma) or c >= len(ma[0]):
        return [r, c, 0]
    elif ma[r][c] != "-":
        return [r, c, 0]

    ma[r][c] = "v"
    result = 1
    result += connected_areas(r, c + 1, ma)[2]
    result += connected_areas(r, c - 1, ma)[2]
    result += connected_areas(r + 1, c, ma)[2]
    result += connected_areas(r - 1, c, ma)[2]

    return [r, c, result]


n = int(input())
m = int(input())

matrix = [[x for x in input()] for _ in range(n)]
areas = []

for row in range(n):
    for col in range(m):
        r, c, size = connected_areas(row, col, matrix)
        if size > 0:
            areas.append(Result(r, c, size))

areas = list(sorted(areas, key=lambda x: -x.size))
print(f"Total areas found: {len(areas)}")
idx = 1
for area in areas:
    print(f"Area #{idx} at ({area.row}, {area.col}), size: {area.size}")
    idx += 1
