def palindrome(number):
    if number < 0 or (number != 0 and number % 10 == 0):
        return False

    number = str(number)
    length = len(number)
    half = length // 2
    left = number[:half]
    right = number[half:][::-1] if length > 1 and length % 2 == 0 else number[half + 1:][::-1]
    return left == right


print(palindrome(10001))
