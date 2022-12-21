def find_pair_with_given_sum(numbers, target):
    pairs = []

    for x in range(len(numbers)):
        for y in range(x + 1, len(numbers) - 1):
            current_sum = numbers[x] + numbers[y]
            if current_sum == target:
                pairs.append((numbers[x], numbers[y]))

    if not pairs:
        print("Pair not found")
        return

    for pair in pairs:
        print(f"Pair found {pair}")


def solution2(numbers, target):
    result = []
    numbers = sorted(numbers)

    start, end = 0, len(numbers) - 1

    while start < end:
        if numbers[start] + numbers[end] == target:
            result.append(f"Pair found: ({numbers[start]}, {numbers[end]})")
            start += 1
            continue

        if numbers[start] + numbers[end] < target:
            start += 1
        else:
            end -= 1

    if not result:
        print("Pair not found")
        return

    for res in result:
        print(res)

solution2([8, 7, 2, 5, 3, 1], 10)