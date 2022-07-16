lines = int(input())

matrix = []

for _ in range(lines):
    nums = [int(x) for x in input().split(", ")]
    matrix.extend(nums)

print(list(matrix))
