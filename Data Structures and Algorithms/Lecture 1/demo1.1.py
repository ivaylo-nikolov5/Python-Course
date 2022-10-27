def recursive_array_sum(array, idx):
    if idx == len(array) - 1:
        return array[idx]
    return array[idx] + recursive_array_sum(array, idx + 1)


numbers = [int(x) for x in input().split()]
print(recursive_array_sum(numbers, 0))