n = int(input())

brackets = 0

for i in range(1, n+1):
    inp = input()
    inp = inp.strip()
    if inp == "(" or inp == ")":
        brackets += 1

if brackets % 2 != 0:
    print("UNBALANCED")
else:
    print("BALANCED")


