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


def sorting(numbers, target):
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


def hashing(numbers, target):
    pairs = []
    hashes = {}

    for i, e in enumerate(numbers):
        if target - e in hashes:
            pairs.append(f"Pair found: ({e}, {target - e})")
            continue

        hashes[e] = i

    if not pairs:
        print("Pair not found")
        return

    for pair in pairs:
        print(pair)


hashing([8, 7, 2, 5, 3, 1], 10)
