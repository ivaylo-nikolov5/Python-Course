number = int(input())

for i in range(1, number+1):
    if i < 11:
        working_number = i % 10
    else:
        working_number = (i % 10)+1
    digit_sum = 0
    digit_sum += working_number
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
    digit_sum = 0