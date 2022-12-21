def solution(numbers, idx, subarray):
    for i in range(idx, len(numbers)):
        number = numbers[i]
        subarray.append(number)
        solution(numbers, i + 1, subarray)

        if sum(subarray) == 0 and len(subarray) > 0:
            return True

        subarray.pop()


def hashing(numbers):
    sums = set()

    total = 0

    for num in numbers:
        total += num

        if total in sums:
            return True

        sums.add(total)

    return False


result = hashing([4, -6, 3, -1, 4, 2, 7])

if result:
    print("Subarray with zero-sum exists")
else:
    print("Subarray with zero-sum doesn't exist")



