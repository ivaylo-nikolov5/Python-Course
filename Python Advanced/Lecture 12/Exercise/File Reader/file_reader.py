try:
    with open("numbers.txt") as numbers:
        nums_sum = sum([int(num) for num in numbers.readlines()])
        print(nums_sum)
except FileNotFoundError:
    pass
