import re

text = input()
mirror_dict = dict()

pattern = r"(#|@)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"

regex = re.finditer(pattern, text)

counter = 0
for x in regex:
    counter += 1
    first = x.group(2)
    second = x.group(3)
    if first == second[::-1]:
        mirror_dict[x.group(2)] = x.group(3)

result = []
if counter > 0:
    print(f"{counter} word pairs found!")
    if len(mirror_dict) > 0:
        print("The mirror words are:")
        for x in mirror_dict:
            result.append(f"{x} <=> {mirror_dict[x]}")
    else:
        print("No mirror words!")

    print(*result, sep=", ")
else:
    print("No word pairs found!")
    print("No mirror words!")
