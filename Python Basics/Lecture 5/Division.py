n = int(input())
res_1 = 0
res_2 = 0
res_3 = 0
dev_2 = 0
dev_3 = 0
dev_4 = 0
for i in range(0, n):
    nums = int(input())
    if nums % 2 ==0:
        dev_2 += 1
        res_1 = dev_2/n * 100
    if nums % 3 == 0:
        dev_3 +=1
        res_2 = dev_3/n *100
    if nums % 4 ==0:
        dev_4 += 1
        res_3 = dev_4/n *100

print(f"{res_1:.2f}%")
print(f"{res_2:.2f}%")
print(f"{res_3:.2f}%")

