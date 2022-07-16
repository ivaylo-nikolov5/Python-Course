rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

res = 0

for i in range(rows):
    res += matrix[i][i]

print(res)