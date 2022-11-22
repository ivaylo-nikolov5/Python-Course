def recursive_array_sum(array, idx):
    result = 0

    if idx == len(array):
        return result

    return array[idx] + recursive_array_sum(array, idx + 1)


array = [int(num) for num in input().split()]

array_sum = recursive_array_sum(array, 0)
print(array_sum)