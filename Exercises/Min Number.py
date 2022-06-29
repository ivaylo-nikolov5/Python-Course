import sys

line = input()

min_num = sys.maxsize

while line != "Stop":
    num = int(line)
    if num < min_num:
        min_num = num

    line = input()

print(min_num)