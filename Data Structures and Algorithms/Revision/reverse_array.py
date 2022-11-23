def reverse_array(array, mid, idx):
    if idx == mid:
        return array

    array[idx], array[-idx - 1] = array[-idx - 1], array[idx]
    return reverse_array(array, mid, idx + 1)


array = input().split()

mid = len(array) // 2

print(*reverse_array(array, mid, 0))