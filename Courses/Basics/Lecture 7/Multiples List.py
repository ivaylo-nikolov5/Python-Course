factor = int(input())
count = int(input())
factor_list = []

for i in range(factor, count * factor+1, factor):
    factor_list.append(i)

print(factor_list)