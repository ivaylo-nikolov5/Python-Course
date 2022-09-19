def get_primes(nums):
    for num in nums:
        if num <= 1:
            continue
        flag = False

        for i in range(2, num):
            if num % i == 0:
                flag = True
                break

        if not flag:
            yield num


print(list(get_primes([-2, 0, 0, 1, 1, 0])))