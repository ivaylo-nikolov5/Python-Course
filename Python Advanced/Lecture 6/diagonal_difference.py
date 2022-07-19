rows = int(input())

matrix = []

for _ in range(rows):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

primary_diagonal = []
secondary_diagonal = []


for idx in range(rows):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][rows - 1 - idx])

diff = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(diff)