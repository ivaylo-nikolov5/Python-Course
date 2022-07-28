odd_or_even = input()
nums = [int(x) for x in input().split()]

parity = 0 if odd_or_even == "Even" else 1

result = sum(x for x in nums if x % 2 == parity) * len(nums)
print(result)
