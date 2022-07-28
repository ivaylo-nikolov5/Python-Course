nums = [int(x) for x in input().split()]
positive = [x for x in nums if x >= 0]
negative = [x for x in nums if x < 0]

print(f"{sum(negative)}\n{sum(positive)}")


if abs(sum(negative)) < sum(positive):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")