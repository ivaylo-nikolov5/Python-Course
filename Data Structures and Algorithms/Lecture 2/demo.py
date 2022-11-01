class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def find_connected_areas(r, c, ma):
    if r < 0 or c < 0 or r >= len(ma) or c >= len(ma[0]):
        return [r, c, 0]
    elif ma[r][c] != "-":
        return [r, c, 0]

    ma[r][c] = "v"
    result = 1
    result += find_connected_areas(r, c + 1, ma)[2]
    result += find_connected_areas(r, c - 1, ma)[2]
    result += find_connected_areas(r + 1, c, ma)[2]
    result += find_connected_areas(r - 1, c, ma)[2]

    return [r, c, result]


n = int(input())
m = int(input())

matrix = [[x for x in input()] for _ in range(n)]
areas = []

for row in range(n):
    for col in range(m):
        r, c, size = find_connected_areas(row, col, matrix)
        if size <= 0:
            continue
        areas.append(Area(r, c, size))

areas = list(sorted(areas, key=lambda x: -x.size))
area_number = 1

print(f"Total areas found: {len(areas)}")
for x in areas:
    print(f"Area #{area_number} at ({x.row}, {x.col}), size: {x.size}")
    area_number += 1