def odd_even_sum(number):
    odd_sum = 0
    even_sum = 0
    for i in number:
        i = int(i)
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


num = input()

odd_even_sum(num)
