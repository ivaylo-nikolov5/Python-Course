try:
    with open("numbers.txt") as file:
        nums = [int(x) for x in file.readlines()]
        print(sum(nums))
except FileNotFoundError:
    print("File was not found")

