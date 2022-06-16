n = int(input())

capacity = 255
in_container = 0

for i in range(n):
    num = int(input())
    if num > capacity:
        print("Insufficient capacity!")
    else:
        capacity -= num
        in_container += num

print(in_container)


