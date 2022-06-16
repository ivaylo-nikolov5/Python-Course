def aliquot_sum(number):
    total = 0
    for i in range(1, number):
        if number % i == 0:
            total += i

    if total == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


num = int(input())

aliquot_sum(num)