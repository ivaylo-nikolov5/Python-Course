def is_prime(num):
    flag = False
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            flag = True
            break

    if not flag:
        return True


def get_primes(nums):
    for num in nums:
        if is_prime(num):
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))