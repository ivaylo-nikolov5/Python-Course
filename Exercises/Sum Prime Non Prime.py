number = input()

prime_numbers_sum = 0
non_prime_numbers_sum = 0

while number != "stop":
    current_number = int(number)
    if current_number < 0:
        print("Number is negative.")
    else:
        is_number_prime = True
        for i in range(2, current_number):
            if current_number % i == 0:
                is_number_prime = False
                break
        if is_number_prime:
            prime_numbers_sum += current_number
        else:
            non_prime_numbers_sum += current_number

    number = input()

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")