def find_all_paths(row, col, field):
    if row < 0 or col < 0 or row >= len(field) or col >= len(field[0]):
        return 0
    elif row == len(field) - 1 and col == len(field[0]) - 1:
        return 1

    field[row][col] = "v"

    result = 0
    result += find_all_paths(row, col + 1, field)
    result += find_all_paths(row + 1, col, field)

    field[row][col] = None

    return result


n = int(input())
m = int(input())

matrix = [[None for _ in range(m)] for _ in range(n)]
print(find_all_paths(0, 0, matrix))