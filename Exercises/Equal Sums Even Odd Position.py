num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):
    odd_sum = 0
    even_sum = 0
    i_as_string = str(i)
    for index, digit in enumerate(i_as_string):
        digit = int(digit)
        if index % 2 == 0:
            odd_sum += digit
        else:
            even_sum += digit

    if odd_sum == even_sum:
        print(f"{i} ", end="")







