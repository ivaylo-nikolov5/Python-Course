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


find_pair_with_given_sum([8, 7, 2, 5, 3, 1], 10)