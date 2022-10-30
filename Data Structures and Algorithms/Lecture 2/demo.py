def reverse_array(arr, idx):
    if idx == len(arr) // 2:
        print(*arr, sep=" ")
        return
    arr[idx], arr[-idx - 1] = arr[-idx - 1], arr[idx]
    reverse_array(arr, idx + 1)


array = input().split()
reverse_array(array, 0)