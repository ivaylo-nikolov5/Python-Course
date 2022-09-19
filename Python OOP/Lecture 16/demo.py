from itertools import permutations


def possible_permutations(nums):
    for permutation in permutations(nums):
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]