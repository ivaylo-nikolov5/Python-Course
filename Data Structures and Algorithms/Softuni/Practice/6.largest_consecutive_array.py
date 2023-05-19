def is_consecutive(array, i, j, min_el, max_el):
    if max_el - min_el != j - i:
        return False

    visited = [False] * (j - i + 1)

    for k in range(i, j + 1):
        if visited[array[k] - min_el]:
            return False

        visited[array[k] - min_el] = True

    return True


def find_max_sublist(array):
    length = 1
    start = end = 0

    for i in range(len(array) - 1):
        min_el = array[i]
        max_el = array[i]

        for j in range(i + 1, len(array)):
            min_el = min(min_el, array[j])
            max_el = max(max_el, array[j])

            if is_consecutive(array, i, j, min_el, max_el):
                if length < max_el - min_el + 1:
                    length = max_el - min_el + 1
                    start = i
                    end = j

    sublist = []

    for i in range(start, end + 1):
        sublist.append(array[i])

    print(f"The largest sublist is {', '.join([str(x) for x in sublist])}")


if __name__ == '__main__':
    A = [2, 0, 2, 1, 4, 3, 1, 0]

    find_max_sublist(A)