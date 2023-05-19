# def recursive_drawing(idx):
#     if idx < 1:
#         return
#
#     print("*" * idx)
#
#     recursive_drawing(idx - 1)
#
#     print("#" * idx)
#
#
# number = int(input())
#
# recursive_drawing(number)


number = int(input())
temp = number

while temp > 0:
    print("*" * temp)
    temp -= 1

temp += 1

while temp <= number:
    print("#" * temp)
    temp += 1