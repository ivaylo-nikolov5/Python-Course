first = [el for el in input()]
second = [el for el in input()]

insertions_and_deletions = 0

for first_idx in range(len(first)):
    if second[first_idx] == first[first_idx]:
        continue

    for sec_idx in range(len(second)):
        if second[sec_idx] == first[first_idx]:
            second[sec_idx], second[first_idx] = second[first_idx], second[sec_idx]
            insertions_and_deletions += 2


while len(first) != len(second):
    if len(first) < len(second):
        insertions_and_deletions += len(second) - len(first)
        first.extend(second[len(first):])
    else:
        insertions_and_deletions += len(first) - len(second)
        second.extend(first[len(second):])


for idx in range(len(first)):
    if first == second:
        break
    elif first[idx] == second[idx]:
        continue

    first[idx] = second[idx]
    insertions_and_deletions += 2

print(f"Deletions and Insertions: " + str(insertions_and_deletions))