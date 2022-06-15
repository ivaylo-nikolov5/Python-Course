sequence1 = input().split(", ")
sequence2 = input()
same = [el for el in sequence1 if el in sequence2]

print(same)