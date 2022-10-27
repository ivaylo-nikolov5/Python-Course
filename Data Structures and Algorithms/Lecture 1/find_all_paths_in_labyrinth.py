def find_all_paths(lab, row, col, direction, path):
    if row < 0 or col < 0:
        return
    elif row >= len(lab) or col >= len(lab[0]):
        return
    elif lab[row][col] == "v" or lab[row][col] == "*":
        return

    path.append(direction)

    if lab[row][col] == "e":
        print(*path, sep="")
    else:
        lab[row][col] = "v"
        find_all_paths(lab, row, col + 1, "R", path)
        find_all_paths(lab, row, col - 1, "L", path)
        find_all_paths(lab, row + 1, col, "D", path)
        find_all_paths(lab, row - 1, col, "U", path)
        lab[row][col] = "-"

    path.pop()


rows = int(input())
cols = int(input())

field = [[x for x in input()] for _ in range(rows)]
find_all_paths(field, 0, 0, "", [])