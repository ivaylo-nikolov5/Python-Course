n = int(input())

for i in range(1111, 9999 + 1):
    is_special = True
    i_as_string = str(i)
    for current_number in i_as_string:
        current_number = int(current_number)
        if current_number == 0 or n % current_number != 0:
            is_special = False
            break
        else:
            is_special = True

    if is_special:
        print(i, end=" ")
