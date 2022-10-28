def reverse_array(arr, idx):
    if idx == len(arr) // 2:
        return
    arr[idx], arr[-idx - 1] = arr[-idx - 1], arr[idx]
    reverse_array(arr, idx + 1)


array = [x for x in input().split()]
reverse_array(array, 0)

print(*array, sep=" ")