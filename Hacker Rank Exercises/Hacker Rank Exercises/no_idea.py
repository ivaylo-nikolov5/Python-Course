n_and_m = [int(x) for x in input().split()]
n_integers = [int(x) for x in input().split()]
a_and_b = set(int(x) for x in input().split())
a1_and_b1 = set(int(x) for x in input().split())

happiness = 0
if len(a_and_b) == n_and_m[1] and len(a1_and_b1) == n_and_m[1]:
    for x in a_and_b:
        if x in n_integers:
            happiness += 1
            n_integers.remove(x)
    for x in a1_and_b1:
        if x in n_integers:
            happiness -= 1
            n_integers.remove(x)

print(happiness)

