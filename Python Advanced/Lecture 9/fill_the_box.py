def fill_the_box(h, l, w, *args):
    size = h * l * w
    size_copy = size
    for cube in args:
        if cube == "Finish":
            break

        if size - cube >= 0:
            size -= cube
        else:
            size = 0
            cube -= size

    all_cubes = [x for x in args if x != "Finish"]

    if size:
        return f"There is free space in the box. You could put {size} more cubes."

    diff = sum(all_cubes) - size_copy
    return f"No more free space! You have {diff} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
