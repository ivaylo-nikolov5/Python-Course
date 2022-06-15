nums = [int(num) for num in input().split(", ")]

beggars = int(input())
beggars_list = [0] * beggars

counter = 0

for num in nums:
    beggars_list[counter] += num
    counter += 1
    if counter >= beggars:
        counter = 0

print(beggars_list)


