n = int(input())

count_current_longest = 0
count_longest = 0
a_prev = 0


for i in range(0, n):
    a = int(input())

    if a > a_prev:
        count_current_longest +=1
    else:
        count_current_longest = 1

    if count_current_longest > count_longest:
        count_longest = count_current_longest

    a_prev = a

print(count_longest)


