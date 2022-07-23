# sub_lists = input().split("|")
#
# matrix = list(reversed(list([x.strip()] for x in sub_lists)))
#
# new_list = []
#
# for pair in matrix:
#     pair = pair[0].split(" ")
#     for el in pair:
#         if el != "":
#             new_list.append(el.strip())
#
# print(*new_list, sep=" ")

################################################################

sublists = input().split("|")

nums = []

while sublists:
    sublist = sublists.pop().split()
    for el in sublist:
        nums.append(el)

print(*nums, sep=" ")