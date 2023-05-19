def brute_force(numbers):
    for i in range(0, len(numbers)):
        current = [numbers[i]]
        for j in range(i + 1, len(numbers)):
            current.append(numbers[j])

            if sum(current) == 0:
                print(current)



nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

