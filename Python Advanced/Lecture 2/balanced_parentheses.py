expression = input()

opening_brackets = []
balanced = True

for ch in expression:
    if ch in "([{":
        opening_brackets.append(ch)
    elif ch in ")]}":
        if not opening_brackets:
            balanced = False
            break

        if f"{opening_brackets[-1]}{ch}" in "()[]{}":
            opening_brackets.pop()
        else:
            balanced = False
            break

if balanced and not opening_brackets:
    print("YES")
else:
    print("NO")