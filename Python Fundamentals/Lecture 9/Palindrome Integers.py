def check_palindromes(nums):
    for i in nums:
        i = str(i)
        if i == i[::-1]:
            print("True")
        else:
            print("False")


numbers = list(map(int, input().split(", ")))

check_palindromes(numbers)