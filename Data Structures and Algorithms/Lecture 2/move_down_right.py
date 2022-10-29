def move_down_right(row, col, matrix, paths):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    elif row == len(matrix) - 1 and col == len(matrix[0]) - 1:
        return 1

    result = 0
    result += move_down_right(row, col + 1, matrix, paths)
    result += move_down_right(row + 1, col, matrix, paths)

    return result

n = int(input())
m = int(input())

matrix = [[None for _ in range(m)] for _ in range(n)]

print(move_down_right(0, 0, matrix, 0))