def sum_func(number):
    total = 0

    first_letter = number[0]
    second_letter = number[-1]
    num = int(number[1:-1])

    if first_letter.isupper():
        total += num / letters[first_letter.lower()]
    else:
        total += num * letters[first_letter.lower()]

    if second_letter.isupper():
        total -= letters[second_letter.lower()]
    else:
        total += letters[second_letter.lower()]

    return total


def letters_change_numbers(info):
    result = 0
    for x in info:
        result += sum_func(x)

    print(f"{result:.2f}")


letters = {}
a = 1
for x in range(97, 123):
    letters[chr(x)] = a
    a += 1

text = input().split()
letters_change_numbers(text)