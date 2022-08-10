def create_sequence(n):
    sequence = [0, 1]
    for i in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence[:n]


def locate_num(sequence: list, num):
    if num in sequence:
        idx = sequence.index(num)
        return f"The number - {num} is at index {idx}"

    return f"The number {num} is not in the sequence"


if __name__ == "__main__":
    print(locate_num([1, 3, 4, 5, 6], 2))