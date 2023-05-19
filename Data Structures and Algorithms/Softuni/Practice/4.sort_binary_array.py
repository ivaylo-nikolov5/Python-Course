from collections import deque


def brute_force(array):
    sorted_array = deque()

    actions = {
        0: lambda x: sorted_array.appendleft(x),
        1: lambda y: sorted_array.append(y)
    }

    while array:
        el = array.pop()
        actions[el](el)

    print(*sorted_array, sep=", ")


def solution2(numbers: list):
    zeros = numbers.count(0)
    ones = len(numbers) - zeros

    sorted_array = [0] * zeros
    sorted_array.extend([1] * ones)

    print(sorted_array)


def solution3(numbers):
    zeros = numbers.count(0)

    idx = 0
    while zeros:
        numbers[idx] = 0
        idx += 1
        zeros -= 1

    while idx < len(numbers):
        numbers[idx] = 1
        idx += 1

    print(numbers)


def solution4(numbers):
    pivot = 1
    j = 0

    for i in range(len(numbers)):
        if numbers[i] < pivot:
            swap(numbers, i, j)
            j += 1

    print(numbers)


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


solution4([1, 0, 1, 0, 1, 0, 0, 1])
