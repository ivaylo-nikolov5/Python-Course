def create_sequence(n):
    sequence = [0, 1]
    for i in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence[:n]


def find_index(sequence: list, n):
    try:
        return f"The number - {n} is at index {sequence.index(n)}"
    except ValueError:
        return f"The number {n} is not in the sequence"