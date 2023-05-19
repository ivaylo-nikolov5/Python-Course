def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = numbers[mid_idx]
        if target == mid_el:
            return mid_idx
        elif mid_el < target:
            left = mid_idx + 1
        else:
            right = mid_idx - 1
    return -1


numbers = [int(x) for x in input().split()]
target = int(input())

idx = binary_search(numbers, target)
print(idx)