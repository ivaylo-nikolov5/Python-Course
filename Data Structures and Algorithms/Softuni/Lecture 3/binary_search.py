def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = numbers[mid_idx]

        if mid_el == target:
            return mid_idx

        if mid_el < target:
            left = mid_idx + 1
        else:
            right = mid_idx - 1

    return -1


def binary_search2(numbers, target, left, right):

    mid_idx = (left + right) // 2
    if mid_idx >= len(numbers):
        return -1
    mid_el = numbers[mid_idx]

    if mid_el == target:
        return mid_idx

    if mid_el < target:
        return binary_search(numbers, target, mid_idx + 1, right)
    else:
        return binary_search(numbers, target, left, mid_idx - 1)



numbers = [int(x) for x in input().split()]
target = int(input())

print(binary_search(numbers, target))


