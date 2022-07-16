lines, columns = [int(x) for x in input().split(", ")]
matrix = []
# for _ in range(columns):
#     matrix.append([])
#
# for _ in range(lines):
#     nums = [int(x) for x in input().split()]
#     for i in range(columns):
#         matrix[i].append(nums[i])
#
# for i in matrix:
#     print(sum(i))

for _ in range(lines):
    matrix.append([int(x) for x in input().split()])

for col_index in range(columns):
    res = 0
    for row_index in range(lines):
        res += matrix[row_index][col_index]
    print(res)