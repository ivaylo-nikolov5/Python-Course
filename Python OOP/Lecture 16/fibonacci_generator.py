def fibonacci():
    nums = [0, 1]
    idx = 0
    while True:
        yield nums[idx]
        idx += 1
        next_num = nums[-1] + nums[-2]
        nums.append(next_num)



generator = fibonacci()
for i in range(100):
    print(next(generator))
