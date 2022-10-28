def reverse_array(arr, idx):
    if idx == len(arr) - 1:
        print(*arr, sep=" ")
        return
    arr.append(arr.pop(-idx - 2))
    return reverse_array(arr, idx + 1)


array = [x for x in input().split()]
reverse_array(array, 0)