def biggest_formed_number(nums):
    nums.sort(key=lambda x: x * 2, reverse=True)

    return "".join(nums)




numbers = [str(x) for x in input().split(" ")]
print(biggest_formed_number(numbers))