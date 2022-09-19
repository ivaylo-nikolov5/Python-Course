from itertools import permutations

def possible_permutations(nums):
    for perm in permutations(nums):
        yield list(perm)

[print(n) for n in possible_permutations([1])]