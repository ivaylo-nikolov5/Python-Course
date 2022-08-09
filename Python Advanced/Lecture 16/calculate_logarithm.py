from math import log

num = int(input())
log_base = input()
if log_base == "natural":
    log_num = log(num)
else:
    log_num = log(num, int(log_base))

print(f"{log_num:.2f}")