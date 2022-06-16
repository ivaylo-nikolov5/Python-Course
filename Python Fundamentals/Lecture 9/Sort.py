def sorting(numbers):
    sort = sorted(list(map(int, numbers.split(" "))))
    return list(sort)


nums = input()

print(sorting(nums))