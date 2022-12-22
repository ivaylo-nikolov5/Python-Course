def brute_force(numbers):
    # time complexity O(N^2)
    repeating_number = None

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                repeating_number = numbers[i]
                break

    if not repeating_number:
        print("There is no duplicate element")
    else:
        print(f"The duplicate element is {repeating_number}")


def hashing(numbers):
    # time complexity O(N)

    visited = []

    for num in numbers:
        if num in visited:
            print(f"The duplicate element is {num}")
            return
        visited.append(num)

    print("There is no duplicate element")


def sorting(numbers):
    numbers = sorted(numbers)

    for idx in range(1, len(numbers)):
        if numbers[idx] == numbers[idx - 1]:
            print(f"The duplicate element is {numbers[idx]}")
            return

    print("There is no duplicate element")


hashing([1, 2, 3, 1, 4, 3])