nums = input().split(" ")
absolute = []

for i in nums:
    i = float(i)
    absolute.append(abs(i))

print(absolute)
