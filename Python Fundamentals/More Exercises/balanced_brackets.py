lines = int(input())
balanced = False
closing = 0
opening = 0
for x in range(lines):
    chars = input()
    if chars == "(":
        closing += 1
    elif x == ")":
        opening += 1

if closing == opening:
    balanced = True

if not balanced:
    print(f"BALANCED")
else:
    print("UNBALANCED")