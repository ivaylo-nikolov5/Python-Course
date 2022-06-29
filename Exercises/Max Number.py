import sys

line = input()

max_num = -sys.maxsize

while line != "Stop":
    num = int(line)

    if num > max_num:
        max_num = num

    line = input()

print(max_num)
