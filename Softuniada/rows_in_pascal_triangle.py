def pascal_triangle(r):

    if r == 0:
        return ""
    elif r == 1:
        return "1 1"

    current_row = [1, 1]

    for i in range(r - 1):
        current_row = get_row(current_row)

    return  ' '.join(str(num) for num in current_row)


def get_row(current_r):
    next_row = [1]

    i, j = 0, 1

    for _ in range(len(current_r) - 1):
        next_row.append(current_r[i] + current_r[j])
        i += 1
        j += 1

    next_row.append(1)
    return next_row


row = int(input())
print(pascal_triangle(row))

