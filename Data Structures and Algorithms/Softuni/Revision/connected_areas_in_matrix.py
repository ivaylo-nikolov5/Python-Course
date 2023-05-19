class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def is_inside(row, col, rows, cols):
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return False
    return True


def find_connected_areas(row, col, rows, cols, matrix, size):
    if not is_inside(row, col, rows, cols) or matrix[row][col] != "-":
        return 0

    matrix[row][col] = "v"
    size += 1

    size += find_connected_areas(row, col + 1, rows, cols, matrix, 0)
    size += find_connected_areas(row + 1, col, rows, cols, matrix, 0)
    size += find_connected_areas(row, col - 1, rows, cols, matrix, 0)
    size += find_connected_areas(row - 1, col, rows, cols, matrix, 0)

    return size

rows = int(input())
cols = int(input())

matrix = []

for _ in range(rows):
    matrix.append([x for x in input()])

areas = []

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == "*":
            continue
        size = find_connected_areas(row, col, rows, cols, matrix, 0)
        if size == 0:
            continue

        areas.append(Area(row, col, size))

areas = list(sorted(areas, key=lambda x: (-x.size, x.row)))
area_number = 1
print(f"Total areas found: {len(areas)}")

for area in areas:
    print(f"Area #{area_number} at ({area.row}, {area.col}), size: {area.size}")
    area_number += 1