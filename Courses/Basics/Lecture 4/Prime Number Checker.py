n = int(input())

is_prime = True

if n % 2 == 0 or n % 3 == 0:
    is_prime = False

print(is_prime)

