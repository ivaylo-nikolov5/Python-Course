clothes = [int(x) for x in input().split()]
capacity = int(input())

racks = 1
current_rack = capacity
while clothes:
    current_cloth = clothes[-1]
    if current_cloth > current_rack:
        racks += 1
        current_rack = capacity
    else:
        current_rack -= clothes.pop()

print(racks)