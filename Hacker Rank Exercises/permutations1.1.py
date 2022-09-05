from itertools import permutations

string, length = [x for x in input().split()]

perms = list(sorted(permutations(string, int(length))))

res = ""

for perm in perms:
    res += f"\n{''.join(perm)}"

print(res.strip())
