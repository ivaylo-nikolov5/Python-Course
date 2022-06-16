def rounding(num_list:list):
    rounded_list = []

    for i in num_list:
        i = float(i)
        rounded_list.append(round(i))

    return rounded_list


numbers = input().split(" ")

print(rounding(numbers))