n = int(input())

max_num = -1000000000000000000
sum = 0

for i in range(n):
    number = int(input())
    if number > max_num:
        max_num = number
    sum += number

sum -= max_num
diff = abs(sum - max_num)


if max_num == sum:
    print(f"Yes \nSum = {sum}")
else:
    print(f"No \nDiff = {diff}")
